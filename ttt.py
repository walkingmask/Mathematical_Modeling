import random
from time import sleep
import numpy as np
import math


# CONSTANTS


FIRST_LIST = [0, 3, 6, 0, 1, 2, 0, 2]
SECOND_LIST = [1, 4, 7, 3, 4, 5, 4, 4]
THIRD_LIST = [2, 5, 8, 6, 7, 8, 8, 6]

NORMAL_P_TABLE = np.array([1/9 for i in range(9)])

FSTDs = [
    [20, 4, 20, 4, 4, 4, 20, 4, 20],  # COR
    [4, 20, 4, 20, 4, 20, 4, 20, 4],  # SID
    [2.5, 2.5, 2.5, 2.5, 80, 2.5, 2.5, 2.5, 2.5],  # CEN
]


# GAME FUNCTIONS


def init_table(table=None):
    return [' ' for i in range(9)]


def mark(table, index, sign):
    if table[index] != ' ':
        return -1
    table[index] = sign
    return 0


def get_choosable_cells(table):
    return [1 if table[i] == ' ' else 0 for i in range(9)]


def judge(table):
    for first, second, third in zip(FIRST_LIST, SECOND_LIST, THIRD_LIST):
        if table[first] != ' ' \
        and table[first] == table[second] \
        and table[first] == table[third]:
            return table[first]  # return winner's sign

    choosable_cells = get_choosable_cells(table)
    if sum(choosable_cells) == 0:
        return 1  # draw

    return 0  # continue


# FUNCTIONS FOR EXPERIMENTS


def recalculate_p_table(p_table):
    return p_table / np.sum(p_table)


def act_with_p_table(table, p_table, sign):
    choosable_cells = get_choosable_cells(table)
    _p_table = recalculate_p_table(np.array(choosable_cells) * p_table)
    index = np.random.choice(range(9), 1, p=_p_table)[0]
    mark(table, index, sign)
    return index


def play_game(player_first_p_table):
    table = init_table()
    sign = 'O'

    first_step = act_with_p_table(table, player_first_p_table, sign)

    while True:
        sign = 'X' if sign == 'O' else 'O'
        act_with_p_table(table, NORMAL_P_TABLE, sign)
        result = judge(table)
        if result != 0:
            return result, first_step


def get_fst(index):
    if index in [0, 2, 6, 8]:
        return 0  # corner
    elif index in [1, 3, 5, 7]:
        return 1  # side
    else:
        return 2  # center


def make_data(n_runs=100):
    # records = [COR[corner[victory, draw, defeat], side, center], SID, CEN]
    records = [
        [[0, 0, 0] for i in range(3)] for i in range(3)
    ]

    for _ in range(n_runs):
        for i in range(3):
            for _ in range(10):
                result, first_step = play_game(FSTDs[i])
                fst = get_fst(first_step)

            if result == 'O':
                records[i][fst][0] += 1
            elif result == 'X':
                records[i][fst][2] += 1
            else:
                records[i][fst][1] += 1

    print("FTSD: [vic, drw, def]")
    print("COR:", [
        sum([records[0][i][0] for i in range(3)]) / sum([sum(records[0][i]) for i in range(3)]),
        sum([records[0][i][1] for i in range(3)]) / sum([sum(records[0][i]) for i in range(3)]),
        sum([records[0][i][2] for i in range(3)]) / sum([sum(records[0][i]) for i in range(3)]),
    ])
    print("SID:", [
        sum([records[1][i][0] for i in range(3)]) / sum([sum(records[1][i]) for i in range(3)]),
        sum([records[1][i][1] for i in range(3)]) / sum([sum(records[1][i]) for i in range(3)]),
        sum([records[1][i][2] for i in range(3)]) / sum([sum(records[1][i]) for i in range(3)]),
    ])
    print("CEN:", [
        sum([records[2][i][0] for i in range(3)]) / sum([sum(records[2][i]) for i in range(3)]),
        sum([records[2][i][1] for i in range(3)]) / sum([sum(records[2][i]) for i in range(3)]),
        sum([records[2][i][2] for i in range(3)]) / sum([sum(records[2][i]) for i in range(3)]),
    ])


def make_datasets(fstd_index, n_datasets=10):
    print("[vic, drw, def]")

    for _ in range(n_datasets):
        records = [0, 0, 0]
        for _ in range(10):
            result, _ = play_game(FSTDs[fstd_index])
            if result == 'O':
                records[0] += 1
            elif result == 'X':
                records[2] += 1
            else:
                records[1] += 1
        print(records)


# MAIN


if __name__ == '__main__':
    print('data:')
    make_data(100)
    print()

    print('dataset:')
    make_datasets(2)
