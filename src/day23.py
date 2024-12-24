import time
from itertools import combinations

class Day23:
    def __init__(self, filename):
        self.lans = {}
        with open(filename) as f:
            data = f.read().split('\n')
            for connection in data:
                pc1, pc2 = connection.split('-')
                try:
                    self.lans[pc1].add(pc2)
                except KeyError:
                    self.lans[pc1] = {pc2}
                try:
                    self.lans[pc2].add(pc1)
                except KeyError:
                    self.lans[pc2] = {pc1}
            self.all_pcs = set()
            for c in data:
                pc1, pc2 = c.split('-')
                self.all_pcs.add(pc1)
                self.all_pcs.add(pc2)
    
    def part1(self):
        three_pc_lans = find_n_lans(self.lans, 3)
        three_lans_t = find_t_lans(three_pc_lans)
        print(len(three_lans_t))
    
    def part2(self):
        for n in range(14, 3, -1):
            big_lan = find_n_lans(self.lans, n)
            if len(big_lan) == 1:
                thee_lan_party = big_lan[0]
                thee_sorted_lan = sorted(thee_lan_party)
        print(','.join(thee_sorted_lan))

    def both_parts_maybe(self):
        three_pc_lans = find_n_lans(self.lans, 3)
        three_lans_t = find_t_lans(three_pc_lans)
        print(len(three_lans_t))

        big_cliques = three_pc_lans
        new_big_cliques = []
        i = 4
        while big_cliques:
            print(f'building size {i} cliques')
            for pc_lan in big_cliques:
                for pc in self.lans.keys():
                    if pc not in pc_lan:
                        if is_new_clique(pc, pc_lan, self.lans):
                            new_big_cliques.append(set([pc]+list(pc_lan)))
            if not new_big_cliques:
                break
            big_cliques = new_big_cliques
            new_big_cliques = []
            i += 1
        thee_lan_party = list(big_cliques[0])
        thee_sorted_lan = sorted(thee_lan_party)
        print(','.join(thee_sorted_lan))


def is_new_clique(pc, clique, lanlist):
    for c in clique:
        if pc not in lanlist[c]:
            return False
    return True


def find_n_lans(lan_list: dict[str, tuple], n: int):
    n_pc_lans = []
    for k in lan_list.keys():
        combs = combinations(lan_list[k],n-1)
        for p in combs:
            all_connected = True
            p_list = list(p)
            for c in p_list:
                all_connected &= connected_to_all(c, p_list, lan_list)
            if all_connected:
                add_lan(n_pc_lans, tuple([k]+p_list))
    return n_pc_lans


def add_lan(lanlist, lan):
    set_lan = set(lan)
    for l in lanlist:
        if set(l) == set_lan:
            return lanlist
    lanlist.append(lan)
    return lanlist

def find_t_lans(lanlist):
    t_lans = []
    for lan in lanlist:
        pc1, pc2, pc3 = lan
        if pc1.startswith('t') or pc2.startswith('t') or pc3.startswith('t'):
            t_lans.append(lan)
    return t_lans

def connected_to_all(c, p_list, lan_list):
    c_idx = p_list.index(c)
    p_list_no_c = p_list[:c_idx]+p_list[c_idx+1:]
    for p in p_list_no_c:
        if c not in lan_list[p]:
            return False
    return True

start = time.time()
puzzle = Day23("inputs/day23.txt")
#puzzle.part1()
#puzzle.part2()
puzzle.both_parts_maybe()
end = time.time()
print(f'Elapsed time: {end - start}s')