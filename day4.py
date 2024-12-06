import time
class Day4:
    def __init__(self, filename):
        with open(filename) as f:
            self.wordsearch = f.read().split('\n')
            self.height = len(self.wordsearch)
            self.width = len(self.wordsearch[0])

    def part1(self):
        count = 0
        for i in range(self.height):
            for j in range(self.width):
                if self.wordsearch[i][j] != 'X':
                    continue
                possible_words = set()
                if i >= 3: 
                    possible_words.add('upper')
                    if j >= 3:
                        possible_words.add('left')
                        possible_words.add('ul')
                    if j < self.width-3:
                        possible_words.add('right')
                        possible_words.add('ur')
                if i < self.height-3:
                    possible_words.add('lower')
                    if j >= 3:
                        possible_words.add('left')
                        possible_words.add('ll')
                    if j < self.width-3:
                        possible_words.add('right')
                        possible_words.add('lr')
                count += xmas_count(self.wordsearch, possible_words, i, j)
        print(count)
    
    def part2(self):
        count = 0
        for i in range(1,self.height-1):
            for j in range(1,self.width-1):
                if self.wordsearch[i][j] == 'A':
                    count += 1 if check_for_mas(self.wordsearch, i, j) else 0
        print(count)
    
    def both_parts(self):
        part1_count = 0
        part2_count = 0
        for i in range(self.height):
            for j in range(self.width):
                if self.wordsearch[i][j] == 'X':
                    possible_words = set()
                    if i >= 3: 
                        possible_words.add('upper')
                        if j >= 3:
                            possible_words.add('left')
                            possible_words.add('ul')
                        if j < self.width-3:
                            possible_words.add('right')
                            possible_words.add('ur')
                    if i < self.height-3:
                        possible_words.add('lower')
                        if j >= 3:
                            possible_words.add('left')
                            possible_words.add('ll')
                        if j < self.width-3:
                            possible_words.add('right')
                            possible_words.add('lr')
                    part1_count += xmas_count(self.wordsearch, possible_words, i, j)
                elif self.wordsearch[i][j] == 'A' and 1<i<self.height-1 and 1<j<self.width-1:
                    part2_count += 1 if check_for_mas(self.wordsearch, i, j) else 0
        print(f'part 1 result is: {part1_count} and part 2 result is: {part2_count}')



def xmas_count(square, search_places, i, j):
    word = ''
    count = 0
    if 'lr' in search_places:
        word = square[i][j]+square[i+1][j+1]+square[i+2][j+2]+square[i+3][j+3]
        count += 1 if word == 'XMAS' else 0
    if 'll' in search_places:
        word = square[i][j]+square[i+1][j-1]+square[i+2][j-2]+square[i+3][j-3]
        count += 1 if word == 'XMAS' else 0
    if 'ur' in search_places:
        word = square[i][j]+square[i-1][j+1]+square[i-2][j+2]+square[i-3][j+3]
        count += 1 if word == 'XMAS' else 0
    if 'ul' in search_places:
        word = square[i][j]+square[i-1][j-1]+square[i-2][j-2]+square[i-3][j-3]
        count += 1 if word == 'XMAS' else 0
    if 'upper' in search_places:
        word = square[i][j]+square[i-1][j]+square[i-2][j]+square[i-3][j]
        count += 1 if word == 'XMAS' else 0
    if 'lower' in search_places:
        word = square[i][j]+square[i+1][j]+square[i+2][j]+square[i+3][j]
        count += 1 if word == 'XMAS' else 0
    if 'left' in search_places:
        word =  square[i][j]+square[i][j-1]+square[i][j-2]+square[i][j-3]
        count += 1 if word == 'XMAS' else 0
    if 'right' in search_places:
        word = square[i][j]+square[i][j+1]+square[i][j+2]+square[i][j+3]
        count += 1 if word == 'XMAS' else 0
    return count

def check_for_mas(square, i, j):
    if square[i-1][j-1] == square[i+1][j-1] == 'M' and square[i-1][j+1] == square[i+1][j+1] == 'S':
        return True
    if square[i-1][j-1] == square[i+1][j-1] == 'S' and square[i-1][j+1] == square[i+1][j+1] == 'M':
        return True
    if square[i-1][j-1] == square[i-1][j+1] == 'M' and square[i+1][j-1] == square[i+1][j+1] == 'S':
        return True
    if square[i-1][j-1] == square[i-1][j+1] == 'S' and square[i+1][j-1] == square[i+1][j+1] == 'M':
        return True
    return False


start = time.time()
puzzle1 = Day4('inputs/day4.txt')
puzzle1.part1()
puzzle1.part2()
end = time.time()
print(f'Elapsed time: {end - start}s')

start = time.time()
puzzle2 = Day4('inputs/day4.txt')
puzzle2.both_parts()
end = time.time()
print(f'Elapsed time: {end - start}s')