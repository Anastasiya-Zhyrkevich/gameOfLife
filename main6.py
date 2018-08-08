
from __future__ import print_function

from  scipy import signal
from scipy import ndimage
import numpy as np


template = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]


def not_confident(x):
    if x == 2:
        return 1
    if x == 3:
        return 2
    return 0

def next_stage(board):

    svertka = signal.convolve2d(board, template, mode='same')

    a1 = ndimage.filters.generic_filter(svertka, not_confident, size = 1)

    a2 = a1 + board


    a2 = np.array(a2)


    a3 = np.array(a2 >= 2, dtype=int)
    return a3


from itertools import product
import termcolor

def green_cell():
    print(termcolor.colored('  ', 'grey', 'on_magenta'), end='')

def white_cell():
    print(termcolor.colored('  ', 'grey', 'on_cyan'), end='')

class Game:

    def __init__(self, init_state, board_size):
        self.board = init_state
        self.size = board_size

    def count_neighbours(self, row, col):
        cnt = 0
        for i, j in product(range(-1, 2), range(-1, 2)):
            cnt += self.board[(row + i) % self.size][(col + j) % self.size]

        return cnt - self.board[row][col]

    def step(self):
        self.board = next_stage(self.board)

    def draw(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j]:
                    green_cell()
                else:
                    white_cell()
            print()


import time
import sys
import subprocess

PATTERN = np.random.randint(0, 2, (100, 100))

if __name__ == '__main__':


    g = Game(PATTERN, 100)
    while(True):
        subprocess.call('clear')
        g.draw()
        g.step()
        time.sleep(1)

