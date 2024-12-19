import time
import heapq as hq

grafo = dict[str, list[tuple[str, int]]]
infinity = float('inf')

class Day16:
    def __init__(self, filename):
        with open(filename) as f:
            self.maze = []
            data = f.read().split('\n')
            for line in data:
                self.maze.append(line)
    
    def part1(self):
        g : grafo = {}
        self.create_graph(g)
        d = {}
        i, j = find_char(self.maze, 'S')
        start_id = str(i*len(self.maze)+j)+'E'
        d = dijkstra(g, start_id, d)
        i, j = find_char(self.maze, 'E')
        end_id1 = str(i*len(self.maze)+j)+'E'
        end_id2 = str(i*len(self.maze)+j)+'N'
        dist1 = d[end_id1]
        dist2 = d[end_id2]
        print(min(dist1, dist2))
        

    def create_graph(self, g):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
                if self.maze[i][j] != '#':
                    id = str(i*len(self.maze)+j)+'E'
                    ns = [(i,j+1), id[:-1]+'N', id[:-1]+'S']
                    for n in ns:
                        if isinstance(n, tuple):
                            k,l = n
                            if self.maze[k][l] != '#':
                                n_id = str(k*len(self.maze)+l)+'E'
                                agregarArista(g, id, n_id, 1)
                        else:
                            agregarArista(g, id, n, 1000)
                    id = str(i*len(self.maze)+j)+'S'
                    ns = [(i+1,j), id[:-1]+'E', id[:-1]+'W']
                    for n in ns:
                        if isinstance(n, tuple):
                            k,l = n
                            if self.maze[k][l] != '#':
                                n_id = str(k*len(self.maze)+l)+'S'
                                agregarArista(g, id, n_id, 1)
                        else:
                            agregarArista(g, id, n, 1000)
                    id = str(i*len(self.maze)+j)+'W'
                    ns = [(i,j-1), id[:-1]+'N', id[:-1]+'S']
                    for n in ns:
                        if isinstance(n, tuple):
                            k,l = n
                            if self.maze[k][l] != '#':
                                n_id = str(k*len(self.maze)+l)+'W'
                                agregarArista(g, id, n_id, 1)
                        else:
                            agregarArista(g, id, n, 1000)
                    id = str(i*len(self.maze)+j)+'N'
                    ns = [(i-1,j), id[:-1]+'W', id[:-1]+'E']
                    for n in ns:
                        if isinstance(n, tuple):
                            k,l = n
                            if self.maze[k][l] != '#':
                                n_id = str(k*len(self.maze)+l)+'N'
                                agregarArista(g, id, n_id, 1)
                        else:
                            agregarArista(g, id, n, 1000)


def find_char(map, chr):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == chr:
                return (i,j)
    return (-1,-1)

def agregarArista(g: grafo, desde: str, hacia: str, peso: int):
    try:
        g[desde].append((hacia,peso))
    except KeyError:
        g[desde] = [(hacia,peso)]
    return g

def initialize_dij(g: grafo, source: str, d: dict[str, int]):
    for k in g.keys():
        d[k] = infinity
    d[source] = 0
    return d

def relax(u: str, v: str, w: int, d: dict[str, int], Q):
    if d[v] > d[u] + w:
        dist = d[u] + w
        d[v] = d[u] + w
        hq.heappush(Q, (dist,v))
    return d

def dijkstra(g: grafo, source: str, d: dict[str, int]):
    d = initialize_dij(g, source, d)

    Q = []
    for i in g.keys():
        Q.append((infinity,i))
    
    count = 0
    while Q:
        u = hq.heappop(Q)[1]
        test_id = str(2*15+13)+'N'
        if u == test_id:
            pass
        for v in g[u]:
            d = relax(u, v[0], v[1], d, Q)
        count += 1
    
    return d

start = time.time()
puzzle = Day16("inputs/day16.txt")
puzzle.part1()
#puzzle.part2()
#puzzle.both_parts()
end = time.time()
print(f'Elapsed time: {end - start}s')