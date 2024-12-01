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
        p1_left = self.left_list
        p1_right = self.right_list
            
        p1_left.sort()
        p1_right.sort()

        distances = 0
        for i in range(len(p1_left)):
            distances += (abs(p1_left[i]-p1_right[i]))
        
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