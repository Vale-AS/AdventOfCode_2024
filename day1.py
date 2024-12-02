class Day1:

    def __init__(self, filename):
        self.left_list = []
        self.right_list = []

        with open(filename) as f:
            data = f.readlines()
            for line in data:
                l, r = line.split('   ')
                self.left_list.append(int(l))
                self.right_list.append(int(r))

    def part1(self):
        self.left_list.sort()
        self.right_list.sort()

        distances = 0
        for i in range(len(self.left_list)):
            distances += (abs(self.left_list[i]-self.right_list[i]))
        
        print(distances)
    
    def part2(self):
        similarity_score = 0
        for loc_id in self.left_list:
            loc_id_count = self.right_list.count(loc_id)
            similarity_score += loc_id * loc_id_count
        
        print(similarity_score)

puzzle = Day1('inputs/day1.txt')
puzzle.part1()
puzzle.part2()