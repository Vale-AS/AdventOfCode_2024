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
        files, blanks = make_files_blanks(self.disk)
        max_id = max(files.keys())
        for i in range(max_id, -1, -1):
            blocks = files[i]
            file_size = len(blocks)
            for j in range(1, file_size + 1):
                free_space_to_use = blanks.pop(0)
                space_to_free = files[i][-j]
                if free_space_to_use < space_to_free:
                    files[i][-j] = free_space_to_use
                    insort(blanks, space_to_free)
                else:
                    blanks.insert(0, free_space_to_use)
                    break
        checksum = calc_checksum(files)
        print(checksum)

    def part2(self):
        files, blanks = make_files_blanks(self.disk)
        max_id = max(files.keys())
        for i in range(max_id, -1, -1):
            blocks = files[i]
            file_size = len(blocks)
            free_blocks = find_free_of_size(blanks, file_size)
            if free_blocks:
                if free_blocks[-1] < blocks[0]:
                    for e in free_blocks:
                        blanks.remove(e)
                    for e in blocks:
                        insort(blanks, e)
                    files[i] = free_blocks
                else:
                    continue
        checksum = calc_checksum(files)
        print(checksum)
                    


def make_files_blanks(dsk: list[int]) -> tuple[dict[int, list[int]], list[int]]:
    files = {}
    blanks = []
    for i in range(len(dsk)):
        if i == 0:
            files[0] = list(range(0, dsk[0]))
        elif i%2 == 0:
            start = max(blanks[-1] + 1, files[int((i-2)/2)][-1] + 1)
            files[int(i/2)] = list(range(start, start + dsk[i]))
        else:
            start = files[int((i-1)/2)][-1] + 1
            blanks += list(range(start, start + dsk[i]))
    return files, blanks

def find_free_of_size(blanks: list[int], size: int) -> list[int]:
    free_bs = [blanks[0]]
    if len(free_bs) == size:
        return free_bs
    for i in range(1,len(blanks)):
        if free_bs:
            if blanks[i] == free_bs[-1]+1:
                free_bs.append(blanks[i])
                if len(free_bs) == size:
                    return free_bs
            else:
                free_bs = [blanks[i]]
    return []

def calc_checksum(d: dict) -> int:
    chksum = 0
    for k in d.keys():
        idxs = d[k]
        for i in idxs:
            chksum += k*i
    return chksum


start = time.time()
puzzle = Day9("inputs/day9.txt")
puzzle.part1()
puzzle.part2()
end = time.time()
print(f'Elapsed time: {end - start}s')