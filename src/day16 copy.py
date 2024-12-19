import time
from collections import  deque

'''class maze_pos:
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
'''
class Day16:
    def __init__(self, filename):
        with open(filename) as f:
            self.maze = []
            data = f.read().split('\n')
            for line in data:
                self.maze.append(line)
    
    def part1(self):
        start_maze = (find_char(self.maze, 'S'), 'E')
        dists = {start_maze : 0}
        visited = set()
        working_list = deque()
        working_list.append(start_maze)
        while working_list:
            mp = working_list.pop()
            if mp[1] == 'N' and mp[0][1] == 1:
                pass
            mp_fw = move_forward(mp)
            mp_fw_i, mp_fw_j = mp_fw[0]
            if self.maze[mp_fw_i][mp_fw_j] != '#':
                dists[mp_fw] = min(dists[mp] + 1, dists[mp_fw]) if mp_fw in dists.keys() else dists[mp] + 1
                if mp_fw not in visited:
                    working_list.append(mp_fw)
            n1, n2 = turn_possibilities(mp)
            dists[n1] = min(dists[mp] + 1000, dists[n1]) if n1 in dists.keys() else dists[mp] + 1000
            dists[n2] = min(dists[mp] + 1000, dists[n2]) if n2 in dists.keys() else dists[mp] + 1000
            if n1 not in visited and n1 not in working_list:
                working_list.append(n1)
            if n2 not in visited and n2 not in working_list:
                working_list.append(n2)
            visited.add(mp)
        end_pos = find_char(self.maze, 'E')
        end_maze1 = (end_pos, 'E')
        end_maze2 = (end_pos, 'N')
        if end_maze1 in dists.keys():
            print('llegué por el oeste')
            print(dists[end_maze1])
        elif end_maze2 in dists.keys():
            print('llegué por el sur')
            print(dists[end_maze2])
        else:
            print('algo salió mal')

def find_char(map, chr):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == chr:
                return (i,j)
    return (-1,-1)

def move_forward(maze_pos: tuple[tuple[int,int], str]):
    i,j = maze_pos[0]
    d = maze_pos[1]
    if d == 'N':
        return ((i-1,j),'N')
    if d == 'E':
        return ((i,j+1),'E')
    if d == 'S':
        return ((i+1,j),'S')
    if d == 'W':
        return ((i,j-1),'W')

def turn_possibilities(maze_pos: tuple[tuple[int,int], str]):
    pos = maze_pos[0]
    d = maze_pos[1]
    if d == 'N':
        return (pos,'W'), (pos,'E')
    if d == 'E':
        return (pos,'N'), (pos,'S')
    if d == 'S':
        return (pos,'E'), (pos,'W')
    if d == 'W':
        return (pos,'S'), (pos,'N')

start = time.time()
puzzle = Day16("inputs/day16test.txt")
puzzle.part1()
#puzzle.part2()
#puzzle.both_parts()
end = time.time()
print(f'Elapsed time: {end - start}s')