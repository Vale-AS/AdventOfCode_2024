import time

class Day7:
    def __init__(self, filename):
        self.test_values = []
        self.equations = []
        with open(filename) as f:
            data = f.readlines()
            for line in data:
                nums = line.split(': ')
                self.test_values.append(int(nums[0]))
                factors = [int(x) for x in nums[1].split(' ')]
                self.equations.append(factors)
    
    def part1(self):
        total_calibration_result = 0
        for i in range(len(self.test_values)):
            test_val = self.test_values[i]
            eq = self.equations[i]
            sat = does_satisfy(test_val, eq, 1)
            if sat:
                total_calibration_result += test_val
        print(total_calibration_result)
    
    def part2(self):
        total_calibration_result = 0
        for i in range(len(self.test_values)):
            test_val = self.test_values[i]
            eq = self.equations[i]
            sat = does_satisfy(test_val, eq, 2)
            if sat:
                total_calibration_result += test_val
        print(total_calibration_result)

def does_satisfy(val: int, eq: list[int], part) -> bool:
    op_num = len(eq)-1
    op_combs = calc_op_combos(op_num, part)
    for c in op_combs:
        res = eq[0]
        i = 0
        op = 0
        while i < len(c):
            if c[i] == '|':
                res = apply_op(c[i:i+2],res,eq[op+1])
                i += 2
            else:
                res = apply_op(c[i],res,eq[op+1])
                i+= 1
            op += 1
        if res == val:
            return True    
    return False

def calc_op_combos(num: int, part: int) -> list[str]:
    if num == 0:
        combos = []
    elif num == 1:
        combos = ['+','*']
        combos += ['||'] if part==2 else []
    else:
        small_combos = calc_op_combos(num-1, part)
        plus_combos = ['+'+l for l in small_combos]
        mul_combos = ['*'+l for l in small_combos]
        concat_combos = ['||'+l for l in small_combos] if part==2 else []
        combos = plus_combos+mul_combos+concat_combos
    return combos

def apply_op(op: str, x: int, y: int) -> int:
    if op == '+':
        return x + y
    if op == '*':
        return x * y
    if op == '||':
        return int(str(x)+str(y))

start = time.time()
puzzle = Day7("inputs/day7.txt")
puzzle.part1()
#puzzle.part2()
end = time.time()
print(f'Elapsed time: {end - start}s')