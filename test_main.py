import unittest
from main import Snake, Meatball, WIDTH, HEIGHT, CELL_SIZE

class TestSnakeGame(unittest.TestCase):
    def setUp(self):
        self.snake = Snake()
        self.meatball = Meatball()

    def test_snake_initial_position(self):
        x, y = self.snake.body[0]
        self.assertTrue(0 <= x < WIDTH)
        self.assertTrue(0 <= y < HEIGHT)

    def test_snake_move(self):
        initial_head = self.snake.body[0]
        self.snake.set_direction((CELL_SIZE, 0))
        self.snake.move()
        new_head = self.snake.body[0]
        self.assertNotEqual(initial_head, new_head)

    def test_snake_grow(self):
        initial_length = len(self.snake.body)
        self.snake.grow()
        self.assertEqual(len(self.snake.body), initial_length + 1)

    def test_snake_collides_with_self(self):
        self.snake.body = [(100, 100), (120, 100), (100, 100)]
        self.assertTrue(self.snake.collides_with_self())

    def test_snake_collides_with_wall(self):
        self.snake.body = [(-20, 100)]
        self.assertTrue(self.snake.collides_with_wall())
        self.snake.body = [(WIDTH, HEIGHT)]
        self.assertTrue(self.snake.collides_with_wall())

    def test_meatball_respawn(self):
        snake_body = [(0, 0), (20, 0), (40, 0)]
        self.meatball.respawn(snake_body)
        self.assertNotIn(self.meatball.position, snake_body)
        x, y = self.meatball.position
        self.assertTrue(0 <= x < WIDTH)
        self.assertTrue(0 <= y < HEIGHT)

if __name__ == "__main__":
    unittest.main()
