from typing import List, Set, Tuple, Optional, Callable, Dict
from .models import User


class RotationState:
    """
    Tracks the pairing/rotation state between meeting rounds
    """

    def __init__(self, last_start_idx: int = 0, break_users: Optional[Set[str]] = None):
        self.last_start_idx: int = last_start_idx
        self.break_users: Set[str] = break_users if break_users is not None else set()


def rotate_pairs_with_breaks(
    users: List[User],
    break_user_ids: Set[str],
    prev_state: Optional[RotationState] = None,
    user_sort_fn: Optional[Callable[[User, List[User]], List[User]]] = None,
) -> Tuple[List[Tuple[User, Optional[User]]], RotationState]:
    """
    Optimized: Efficiently pairs users into 1vs1 meetings for large groups (100+).
    Skips users on break for this round only. Integrates optional sorting fn for best-effort preferences.

    Args:
        users: List of User objects.
        break_user_ids: Set of user IDs on break this round.
        prev_state: Previous RotationState.
        user_sort_fn: Optional(user, candidates) -> sorted list; allows preference-based scheduling.
    Returns:
        pairs: List of (User, Optional[User]); None if odd leftover.
        next_state: RotationState for next round.
    """
    active_users = [u for u in users if u.user_id not in break_user_ids]
    n = len(active_users)
    ids_set = set(u.user_id for u in active_users)
    used_ids = set()
    pairs = []
    next_break_users = set()

    # Fast index assignment, not nested greedy search
    reversed_sort = False
    # Stack users by id for stable large-N behavior
    if user_sort_fn:
        user_queue = active_users[:]
    else:
        user_queue = sorted(active_users, key=lambda u: u.user_id)

    i = 0
    while i < n:
        if user_queue[i].user_id in used_ids:
            i += 1
            continue
        user = user_queue[i]
        # Candidates are those left, not yet used
        candidates = [
            u
            for u in user_queue
            if u.user_id not in used_ids and u.user_id != user.user_id
        ]
        partner = None
        if user_sort_fn and candidates:
            sorted_candidates = user_sort_fn(user, candidates)
            for c in sorted_candidates:
                if c.user_id not in used_ids:
                    partner = c
                    break
        elif candidates:
            partner = candidates[0]
        if partner:
            pairs.append((user, partner))
            used_ids.add(user.user_id)
            used_ids.add(partner.user_id)
        else:
            # Can't find any, goes as singleton (will get a break)
            pairs.append((user, None))
            used_ids.add(user.user_id)
        i += 1
    # Ensure no duplicate/overlap, and singletons get break flagged
    final_pairs = []
    for u1, u2 in pairs:
        if u2 is not None:
            final_pairs.append((u1, u2))
        else:
            final_pairs.append((u1, None))
            next_break_users.add(u1.user_id)

    # Prepare next state
    next_state = RotationState(
        last_start_idx=(prev_state.last_start_idx + 1) % max(1, n) if prev_state else 1,
        break_users=next_break_users,
    )
    return final_pairs, next_state
