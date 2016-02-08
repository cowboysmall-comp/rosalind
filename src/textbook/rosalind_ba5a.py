import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import algorithms


def main(argv):
    lines = files.read_lines(argv[0])
    money = int(lines[0])
    coins = [int(coin) for coin in lines[1].split(',')]

    print algorithms.minimum_coins(coins, money)


if __name__ == "__main__":
    main(sys.argv[1:])
