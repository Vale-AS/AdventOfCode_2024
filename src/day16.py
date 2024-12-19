import time
from collections import  deque

class maze_pos:
    def __init__(self, pos: tuple[int, int], dir: str):
        self.pos = pos
        self.dir = dir

    def turn_possibilities(self):
        if self.dir == 'N':
            return (maze_pos(self.pos,'W'), maze_pos(self.pos,'E'))
        if self.dir == 'E':
            return (maze_pos(self.pos,'N'), maze_pos(self.pos,'S'))
        if self.dir == 'S':
            return (maze_pos(self.pos,'E'), maze_pos(self.pos,'W'))
        if self.dir == 'W':
            return (maze_pos(self.pos,'S'), maze_pos(self.pos,'N'))
    
    def move_forward(self):
        i,j = self.pos
        if self.dir == 'N':
            return maze_pos((i-1,j),'N')
        if self.dir == 'E':
            return maze_pos((i,j+1),'E')
        if self.dir == 'S':
            return maze_pos((i+1,j),'S')
        if self.dir == 'W':
            return maze_pos((i,j-1),'W')

class Day16:
    def __init__(self, filename):
        with open(filename) as f:
            self.maze = []
            data = f.read().split('\n')
            for line in data:
                self.maze.append(line)
    
    def part1(self):
        start_pos = find_char(self.maze, 'S')
        start_maze = maze_pos(start_pos, 'E')
        dists = {start_maze : 0}
        visited = {start_maze}
        working_list = deque()
        working_list.append(start_maze)
        while working_list:
            mp : maze_pos = working_list.pop()
            mp_fw = mp.move_forward()
            mp_fw_i, mp_fw_j = mp_fw.pos
            if self.maze[mp_fw_i][mp_fw_j] != '#':
                dists[mp_fw] = min(dists[mp] + 1, dists[mp_fw]) if mp_fw in dists.keys() else dists[mp] + 1
                if mp_fw not in visited:
                    working_list.append(mp_fw)
            n1, n2 = mp.turn_possibilities()
            dists[n1] = min(dists[mp] + 1000, dists[n1]) if n1 in dists.keys() else dists[mp] + 1000
            dists[n2] = min(dists[mp] + 1000, dists[n2]) if n2 in dists.keys() else dists[mp] + 1000
            if n1 not in visited:
                working_list.append(n1)
            if n2 not in visited:
                working_list.append(n2)
        end_pos = find_char(self.maze, 'E')
        end_maze1 = maze_pos(end_pos, 'E')
        end_maze2 = maze_pos(end_pos, 'N')
        if end_maze1 in dists.keys():
            print(dists[end_maze1])
        elif end_maze2 in dists.keys():
            print(dists[end_maze2])
        else:
            print('algo salió mal')




def find_char(map, chr):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == chr:
                return (i,j)
    return (-1,-1)

start = time.time()
puzzle = Day16("inputs/day16test.txt")
puzzle.part1()
#puzzle.part2()
#puzzle.both_parts()
end = time.time()
print(f'Elapsed time: {end - start}s')