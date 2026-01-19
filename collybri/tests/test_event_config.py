import unittest
from models.event_config import EventConfig
from models.models import User
from typing import List

def custom_sort(user: User, users: List[User]) -> List[User]:
    # Sort users in reverse alphabetical order by name for test
    return sorted(users, key=lambda u: u.name, reverse=True)

class TestEventConfig(unittest.TestCase):
    def setUp(self):
        self.user1 = User(user_id=1, name="Alice")
        self.user2 = User(user_id=2, name="Bob")
        self.user3 = User(user_id=3, name="Charlie")

    def test_defaults(self):
        cfg = EventConfig()
        self.assertTrue(cfg.all_in_one_room)
        self.assertIsNone(cfg.user_sort_func)
        self.assertEqual(cfg.initial_users, [])

    def test_toggle_all_in_one_room(self):
        cfg = EventConfig(all_in_one_room=False)
        self.assertFalse(cfg.all_in_one_room)
        cfg2 = EventConfig(all_in_one_room=True)
        self.assertTrue(cfg2.all_in_one_room)

    def test_add_user(self):
        cfg = EventConfig()
        cfg.add_user(self.user1)
        self.assertIn(self.user1, cfg.initial_users)
        cfg.add_user(self.user2)
        self.assertEqual(cfg.initial_users, [self.user1, self.user2])

    def test_initial_users(self):
        cfg = EventConfig(initial_users=[self.user1, self.user2])
        self.assertEqual(cfg.initial_users, [self.user1, self.user2])

    def test_set_user_sort_func(self):
        cfg = EventConfig()
        cfg.set_user_sort_func(custom_sort)
        self.assertIsNotNone(cfg.user_sort_func)
        users = [self.user2, self.user3]
        sorted_users = cfg.user_sort_func(self.user1, users)
        self.assertEqual(sorted_users, [self.user3, self.user2])  # Charlie > Bob

    def test_repr(self):
        cfg = EventConfig(initial_users=[self.user1])
        rep = repr(cfg)
        self.assertIn("all_in_one_room", rep)
        self.assertIn("initial_users=1", rep)

if __name__ == "__main__":
    unittest.main()
