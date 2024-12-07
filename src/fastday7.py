import time
import math

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

def does_satisfy(val: int, eq: list[int], part:int) -> bool:
    if part == 1:
        if len(eq) == 1:
            return True if val == eq[0] else False
        if val % eq[-1] != 0:
            return does_satisfy(val-eq[-1],eq[:-1], 1)
        else:
            return does_satisfy(val-eq[-1], eq[:-1], 1) or does_satisfy(val/eq[-1], eq[:-1], 1)
    elif part == 2:
        if len(eq) == 1:
            return True if val == eq[0] else False
        
        sat_plus = does_satisfy(val-eq[-1],eq[:-1], 2)
        if sat_plus: return True

        concat_pwr = 10 ** math.floor(math.log10(eq[-1])+1)
        concat_val = val%concat_pwr
        rest_val = (val-concat_val)/concat_pwr
        sat_concat = True if concat_val == eq[-1] and does_satisfy(rest_val, eq[:-1], 2) else False
        if sat_concat: return True

        if val % eq[-1] != 0:
            return False
        else:
            sat_mul = does_satisfy(val/eq[-1], eq[:-1], 2)
            return sat_mul

start = time.time()
puzzle = Day7("inputs/day7.txt")
puzzle.part1()
puzzle.part2()
end = time.time()
print(f'Elapsed time: {end - start}s')