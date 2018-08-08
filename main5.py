import unittest

class MyTest(unittest.TestCase):

    def test1(self):
        n, m = 10, 10
        board = generate_board(n, m)

    def test2(self):
        pass

def generate_board(n ,m):
    return [[False] * m for _ in xrange(n)]

def get_board_cell(board, i, j):
    return board[i][j]