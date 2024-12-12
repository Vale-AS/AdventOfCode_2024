import time

class Day12:
    def __init__(self, filename):
        self.garden = []
        with open(filename) as f:
            data = f.read().split()
            self.garden.append('-'*(len(data[0])+2))
            for line in data:
                line = '-'+line+'-'
                self.garden.append(line)
            self.garden.append('-'*(len(data[0])+2))
    
    def part1(self):
        fencing_price = 0
        visited = set()
        for i in range(1,len(self.garden)-1):
            for j in range(1,len(self.garden[0])-1):
                if (i,j) in visited:
                    continue
                plant = self.garden[i][j]
                region = find_plant_region(plant, i, j, self.garden)
                visited = visited.union(region)
                area = len(region)
                perimeter = 0
                for p in region:
                    k, l = p
                    perimeter += single_plant_perimeter(plant, k, l, self.garden)
                fencing_price += area * perimeter
        print(fencing_price)
    
    def part2(self):
        fencing_price = 0
        visited = set()
        for i in range(1,len(self.garden)-1):
            for j in range(1,len(self.garden[0])-1):
                if (i,j) in visited:
                    continue
                plant = self.garden[i][j]
                region = find_plant_region(plant, i, j, self.garden)
                visited = visited.union(region)
                area = len(region)
                sides = calc_sides(region, plant, self.garden)
                fencing_price += area * sides
        print(fencing_price)

def calc_sides(reg, pl, garden):
    sides = 0
    for r in reg:
        i, j = r
        pl_ns = same_plant_neighbors(pl, i, j, garden)
        n = len(pl_ns)

        ll = 1 if (garden[i+1][j-1] != pl) else 0
        ul = 1 if (garden[i-1][j-1] != pl) else 0
        ur = 1 if (garden[i-1][j+1] != pl) else 0
        lr = 1 if (garden[i+1][j+1] != pl) else 0

        if n == 0:
            sides += 4
        elif n == 1:
            sides += 2
        elif n == 2:
            n1 = pl_ns[0]
            n2 = pl_ns[1]
            if n1[0] == n2[0] or n1[1] == n2[1]:
                sides += 0
            elif (n1 == (i-1,j) and n2 == (i,j+1)): # or (n2 == (i-1,j) and n1 == (i,j+1)): ?
                sides += (1+ur)
            elif (n1 == (i,j+1) and n2 == (i+1,j)):
                sides += (1+lr)
            elif (n1 == (i+1,j) and n2 == (i,j-1)):
                sides += (1+ll)
            elif (n2 == (i,j-1) and n1 == (i-1,j)):
                sides += (1+ul)
        elif n == 3:
            if (i-1, j) not in pl_ns:
                sides += ll + lr
            elif (i, j+1) not in pl_ns:
                sides += ll + ul
            elif (i+1, j) not in pl_ns:
                sides += ul + ur
            elif (i, j-1) not in pl_ns:
                sides += ur + lr
        elif n == 4:
            sides += (ll + lr + ul + ur)
    return sides


def same_plant_neighbors(pl, i, j, garden):
    res = []
    ns = [(i-1,j), (i,j+1), (i+1,j), (i,j-1)]
    for n in ns:
        k, l = n
        if garden[k][l] == pl:
            res.append(n)
    return res

def find_plant_region(pl, i, j, garden):
    reg = {(i,j)}
    working_list = {(i,j)}
    visited = []
    while working_list:
        p = working_list.pop()
        visited.append(p)
        y, x = p
        ns = [(y-1,x), (y+1,x), (y,x-1), (y,x+1)]
        for n in ns:
            k, l = n
            if garden[k][l] == pl:
                if n not in visited:
                    working_list.add(n)
                    reg.add(n)
    return reg

def single_plant_perimeter(pl, i, j, garden):
    single_p = 0
    ns = [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]
    for n in ns:
        k, l = n
        if garden[k][l] != pl:
            single_p += 1
    return single_p

start = time.time()
puzzle = Day12("inputs/day12.txt")
puzzle.part1()
puzzle.part2()
end = time.time()
print(f'Elapsed time: {end - start}s')