import time
from bisect import insort

class Day9:
    def __init__(self, filename):
        with open(filename) as f:
            dsk = list(f.readline())
            for i in range(len(dsk)):
                dsk[i] = int(dsk[i])
            self.disk = dsk

    def part1(self):
        full_disk, blank_space_idx = create_disk_and_blank_space(self.disk)
        i = 0
        max_id = full_disk[-1]
        while i < len(blank_space_idx):
            idx = blank_space_idx[i]
            j = find_next_block(full_disk, len(full_disk)-1, max_id)
            if idx > j:
                break
            swap(full_disk, idx, j)
            i += 1
        checksum = calc_chksm(full_disk)
        print(checksum)
    
    def part2(self):
        full_disk, blank_space_idx = create_disk_and_blank_space(self.disk)
        max_id = full_disk[-1]
        i = find_next_block(full_disk, len(full_disk)-1, max_id)
        while i >= 0:
            if i == 1:
                pass
            id = full_disk[i]
            file_size = full_disk.count(id)
            blank_space_idx, idx = find_free_space(blank_space_idx, file_size, i)
            if idx:
                for j in range(file_size):
                    full_disk[idx+j] = id
                    full_disk[i-j] = '.'
                    insort(blank_space_idx, i-j)
                i = find_next_block(full_disk, i-file_size, id)
            else:
                i = find_next_block(full_disk, i-file_size, id)
        checksum = calc_chksm(full_disk)
        print(checksum)

def create_disk_and_blank_space(dsk):
    full_disk = []
    blank_space_idx = []
    for i in range(len(dsk)):
            if i%2 == 0:
                id = int(i/2)
                for _ in range(dsk[i]):
                    full_disk.append(id)
            else:
                for _ in range(dsk[i]):
                    full_disk.append('.')
                    blank_space_idx.append(len(full_disk)-1)
    return full_disk, blank_space_idx

def find_next_block(dsk, idx, id):
    if id == 0:
        return -1
    for i in range(idx,-1,-1):
        if dsk[i] != '.':
            if dsk[i] > id:
                continue
            else:
                return i

def find_free_space(blank_space, size, to_i):
    i = 1
    idx = blank_space[0]
    count = 1
    if count == size:
        res = blank_space[i-size]
        blank_space = blank_space[:i-size]+blank_space[i:]
        return blank_space, res
    while i < len(blank_space):
        if blank_space[i] > to_i:
            break
        if blank_space[i] == idx + 1:
            count += 1
            idx += 1
            i += 1
        else:
            count = 1
            idx = blank_space[i]
            i += 1
        if count == size: 
            res = blank_space[i-size]
            blank_space = blank_space[:i-size]+blank_space[i:]
            return blank_space, res
    return blank_space, None



def swap(dsk, i, j):
    tmp = dsk[i]
    dsk[i] = dsk[j]
    dsk[j] = tmp

def calc_chksm(dsk):
    sum = 0
    for i in range(len(dsk)):
        if isinstance(dsk[i],int):
            sum += i*dsk[i]
    return sum

start = time.time()
puzzle = Day9("inputs/day9.txt")
#puzzle.part1()
puzzle.part2()
end = time.time()
print(f'Elapsed time: {end - start}s')