import re

class Day3:

    def __init__(self, filename):
        with open(filename) as f:
            self.program = f.readlines()
        
    def part1(self):
        line = self.program[0]
        sum_of_mul = 0
        i = 0
        while i < len(line):
            if line[i] != 'm':
                i += 1
            else:
                close_p_index = line.find(')', i)
                is_mul, res = check_if_mul(line[i:close_p_index+1])
                if is_mul:
                    sum_of_mul += res
                    i = close_p_index+1
                else:
                    i += 1
        print(sum_of_mul)
    
    def part2(self):
        line = self.program[0]
        sum_of_mul = 0
        i = 0
        mul_enabled = True
        while i < len(line):
            char = line[i]
            if i == 100:
                pass
            mul_enabled = switch_mul(mul_enabled, line[i:i+7])
            if line[i] != 'm':
                i += 1
            elif not mul_enabled:
                i += 1
            else:
                close_p_index = line.find(')', i)
                is_mul, res = check_if_mul(line[i:close_p_index+1])
                if is_mul:
                    sum_of_mul += res
                    i = close_p_index+1
                else:
                    i += 1
        print(sum_of_mul)
            

def switch_mul(switch, line):
    disable = re.fullmatch('don\'t\(\)',line) is not None
    switch = False if disable else switch
    enable = re.fullmatch('do\(\)', line[:4]) is not None
    switch = True if enable else switch
    return switch
    
def check_if_mul(line):
    is_mul = re.fullmatch('mul\([1-9][0-9]{0,2},[1-9][0-9]{0,2}\)',line) is not None
    res = None
    if is_mul:
        nums = line[4:-1].split(',')
        res = int(nums[0]) * int(nums[1])
    return is_mul, res

puzzle = Day3('inputs/day3.txt')
puzzle.part1()
puzzle.part2()