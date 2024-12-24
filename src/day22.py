import time

class Day22:
    def __init__(self, filename):
        with open(filename) as f:
            data = f.read().split()
            self.sec_nums = [int(n) for n in data]
    
    def part1(self):
        final_sec_num_sum = 0
        for n in self.sec_nums:
            sec_num = n
            for _ in range(2000):
                sec_num = evolve_sec_num(sec_num)
            final_sec_num_sum += sec_num
        print(final_sec_num_sum)
    
    def part2(self):
        total_bananas = 0
        change_seq_apps = {}
        price_seqs = []
        for n in self.sec_nums:
            sec_num_seq = [n % 10]
            changes = [0]
            sec_num = n
            for _ in range(2000):
                sec_num = evolve_sec_num(sec_num)
                mod_sec_num = sec_num % 10
                sec_num_seq.append(mod_sec_num)
                changes.append(mod_sec_num - sec_num_seq[-2])
            price_seqs.append(sec_num_seq)
            max_val = max(sec_num_seq[4:])
            max_val_idx = sec_num_seq[4:].index(max_val)+4
            change_seq = tuple(changes[max_val_idx-4+1:max_val_idx+1])
            try:
                change_seq_apps[change_seq] += 1
            except KeyError:
                change_seq_apps[change_seq] = 1
        change_seq_most_app = max(change_seq_apps, key= lambda k : change_seq_apps[k])
        for seq in price_seqs:
            for idx in range(len(seq) - len(change_seq_most_app)):
                if seq[idx: idx + len(change_seq_most_app)] == change_seq_most_app:
                    sell_idx = idx +len(change_seq_most_app)
                    total_bananas += seq[sell_idx]
                    break
        print(total_bananas)


def evolve_sec_num(sn):
    mul_64 = sn * 64
    mix = mul_64 ^ sn
    prune = mix % 16777216

    div_32 = int(prune/32)
    mix = div_32 ^ prune
    prune = mix % 16777216

    mul_2048 = prune * 2048
    mix = mul_2048 ^ prune
    prune = mix % 16777216

    return prune


#print(evolve_sec_num(123))
start = time.time()
puzzle = Day22("inputs/day22test2.txt")
#puzzle.part1()
puzzle.part2()
end = time.time()
print(f'Elapsed time: {end - start}s')