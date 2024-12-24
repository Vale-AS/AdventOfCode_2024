import time
import heapq as hq
from copy import deepcopy

grafo = dict[int, list[tuple[int,int]]]
infinity = float('inf')

class Day20:
    def __init__(self, filename):
        with open(filename) as f:
            data = f.read().split('\n')
            self.track = []
            for line in data:
                self.track.append(list(line))
    
    def create_graph(self, g):
        for i in range(1, len(self.track)-1):
            for j in range(1, len(self.track[0])-1):
                if self.track[i][j] != '#':
                    id = i*len(self.track)+j
                    ns = [(i-1,j),(i+1,j),(i,j+1),(i,j-1)]
                    for n in ns:
                        k,l = n
                        if self.track[k][l] != '#':
                            n_id = k*len(self.track)+l
                            agregarArista(g, id, n_id, 1)
    
    def part1(self):
        g : grafo = {}
        self.create_graph(g)
        
        start = find_char(self.track, 'S')
        start_id = start[0] * len(self.track) + start[1]
        end = find_char(self.track, 'E')
        end_id = end[0] * len(self.track) + end[1]

        d = [None] * (len(self.track) ** 2)
        d = dijkstra(g, start_id, d)
        original_track_time = d[end_id]
        print(original_track_time)

        cheats_by_time_saved = {}
        cheats = find_cheat_places(self.track)
        print(f'there are {len(cheats)} possible cheat places')
        for c in cheats:
            print(f'cheat place {c}')
            i, j = c
            #self.track[i][j] = '.'

            #g : grafo = {}
            #self.create_graph(g)
            #d = [None] * (len(self.track) ** 2)
            new_cheat_id = i*len(self.track)+j
            ns = [(i-1,j),(i+1,j),(i,j+1),(i,j-1)]
            for n in ns:
                k,l = n
                if self.track[k][l] != '#':
                    n_id = k*len(self.track)+l
                    agregarArista(g, new_cheat_id, n_id, 1)
                    agregarArista(g,n_id, new_cheat_id, 1)


            d = [None] * (len(self.track) ** 2)
            d = dijkstra(g, start_id, d)
            track_time = d[end_id]
            try:
                cheats_by_time_saved[original_track_time - track_time].append(c)
            except KeyError:
                cheats_by_time_saved[original_track_time - track_time] = [c]
            #self.track[i][j] = '#'

            g.pop(new_cheat_id)
            
            ns = [(i-1,j),(i+1,j),(i,j+1),(i,j-1)]
            for n in ns:
                k,l = n
                if self.track[k][l] != '#':
                    n_id = k*len(self.track)+l
                    g[n_id].remove((new_cheat_id,1))

        cheats_count = 0
        for k in cheats_by_time_saved.keys():
            if k >= 100:
                cheats_count += len(cheats_by_time_saved[k])
        print(cheats_count)



def find_cheat_places(track) -> list[tuple[int,int]]:
    cheat_walls = []
    for i in range(1, len(track)-1):
        for j in range(1, len(track[0])-1):
            if track[i][j] == '#':
                if 1 < i < len(track)-2:
                    if track[i-1][j] != '#' and track[i+1][j] != '#':
                        cheat_walls.append((i,j))
                if 1 < j < len(track[0])-2:
                    if track[i][j-1] != '#' and track[i][j+1] != '#':
                        cheat_walls.append((i,j))
    return cheat_walls



def find_char(map, chr):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == chr:
                return (i,j)
    return (-1,-1)

def agregarArista(g: grafo, desde: int, hacia: int, peso: int):
    try:
        g[desde].append((hacia,peso))
    except KeyError:
        g[desde] = [(hacia,peso)]
    return g

def initialize_dij(g: grafo, source: int, d: list[int]):
    for k in g.keys():
        d[k] = infinity
    d[source] = 0
    return d

def relax(u: int, v: int, w: int, d: dict[int, int], Q):
    if d[v] > d[u] + w:
        dist = d[u] + w
        d[v] = d[u] + w
        hq.heappush(Q, (dist,v))

def dijkstra(g: grafo, source: int, d: list[int]):
    d = initialize_dij(g, source, d)

    Q = []
    for i in g.keys():
        Q.append((infinity,i))
    
    while Q:
        u = hq.heappop(Q)[1]
        for v in g[u]:
            relax(u, v[0], v[1], d, Q)
    
    return d

start = time.time()
puzzle = Day20("inputs/day20.txt")
puzzle.part1()
#puzzle.part2()
end = time.time()
print(f'Elapsed time: {end - start}s')