import time
import heapq as hq

grafo = dict[int, list[tuple[int,int]]]
infinity = float('inf')

class Day18:
    def __init__(self, filename, size, p1_bytes):
        with open(filename) as f:
            self.all_bytes = f.read().split()
            self.p1_b = p1_bytes
            self.size = size
            self.memory = [['#' for _ in range(size+2)]]
            self.memory += [['#']+['.' for _ in range(size)]+['#'] for _ in range(size)]
            self.memory += [['#' for _ in range(size+2)]]

    def part1(self):
        g : grafo = {}
        self.fall_bytes()
        self.create_graph(g)

        d = [None] * (self.size ** 2)
        d = dijkstra(g, 0, d)
        min = d[self.size ** 2-1]
        print(min)
    
    def part2(self):
        for b in range(self.p1_b, len(self.all_bytes)):
            j, i = (int(e) for e in list(self.all_bytes[b].split(',')))
            self.memory[i+1][j+1] = '#'

            g : grafo = {}
            self.create_graph(g)

            d = [None] * (self.size ** 2)
            d = dijkstra(g, 0, d)
            path = d[self.size ** 2-1]
            if path == infinity:
                print((j,i))
                break


    def create_graph(self, g):
        for i in range(1,self.size+1):
            for j in range(1, self.size+1):
                if self.memory[i][j] == '.':
                    id = (i-1)*self.size+(j-1)
                    ns = [(i-1,j),(i+1,j),(i,j+1),(i,j-1)]
                    for n in ns:
                        k,l = n
                        if self.memory[k][l] == '.':
                            n_id = (k-1)*self.size+(l-1)
                            agregarArista(g, id, n_id, 1)
                            
    def fall_bytes(self):
        for o in range(self.p1_b):
            j, i = [int(e) for e in list(self.all_bytes[o].split(','))]
            self.memory[i+1][j+1] = '#'


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
puzzle = Day18("inputs/day18.txt", 71, 1024)
puzzle.part1()
puzzle.part2()
#puzzle.both_parts()
end = time.time()
print(f'Elapsed time: {end - start}s')