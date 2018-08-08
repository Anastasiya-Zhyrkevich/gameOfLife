import unittest
import random

class MyTest(unittest.TestCase):

    def test_edge(self):
        n = 10
        board = [[0] * n for _ in xrange(n)]

        alive_neigb = get_alive_neigb(board, 0, 0)

        self.assertEqual(alive_neigb, 0)

    def test_edge_right(self):
        n, m = 10, 1
        board = [[0] * m for _ in xrange(n)]

        alive_neigb = get_alive_neigb(board, 9, 0)

        self.assertEqual(alive_neigb, 0)

    def test_is_alive(self):
        n, m = 10, 1
        board = [[0] * m for _ in xrange(n)]

        is_alive_value = is_alive(board, 0, 9)

        self.assertEqual(is_alive_value, False)

    def test_1_diag(self):
        n = 10
        board = [[0] * n for _ in xrange(n)]

        board[3][3] = 1

        alive_neigb = get_alive_neigb(board, 4, 4)

        self.assertEqual(alive_neigb, 1)

    def test_1_boarder(self):
        n = 10
        board = [[0] * n for _ in xrange(n)]

        board[3][3] = 1

        alive_neigb = get_alive_neigb(board, 4, 3)

        self.assertEqual(alive_neigb, 1)

    def test_next_state_1(self):
        n = 10
        board = [[0] * n for _ in xrange(n)]

        board[3][3] = 1

        is_alive = is_next_state_alive(board, 4, 4)

        self.assertEqual(is_alive, False)

    def test_next_state_2(self):
        n = 10
        board = [[0] * n for _ in xrange(n)]

        board[3][3] = 1
        board[2][2] = 1
        board[2][3] = 1

        is_alive = is_next_state_alive(board, 3, 2)

        self.assertEqual(is_alive, True)

    def test_next_state_3(self):
        n = 10
        board = [[0] * n for _ in xrange(n)]

        board[3][3] = 1
        board[2][2] = 1
        board[2][3] = 1

        is_alive = is_next_state_alive(board, 3, 3)

        self.assertEqual(is_alive, True)


    def test_gen_new_stage_blinker(self):
        n = 5
        board = [[0] * n for _ in xrange(n)]

        board[2][2] = 1
        board[2][1] = 1
        board[2][3] = 1

        new_board = generate_next_stage(board)

        new_board_expected = [[0] * n for _ in xrange(n)]
        new_board_expected[1][2] = 1
        new_board_expected[2][2] = 1
        new_board_expected[3][2] = 1

        self.assertEqual(new_board, new_board_expected)

    def test_gen_new_stage_block(self):
        n = 5
        board = [[0] * n for _ in xrange(n)]

        board[1][1] = 1
        board[1][2] = 1
        board[2][1] = 1
        board[2][2] = 1

        new_board = generate_next_stage(board)

        self.assertEqual(new_board, board)

    def test_init(self):
        n = 5
        m = 3

        new_board = generate_init(n,m)

        self.assertEqual(len(new_board), n)
        self.assertEqual(len(new_board[0]), m)

def get_alive_neigb(board, i, j):
    count = 0
    for x in range(i-1,i+2):
        for y in range(j-1,j+2):
            if i == x and j == y:
                pass
            else:
                count = count + int(is_alive(board,x,y))

    return count

def is_alive(board,i,j):

    if i < 0 or j < 0 or j >= len(board[0]) or i >= len(board):
        return 0
    return board[i][j]

def is_next_state_alive(board, i, j):
    alive_neib = get_alive_neigb(board, i, j)

    if alive_neib in [2, 3] and is_alive(board, i, j):
        return True
    elif alive_neib == 3:
        return True
    else:
        return False

def generate_next_stage(board):
    new_board = [[False] * len(board[0]) for _ in xrange(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if is_next_state_alive(board,i,j):
                new_board[i][j] = True
    return new_board

def generate_init(n, m):
    board = [[bool(random.randint(0, 1)) for _ in xrange(m)] for _ in xrange(n)]
    return board


if __name__ == '__main__':
    n, m, steps = 5, 3, 2
    board = generate_init(n, m)
    print board

    for _ in xrange(steps):
        board = generate_next_stage(board)
        print board
