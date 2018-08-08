import unittest
import random
from itertools import product

class MyTest(unittest.TestCase):

    def setUp(self):
        self.expected_w = random.randint(5, 100)
        self.expected_h = random.randint(5, 100)
        self.board = generate_board(self.expected_h, self.expected_w)

    def test_generate_board(self):
        computed_w = self.board.w
        computed_h = self.board.h

        self.assertEqual(computed_w, self.expected_w)
        self.assertEqual(computed_h, self.expected_h)

    def test_get_board_cell(self):
        for i, j in product(range(self.expected_h + 1), range(self.expected_w + 1)):
            self.assertIn(self.board.get_board_cell(i, j),  [True, False])

    def test_get_alive_num_neighbours(self):
        self.board.clear()
        to_set = random.randrange(0, self.expected_h), random.randrange(0, self.expected_w)
        self.board.set_value(to_set[0], to_set[1], True)

        offsets = [(0, -1), (0, 1), (-1, 1)]
        offset = random.choice(offsets)

        self.assertEqual(self.board.get_alive_cells(to_set[0] + offset[0], to_set[1] + offset[1]), 1)

    def test_get_alive_num_neighbours(self):
        self.board.clear()
        to_set = random.randrange(0, self.expected_h), random.randrange(0, self.expected_w)
        self.board.set_value(to_set[0], to_set[1], True)

        offsets = [(0, 0)]
        offset = random.choice(offsets)

        self.assertEqual(self.board.get_alive_cells(to_set[0] + offset[0], to_set[1] + offset[1]), 0)


    def test_will_be_alive_cell(self):
        self.board.clear()
        to_set = random.randrange(0, self.expected_h), random.randrange(0, self.expected_w)
        self.board.set_value(to_set[0], to_set[1], True)

        offsets = [(0, -1), (0, 1), (-1, 1)]
        offset = random.choice(offsets)

        self.assertEqual(self.board.will_be_alive(to_set[0] + offset[0], to_set[1] + offset[1]), False)



class Board(object):
    def __init__(self, n, m):
        self.w = m
        self.h = n
        self.board = [[False] * self.w for _ in xrange(self.h)]

    def get_board_cell(self, i, j):
        if i < 0 or j < 0 or i >= self.h or j >= self.w:
            return False
        return self.board[i][j]

    def set_value(self, i, j, value):
        self.board[i][j] = value

    def clear(self):
        for i in xrange(self.h):
            for j in xrange(self.w):
                self.set_value(i, j, False)

    def get_alive_cells(self, i, j):
        alive = 0
        for i_off in xrange(-1, 2):
            for j_off in xrange(-1, 2):
                if i_off != i or j_off != j:
                    alive += int(self.get_board_cell(i + i_off, j + j_off))
        return alive



def generate_board(n, m):
    return Board(n, m)
