import unittest

class MyTest(unittest.TestCase):

    def test1(self):
        n, m = 10, 10
        board = generate_board(n, m)

    def test2(self):
        n, m = 10, 10
        board = generate_board(n, m)
        self.assertLessEqual(get_active_cells(board, 0, 0), 8)

    def test3(self):
        n,m=10,10
        board = generate_board(n, m)
        self.assertEqual(get_board_cell(board, 10, 10), False)

    def test4(self):
        n,m=10,10
        board = generate_board(n, m)
        self.assertEqual(get_board_cell(board, 20, 20), False)


    def test5(self):
        n,m=10,10
        board = generate_board(n, m)

        new_board = next_stage(board)

        x = number_alive(board)
        y = number_alive(new_board)

        self.assertLessEqual(y, x)



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

def number_alive(board):
    return sum(sum(board[i]) for i in xrange(len(board)))

def next_stage(board):

    n, m = len(board), len(board[0])
    new_board = [[False] * m for _ in xrange(n)]
    for i in xrange(n):
        for j in xrange(m):
            if get_active_cells(board, i, j) in [2, 3] and get_board_cell(board, i, j):
                new_board[i][j] = True
            elif get_active_cells(board, i, j) == 3:
                new_board[i][j] = True

    return new_board

