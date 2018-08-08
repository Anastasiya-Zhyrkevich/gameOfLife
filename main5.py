import unittest

class MyTest(unittest.TestCase):

    def test1(self):
        n, m = 10, 10
        board = generate_board(n, m)

    def test2(self):
        n, m = 10, 10
        board = generate_board(n, m)
        self.assertLessEqual(get_active_cells(board, 0, 0), 8)


def generate_board(n ,m):
    return [[False] * m for _ in xrange(n)]

def get_board_cell(board, i, j):
    if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
        return False
    return board[i][j]

def get_active_cells(board, i, j):
    alive = 0
    for ii in xrange(-1, 2):
        for jj in xrange(-1, 2):
            alive += int(get_board_cell(board, i + ii, j + jj))
    return alive