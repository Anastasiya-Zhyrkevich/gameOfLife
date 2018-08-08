import numpy as np

def get_input_from_file():

    with open('input.txt') as f:
        n, m, k = (int(value) for value in f.readlines()[0].strip().split(' '))
    return n, m, k


def generate_board(n, m):
    board = np.random.randint(0, 2, size=(n, m), dtype=bool)
    return board

'''
# deprecated verion 1
def get_board_cell(board, i, j):
    if i < 0 or j < 0 or i >= board.shape[0] or j >= board.shape[1]:
        return False
    return board[i][j]
'''


def get_board_cell(board, i, j):
    n, m = board.shape
    i = (i + n) % n
    j = (j + m) % m
    return board[i][j]


def is_alive(board, i, j):
    alive_neib_cnt = 0
    for i_offset in xrange(i - 1, i + 2):
        for j_offset in xrange(j - 1, j + 2):
            if i != i_offset or j != j_offset:
                if get_board_cell(board, i_offset, j_offset):
                    alive_neib_cnt += 1

    if alive_neib_cnt in [0, 1, 4, 5, 6, 7, 8]:
        return False
    elif alive_neib_cnt in [2, 3] and board[i][j] == True:
        return True
    elif alive_neib_cnt == 3:
        return True
    else:
        return False


def next_stage(board):
    n, m = board.shape
    new_board = np.zeros(board.shape, dtype=bool)

    for i in xrange(n):
        for j in xrange(m):
            if is_alive(board, i, j):
                new_board[i, j] = True

    return new_board

import unittest

class MyTest(unittest.TestCase):

    def test_1(self):
        board = np.array([1, 0, 0,
                          0, 1, 0,
                          0, 0, 0], dtype=bool).reshape(3, 3)
        new_board = next_stage(board)
        new_board_expected = np.zeros((3, 3), dtype=bool)
        print board
        print new_board
        print new_board_expected

        np.testing.assert_array_equal(new_board, new_board_expected)


if __name__ == '__main__':

    n, m, k = get_input_from_file()
    board = generate_board(n, m)
    print board

    print

    for step in xrange(k):
        new_board = next_stage(board)
        print new_board
        board = new_board
