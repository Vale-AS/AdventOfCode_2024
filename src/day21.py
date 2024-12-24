import time

class Day21:
    def __init__(self, filename):
        with open(filename) as f:
            self.codes = f.read().split()
    
    def part1(self):
        complexity = 0
        num_pad = {7: (0,0), 8: (0,1), 9: (0,2),
                   4: (1,0), 5: (1,1), 6: (1,2),
                   1: (2,0), 2: (2,1), 3: (2,2),
                             0: (3,1), 'A': (3,2)}
        key_pad = {            '^': (0,1), 'A': (0,2),
                   '<': (1,0), 'v': (1,1), '>': (1,2)}
        for code in self.codes:
            key_presses = ''
            past_c = 'A'
            for c in code:
                if c.isnumeric():
                    c = int(c)
                    key_presses += numpad_path(num_pad, past_c, c)
                    past_c = c
                else:
                    key_presses += numpad_path(num_pad, past_c, c)
                    past_c = c
            for _ in range(2):
                temp_key_p = ''
                past_k = 'A'
                for k in key_presses:
                    temp_key_p += keypad_path(key_pad, past_k, k)
                    past_k = k
                key_presses = temp_key_p
            num_part = int(code[:-1])
            kp_len = len(key_presses)
            complexity += num_part * kp_len
        print(complexity)

def numpad_path(numpad, from_key, to_key):
    i,j = numpad[from_key]
    k,l = numpad[to_key]

    res = ''

    if i==k and j==l:
        #res += 'A'
        pass
    elif i==k:
        d_abs = abs(l-j)
        for _ in range(d_abs):
            res += '>' if j<l else '<'
    elif j==l:
        d_abs = abs(k-i)
        for _ in range(d_abs):
            res += 'v' if i<k else '^'
    else:
        if i<k:
            vd = k-i
            hd_abs = abs(l-j)
            for _ in range(hd_abs):
                res += '>' if j<l else '<'
            for _ in range(vd):
                res += 'v'
        elif i>k:
            vd = i-k
            hd_abs = abs(l-j)
            for _ in range(vd):
                res += '^'
            for _ in range(hd_abs):
                res += '>' if j<l else '<'
            
    res += 'A'
    return res

def keypad_path(keypad, from_key, to_key):
    i,j = keypad[from_key]
    k,l = keypad[to_key]

    res = ''

    if i==k and j==l:
        #res += 'A'
        pass
    elif i==k:
        d_abs = abs(l-j)
        for _ in range(d_abs):
            res += '>' if j<l else '<'
    elif j==l:
        d_abs = abs(k-i)
        for _ in range(d_abs):
            res += 'v' if i<k else '^'
    else:
        if i<k:
            vd = k-i
            hd_abs = abs(l-j)
            for _ in range(vd):
                res += 'v'
            for _ in range(hd_abs):
                res += '>' if j<l else '<'
        elif i>k:
            vd = i-k
            hd_abs = abs(l-j)
            for _ in range(hd_abs):
                res += '>' if j<l else '<'
            for _ in range(vd):
                res += '^'
            
            
    res += 'A'
    return res

start = time.time()
puzzle = Day21("inputs/day21test.txt")
puzzle.part1()
end = time.time()
print(f'Elapsed time: {end - start}s')
'''
num_pad = {7: (0,0), 8: (0,1), 9: (0,2),
           4: (1,0), 5: (1,1), 6: (1,2),
           1: (2,0), 2: (2,1), 3: (2,2),
                     0: (3,1), 'A': (3,2)}

key_pad = {            '^': (0,1), 'A': (0,2),
           '<': (1,0), 'v': (1,1), '>': (1,2)}

#print(numpad_path(num_pad,'A',4))
test_code = '029A'
print(test_code)
past_c = 'A'
key_presses = ''
for c in test_code:
    if c.isnumeric():
        c = int(c)
        key_presses += numpad_path(num_pad, past_c, c)
        past_c = c
    else:
        key_presses += numpad_path(num_pad, past_c, c)
print(key_presses)
past_k = 'A'
key_presses2 = ''
for k in key_presses:
    key_presses2 += keypad_path(key_pad, past_k, k)
    past_k = k
print(key_presses2)
past_k = 'A'
key_presses3 = ''
for k in key_presses2:
    key_presses3 += keypad_path(key_pad, past_k, k)
    past_k = k
print(key_presses3)'''