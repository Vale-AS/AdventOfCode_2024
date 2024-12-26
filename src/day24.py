import time

class Day24:
    def __init__(self, filename):
        with open(filename) as f:
            primary_inputs, gates = f.read().split('\n\n')
            primary_inputs = primary_inputs.split('\n')
            gates = gates.split('\n')
            self.inputs = {}
            for pi in primary_inputs:
                var, value = pi.split(': ')
                self.inputs[var] = int(value)
            self.gate_operations = []
            self.z_output_size = 0
            for g in gates:
                g = g.split(' ')
                g.remove('->')
                if g[-1].startswith('z'):
                    self.z_output_size += 1
                self.gate_operations.append(tuple(g))
        
    
    def part1(self):
        z_outputs = {}
        i = 0
        while len(z_outputs) != self.z_output_size:
            print(f'pasada {i}')
            for g in self.gate_operations:
                op1, oper, op2, output = g
                if op1 in self.inputs.keys() and op2 in self.inputs.keys():
                    op1, op2 = self.inputs[op1], self.inputs[op2]
                    res = apply_operation(op1, op2, oper)
                    if output.startswith('z'):
                        z_outputs[output] = res
                    else:
                        self.inputs[output] = res
            i += 1
        z_keys = list(z_outputs.keys())
        z_keys.sort(reverse=True)
        num = ''
        for z in z_keys:
            digit = z_outputs[z]
            num += str(digit)
        dec_output = int(num, base=2)
        print(dec_output)

def apply_operation(op1, op2, oper):
    if oper == 'AND':
        res = op1 and op2
    elif oper == 'OR':
        res = op1 or op2
    elif oper == 'XOR':
        res = op1 ^ op2
    return res

start = time.time()
puzzle = Day24("inputs/day24.txt")
puzzle.part1()
end = time.time()
print(f'Elapsed time: {end - start}s')