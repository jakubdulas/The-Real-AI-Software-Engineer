import unittest
from models.models import User
from models.rotate_meetings import RotationState, rotate_pairs_with_breaks
from typing import List

class TestRotateMeetingsWithPreferences(unittest.TestCase):
    def setUp(self):
        # 6 users for easier preference simulation
        self.users = [User(user_id=i, name=f"User{i}") for i in range(1, 7)]

    def test_default_round_robin(self):
        pairs, state = rotate_pairs_with_breaks(self.users, set())
        self.assertEqual(len(pairs), 3)
        paired_ids = {u.user_id for tup in pairs for u in tup if u}
        self.assertEqual({u.user_id for u in self.users}, paired_ids)

    def test_custom_preference_fn(self):
        # Preference: user prefers to match with highest-numbered user possible
        def prefer_highest(user, others: List[User]) -> List[User]:
            return sorted(others, key=lambda u: -u.user_id)
        pairs, state = rotate_pairs_with_breaks(self.users, set(), user_sort_fn=prefer_highest)
        for user1, user2 in pairs:
            if user2:
                self.assertTrue(user2.user_id < user1.user_id or user2.user_id == max(u.user_id for u in self.users if u != user1))
        self.assertEqual(len(pairs), 3)

    def test_breaks_are_honored(self):
        breaking = {self.users[2].user_id, self.users[4].user_id}  # User 3 and 5 on break
        pairs, state = rotate_pairs_with_breaks(self.users, breaking)
        paired_ids = {u.user_id for tup in pairs for u in tup if u}
        for bid in breaking:
            self.assertNotIn(bid, paired_ids)
        # Odd count minus breaks gives correct pairs
        self.assertEqual(len(pairs), 2)

    def test_edge_case_incomplete_preferences(self):
        # Preference: User 1 (only) has a specific preference; others default
        def user1_pref(user, others: List[User]) -> List[User]:
            if user.user_id == 1:
                # Only consider user 4
                return [o for o in others if o.user_id == 4] + [o for o in others if o.user_id != 4]
            return others
        pairs, state = rotate_pairs_with_breaks(self.users[:4], set(), user_sort_fn=user1_pref)
        user1_pair = [tup for tup in pairs if tup[0].user_id == 1 or (tup[1] and tup[1].user_id == 1)][0]
        # User 1 matched with user 4
        self.assertIn(4, (user1_pair[0].user_id, user1_pair[1].user_id))

    def test_preference_with_odd_leftover(self):
        # Preference: Always choose lowest-numbered partner
        def prefer_lowest(user, others):
            return sorted(others, key=lambda u: u.user_id)
        pairs, state = rotate_pairs_with_breaks(self.users[:5], set(), user_sort_fn=prefer_lowest)
        # There should be 2 pairs, 1 None leftover
        self.assertEqual(len(pairs), 3)
        none_found = any(pair[1] is None for pair in pairs)
        self.assertTrue(none_found)

    def test_no_duplicates_in_pairs(self):
        def dummy_fn(user, others):
            return others[::-1]
        pairs, state = rotate_pairs_with_breaks(self.users, set(), user_sort_fn=dummy_fn)
        paired_ids = set()
        for a, b in pairs:
            self.assertNotEqual(a.user_id, b.user_id if b else None)
            self.assertNotIn(a.user_id, paired_ids)
            if b: self.assertNotIn(b.user_id, paired_ids)
            paired_ids.add(a.user_id)
            if b:
                paired_ids.add(b.user_id)
        # All users are paired
        self.assertEqual(paired_ids, {u.user_id for u in self.users})

if __name__ == "__main__":
    unittest.main()
