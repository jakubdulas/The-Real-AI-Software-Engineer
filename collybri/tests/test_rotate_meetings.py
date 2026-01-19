import unittest
from models.models import User
from models.rotate_meetings import rotate_pairs_with_breaks, RotationState

class TestRotateMeetings(unittest.TestCase):
    def setUp(self):
        self.users = [User(user_id=str(i), name=f"User{i}") for i in range(6)]

    def test_basic_pairing(self):
        pairs, state = rotate_pairs_with_breaks(self.users, set())
        self.assertEqual(len(pairs), 3)
        all_ids = set(u.user_id for pair in pairs for u in pair if u is not None)
        expected_ids = set(str(i) for i in range(6))
        self.assertEqual(all_ids, expected_ids)

    def test_break_users(self):
        # User 1 and User 2 are on break
        break_ids = {"1", "2"}
        pairs, state = rotate_pairs_with_breaks(self.users, break_ids)
        active_ids = [u.user_id for u in self.users if u.user_id not in break_ids]
        # Only 4 users should be paired
        self.assertEqual(len(pairs), 2)
        for pair in pairs:
            self.assertTrue(pair[0].user_id in active_ids)
            self.assertTrue(pair[1].user_id in active_ids)
    
    def test_odd_user_break(self):
        # Remove one user to make it odd
        users = self.users[:-1]  # 5 users
        break_ids = {"4"}  # User 4 on break
        pairs, state = rotate_pairs_with_breaks(users, break_ids)
        # Should be two pairs and one with None
        num_none = sum(1 for _, v in pairs if v is None)
        self.assertEqual(len(pairs), 2)
        self.assertEqual(num_none, 0)  # 4 users: 2 pairs, so no None
        # Add break to make 3, active 2
        pairs, state = rotate_pairs_with_breaks(users, {"1", "3"})
        self.assertEqual(len(pairs), 1)

    def test_rotation_carries_state(self):
        # Do two consecutive rounds and check rotation index
        pairs1, state1 = rotate_pairs_with_breaks(self.users, set())
        pairs2, state2 = rotate_pairs_with_breaks(self.users, set(), state1)
        # The order of pairing should rotate
        # The first pair's user id should change
        self.assertNotEqual(pairs1[0][0].user_id, pairs2[0][0].user_id)

    def test_break_users_rejoin_next_round(self):
        # Round 1: users 0, 1 on break
        pairs1, state1 = rotate_pairs_with_breaks(self.users, {"0", "1"})
        paired_ids_r1 = set(u.user_id for pair in pairs1 for u in pair if u)
        self.assertNotIn("0", paired_ids_r1)
        self.assertNotIn("1", paired_ids_r1)
        # Round 2: all join back
        pairs2, state2 = rotate_pairs_with_breaks(self.users, set(), state1)
        paired_ids_r2 = set(u.user_id for pair in pairs2 for u in pair if u)
        self.assertIn("0", paired_ids_r2)
        self.assertIn("1", paired_ids_r2)

if __name__ == '__main__':
    unittest.main()
