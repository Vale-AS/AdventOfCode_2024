class Day2:

    def __init__(self, filename):
        with open(filename) as f:
            self.data = f.readlines()
            for i in range(len(self.data)):
                lvls = self.data[i].split(' ')
                for j in range(len(lvls)):
                    lvls[j] = int(lvls[j])
                self.data[i] = lvls

    def part1(self):
        safe_count = 0
        for report in self.data:
            if is_safe(report):
                safe_count += 1
        print(safe_count)
    
    def part2(self):
        safe_count = 0
        for report in self.data:
            if is_safe(report):
                safe_count += 1
            elif problem_dampener(report):
                safe_count += 1
        print(safe_count)

    def both_parts(self):
        part1_safe_count = 0
        part2_safe_count = 0
        for report in self.data:
            part1_safe_count += 1 if is_safe(report) else 0
            part2_safe_count += 1 if is_safe(report) or problem_dampener(report) else 0
        print(f'part 1 result is: {part1_safe_count} and part 2 result is: {part2_safe_count}')


def is_safe(report: list[int]) -> bool:
    '''if all_increasing(report):
        return diff_less_than_three(report)
    elif all_decreasing(report):
        return diff_less_than_three(report)
    else:
        return False'''
    
    '''if monotonic(report):
        return diff_less_than_three(report)
    else: 
        return False'''
    
    is_inc = True
    is_dec = True
    all_diff_less_than_three = True
    for i in range(len(report)-1):
        if report[i] <= report[i+1]:
            is_dec = False
        if report[i] >= report[i+1]:
            is_inc = False
        if abs(report[i]-report[i+1]) > 3:
            all_diff_less_than_three = False
    return (is_inc or is_dec) and all_diff_less_than_three

def monotonic(line: list[int]) -> bool:
    is_inc = True
    is_dec = True
    all_diff_less_than_three = True
    for i in range(len(line)-1):
        if line[i] <= line[i+1]:
            is_dec = False
        if line[i] >= line[i+1]:
            is_inc = False
        if abs(line[i]-line[i+1]) > 3:
            all_diff_less_than_three = False
    return (is_inc or is_dec) and all_diff_less_than_three
    
def all_decreasing(line: list[int]) -> bool:
    for i in range(len(line)-1):
        if line[i] <= line[i+1]:
            return False
    return True

def all_increasing(line: list[int]) -> bool:
    for i in range(len(line)-1):
        if line[i] >= line[i+1]:
            return False
    return True

def diff_less_than_three(line: list[int]) -> bool:
    for i in range(len(line)-1):
        if abs(line[i+1] - line[i]) > 3:
            return False
    return True

def problem_dampener(line: list[int]) -> bool:
    for i in range(len(line)):
        one_less_line = line[:i]+line[i+1:]
        if is_safe(one_less_line):
            return True
    return False

puzzle = Day2('inputs/day2.txt')
#puzzle.part1()
#puzzle.part2()
puzzle.both_parts()