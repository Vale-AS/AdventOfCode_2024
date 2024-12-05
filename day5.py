import numpy as np

class Day5:
    def __init__(self, filename):
        with open(filename) as f:
            data = f.read()
            split = data.split('\n\n')
            self.rules = split[0].split('\n')
            self.updates = split[1].split('\n')
            for i in range(len(self.updates)):
                upd = self.updates[i].split(',')
                upd = [int(e) for e in upd]
                self.updates[i] = upd
            for i in range(len(self.rules)):
                rl = self.rules[i].split('|')
                rl = (int(rl[0]),int(rl[1]))
                self.rules[i] = rl
    
    def part1(self):
        middle_page_sum = 0
        for upd in self.updates:
            correct = True
            for i in range(len(upd)-1):
                if not check_for_rules(upd, i, self.rules):
                    correct = False
            middle_page_sum += upd[int(np.floor(len(upd)/2))] if correct else 0
        print(middle_page_sum)

    def part2(self):
        middle_page_sum = 0
        for upd in self.updates:
            correct = True
            for i in range(len(upd)-1):
                if not check_for_rules(upd, i, self.rules):
                    correct = False
            if not correct:
                middle_page_sum += correct_ordering(upd, self.rules)
        print(middle_page_sum)
    
    def both_parts(self):
        correct_middle_page_sum = 0
        incorrect_middle_page_sum = 0
        for upd in self.updates:
            correct = True
            for i in range(len(upd)-1):
                if not check_for_rules(upd, i, self.rules):
                    correct = False
            if correct:
                correct_middle_page_sum += upd[int(np.floor(len(upd)/2))]
            else:
                incorrect_middle_page_sum += correct_ordering(upd, self.rules)
        print(f'part 1 result is: {correct_middle_page_sum} and part 2 result is: {incorrect_middle_page_sum}')

        

def check_for_rules(upd, i, rules):
    j = 0
    while j < len(upd):
        if j < i:
            if (upd[j],upd[i]) not in rules:
                return False
            j += 1
        elif j > i:
            if (upd[i],upd[j]) not in rules:
                return False
            j += 1
        else:
            j += 1
    return True
             
def correct_ordering(upd, rules):
    length = len(upd)
    order = []
    for i in range(length):
        ord_count = 0
        num = upd[i]
        j = 0
        while j < length:
            if j!=i:
                if (upd[i],upd[j]) in rules:
                    ord_count += 1
            j += 1
        order.append((num,ord_count))
    order.sort(key=lambda tup: tup[1])
    correct_update = [t[0] for t in order]
    return correct_update[int(np.floor(len(correct_update)/2))]
    

puzzle = Day5('inputs/day5.txt')
#puzzle.part1()
#puzzle.part2()
puzzle.both_parts()