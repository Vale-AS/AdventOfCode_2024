import time
import numpy as np
from math import isclose
from copy import deepcopy

class Day13:
    def __init__(self, filename):
        self.mats = []
        with open(filename) as f:
            data = f.read().split('\n\n')
            for machine in data:
                a_button, b_button, prize_loc = machine.split('\n')
                a_col = [int(e) for e in a_button[12:].split(', Y+')]
                b_col = [int(e) for e in b_button[12:].split(', Y+')]
                prize_col = [int(e) for e in prize_loc[9:].split(', Y=')]
                mat = np.column_stack((a_col,b_col,prize_col))
                self.mats.append(mat)

    def part1(self):
        token_cost = 0
        matrices = deepcopy(self.mats)
        for m in matrices:
            token_cost += mini_gauss_and_token_calc(m)
        print(int(token_cost))

    def part2(self):
        matrices = deepcopy(self.mats)
        matrices = adjust_prizes(matrices)
        token_cost = 0
        for m in matrices:
            token_cost += mini_gauss_and_token_calc(m)
        print(token_cost)
    
    def both_parts(self):
        matrices1 = deepcopy(self.mats)
        matrices2 = adjust_prizes(deepcopy(self.mats))
        tkn_cost1 = 0
        tkn_cost2 = 0
        for i in range(len(matrices1)):
            m1 = matrices1[i]
            tkn_cost1 += mini_gauss_and_token_calc(m1)
            m2 = matrices2[i]
            tkn_cost2 += mini_gauss_and_token_calc(m2)
        print(f'part 1 result is: {tkn_cost1} and part 2 result is: {tkn_cost2}')

def mini_gauss_and_token_calc(matrix):
    f1 = matrix[0]
    f2 = matrix[1]
    f2 = f2-(f1*(f2[0]/f1[0]))
    f2 = f2/(f2[1])
    f1 = f1-(f2*(f1[1]))
    f1 = f1/(f1[0])
    a, b = f1[2], f2[2]
    res = np.array([a,b])
    rounded_res = np.array([round(a), round(b)])
    if np.allclose(res, rounded_res,rtol=1e-14,atol=0) and a >= 0 and b >= 0:
        return 3*round(a) + round(b)
    else:
        return 0


def adjust_prizes(mats: list[np.ndarray]):
    for i in range(len(mats)):
        m = mats[i]
        prize_col = m[:,-1:]
        new_prize_col = []
        for num in prize_col:
            n = num[0]
            new_num = 10000000000000+n
            new_prize_col.append(new_num)
        mats[i][:,-1] = new_prize_col
    return mats

start = time.time()
puzzle = Day13("inputs/day13.txt")
#puzzle.part1()
#puzzle.part2()
puzzle.both_parts()
end = time.time()
print(f'Elapsed time: {end - start}s')