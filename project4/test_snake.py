import unittest
from snake import Snake

class TestSnake(unittest.TestCase):
    def setUp(self):
        self.snake = Snake(init_pos=(5, 5), init_length=3, direction=(1, 0))  # Horizontal, to the right

    def test_initial_body(self):
        expected_body = [(5, 5), (4, 5), (3, 5)]
        self.assertEqual(self.snake.get_body(), expected_body)

    def test_move_forward(self):
        self.snake.move()
        expected_body = [(6, 5), (5, 5), (4, 5)]
        self.assertEqual(self.snake.get_body(), expected_body)

    def test_change_direction_and_move(self):
        self.snake.set_direction((0, 1))  # Move down
        self.snake.move()
        expected_body = [(5, 6), (5, 5), (4, 5)]
        self.assertEqual(self.snake.get_body(), expected_body)

    def test_grow(self):
        self.snake.grow()
        self.snake.move()
        expected_body = [(6, 5), (5, 5), (4, 5), (3, 5)]
        self.assertEqual(self.snake.get_body(), expected_body)

    def test_no_reverse_direction(self):
        self.snake.set_direction((-1, 0))  # Attempt to reverse
        self.snake.move()
        expected_body = [(6, 5), (5, 5), (4, 5)]  # Should still move right
        self.assertEqual(self.snake.get_body(), expected_body)

if __name__ == "__main__":
    unittest.main()
