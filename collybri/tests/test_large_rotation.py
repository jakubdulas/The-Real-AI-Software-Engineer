import unittest
import sys
import os
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from models.models import User
from models.rotate_meetings import rotate_pairs_with_breaks

class TestLargeScaleRotationPerformance(unittest.TestCase):
    def test_even_large_rotation(self):
        users = [User(user_id=i, name=f"U{i}") for i in range(200)]
        t0 = time.time()
        pairs, state = rotate_pairs_with_breaks(users, set())
        t1 = time.time()
        seen = set()
        for a, b in pairs:
            seen.add(a.user_id)
            if b is not None:
                seen.add(b.user_id)
        self.assertEqual(len(seen), 200)
        self.assertEqual(len(pairs), 100)
        self.assertLess(t1-t0, 2.0)

    def test_odd_large_rotation(self):
        users = [User(user_id=i, name=f"U{i}") for i in range(201)]
        t0 = time.time()
        pairs, state = rotate_pairs_with_breaks(users, set())
        t1 = time.time()
        seen = set()
        lone = None
        for a, b in pairs:
            seen.add(a.user_id)
            if b is None:
                lone = a.user_id
            else:
                seen.add(b.user_id)
        self.assertEqual(len(seen), 201)
        self.assertTrue(any(b is None for _, b in pairs))
        self.assertLess(t1-t0, 2.0)

    def test_large_rotation_with_majority_breaks(self):
        users = [User(user_id=i, name=f"U{i}") for i in range(120)]
        # Half on break
        breaks = set(u.user_id for u in users[:60])
        t0 = time.time()
        pairs, state = rotate_pairs_with_breaks(users, breaks)
        t1 = time.time()
        seen = set()
        for a, b in pairs:
            seen.add(a.user_id)
            if b:
                seen.add(b.user_id)
        self.assertEqual(len(seen), 60)
        self.assertEqual(len(pairs), 30)
        self.assertLess(t1-t0, 2.0)

    def test_unschedulable_best_effort_partition(self):
        users = [User(user_id=i, name=f"U{i}") for i in range(105)]
        # Can't do full 1vs1 for all, but system must still return best-effort
        t0 = time.time()
        pairs, state = rotate_pairs_with_breaks(users, set())
        t1 = time.time()
        paired_ids = set()
        singletons = 0
        for u1, u2 in pairs:
            paired_ids.add(u1.user_id)
            if u2 is None:
                singletons += 1
            else:
                paired_ids.add(u2.user_id)
        self.assertEqual(len(paired_ids), 105)
        self.assertEqual(singletons, 1)
        self.assertLess(t1-t0, 2.0)

    def test_large_preference_rotation(self):
        N = 110
        users = [User(user_id=i, name=f"U{i}") for i in range(N)]
        # Reverse preference: prefer highest id
        def prefer_highest(user, candidates):
            return sorted(candidates, key=lambda x: -x.user_id)
        t0 = time.time()
        pairs, state = rotate_pairs_with_breaks(users, set(), user_sort_fn=prefer_highest)
        t1 = time.time()
        all_ids = set()
        for a, b in pairs:
            all_ids.add(a.user_id)
            if b: all_ids.add(b.user_id)
        self.assertEqual(len(all_ids), N)
        self.assertLess(t1-t0, 2.0)

if __name__ == "__main__":
    unittest.main()
