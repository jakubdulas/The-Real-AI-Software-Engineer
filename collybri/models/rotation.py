from typing import List, Tuple, Dict, Set, Callable, Optional
from models.models import User, CandidateSorter
from dataclasses import dataclass, field


@dataclass
class RotationState:
    """
    Tracks the current state of meeting rotations.

    Attributes:
        met_pairs (Set[frozenset]): Set of frozensets containing user_id pairs that have already met.
        user_on_break (Set[int]): Set of user_ids scheduled for a break in the current rotation.
        round_number (int): Tracks the current round of rotation.
    """

    met_pairs: Set[frozenset] = field(default_factory=set)
    user_on_break: Set[int] = field(default_factory=set)
    round_number: int = 0


def pair_users_for_1on1(
    users: List[User], sort_candidates_fn: Optional[CandidateSorter] = None
) -> List[Tuple[User, User]]:
    """
    Creates 1vs1 meeting pairs from a list of users, skipping those marked as 'on_break'.
    All available users are paired as fairly as possible (no user is paired twice in a round).
    If there's an odd number of available users, the last one will be left out (should be handled by higher level logic).
    Users are paired using the optionally provided candidate-sorting function.

    Args:
        users (List[User]): List of User objects.
        sort_candidates_fn (Optional[CandidateSorter]):
            Optionally, a callable (user, candidates_list) -> sorted_candidates_list for custom pairing priority.
            For example, if you want to prioritize by similar interest:

            def preference_based_sort(user, candidates):
                return sorted(candidates, key=lambda u: similarity(user.preferences, u.preferences), reverse=True)

            pairs = pair_users_for_1on1(users, sort_candidates_fn=preference_based_sort)

    Returns:
        List[Tuple[User, User]]: List of paired tuples for meetings.
    """
    available_users = [user for user in users if not user.on_break]
    used = set()
    pairs = []
    n = len(available_users)
    for i, user in enumerate(available_users):
        if user.user_id in used:
            continue
        # Get candidate partners
        candidates = [
            u
            for u in available_users
            if u.user_id not in used and u.user_id != user.user_id
        ]
        if sort_candidates_fn:
            candidates = sort_candidates_fn(user, candidates)
        if candidates:
            partner = candidates[0]
            pairs.append((user, partner))
            used.add(user.user_id)
            used.add(partner.user_id)
    return pairs


def next_rotation(
    users: List[User],
    rotation_state: RotationState,
    sort_candidates_fn: Optional[CandidateSorter] = None,
) -> Tuple[List[Tuple[User, User]], RotationState]:
    """
    Given the current rotation state and users, schedules the next round of 1vs1 meeting pairs and updates the state.
    Skips users scheduled for a break this round, rotates users off their breaks.
    Ensures that, as best as possible, pairs haven't previously met (based on met_pairs) this event.
    Allows passing a function that sorts pairing candidates for each user.

    Args:
        users (List[User]): List of all User objects (their 'on_break' should be up-to-date).
        rotation_state (RotationState): Current rotation state.
        sort_candidates_fn (Optional[CandidateSorter]):
            If provided, controls the order in which candidate pairs are selected. Example:
                def prefer_higher_ids(user, candidates):
                    return sorted(candidates, key=lambda u: u.user_id, reverse=True)
                pairs, new_state = next_rotation(users, rotation_state, sort_candidates_fn=prefer_higher_ids)

    Returns:
        Tuple containing:
            - List of tuples (User, User) for this round.
            - Updated RotationState reflecting new pairs and break status.
    """
    # Prepare break handling
    new_user_on_break = set()
    for user in users:
        if user.on_break:
            new_user_on_break.discard(user.user_id)
        elif user.user_id in rotation_state.user_on_break:
            user.on_break = False

    available = [
        user for user in users if user.user_id not in rotation_state.user_on_break
    ]
    # for stable pairing order if no sort function provided
    available.sort(key=lambda u: u.user_id)
    used = set()  # Track user_ids paired this round
    pairs = []
    for user in available:
        if user.user_id in used:
            continue
        candidates = [
            u
            for u in available
            if u.user_id not in used
            and u.user_id != user.user_id
            and frozenset([user.user_id, u.user_id]) not in rotation_state.met_pairs
        ]
        if sort_candidates_fn:
            candidates = sort_candidates_fn(user, candidates)
        partner = candidates[0] if candidates else None
        if partner:
            pairs.append((user, partner))
            used.add(user.user_id)
            used.add(partner.user_id)
            rotation_state.met_pairs.add(frozenset([user.user_id, partner.user_id]))
        else:
            # fallback: try to pair even if already met, for fairness
            candidates = [
                u
                for u in available
                if u.user_id not in used and u.user_id != user.user_id
            ]
            if sort_candidates_fn:
                candidates = sort_candidates_fn(user, candidates)
            fallback_partner = candidates[0] if candidates else None
            if fallback_partner:
                pairs.append((user, fallback_partner))
                used.add(user.user_id)
                used.add(fallback_partner.user_id)
                rotation_state.met_pairs.add(
                    frozenset([user.user_id, fallback_partner.user_id])
                )
            # else: this user will go on break
    # The rest (odd user out, or those explicitly scheduled on break) get a break this round
    all_paired = {uid for pair in pairs for uid in [pair[0].user_id, pair[1].user_id]}
    for user in users:
        if user.user_id not in all_paired:
            user.on_break = True
            new_user_on_break.add(user.user_id)
        else:
            user.on_break = False
    new_rotation = RotationState(
        met_pairs=rotation_state.met_pairs.copy(),
        user_on_break=new_user_on_break,
        round_number=rotation_state.round_number + 1,
    )
    return pairs, new_rotation
