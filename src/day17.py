import time

zigzag = [
    "<3      ",
    " <3     ",
    "  <3    ",
    "   <3   ",
    "    <3  ",
    "     <3 ",
    "      <3",
    "     <3 ",
    "    <3  ",
    "   <3   ",
    "  <3    ",
    " <3     ",
]

class computer:
    def __init__(self, A: int, B: int, C: int, program: list[int]):
        self.A = A
        self.B = B
        self.C = C
        self.prog = program

    def run(self):
        i = 0
        output = ''
        while i < len(self.prog):
            opcode = self.prog[i]
            operand = self.prog[i+1]
            i, output = self.solve(opcode, operand, i, output)
        return output[:-1]
    
    def find_A_reg(self):
        desired_output = ','.join([str(o) for o in self.prog])
        current_output = ''
        for n in range(1,10000000):
            print(f'\rN = {n}   {zigzag[n%(len(zigzag))]}')
            print ("\033[A\033[A")
            if n == 117440:
                pass
            i = 0
            current_output = ''
            self.A = n
            while i < len(self.prog):
                opcode = self.prog[i]
                operand = self.prog[i+1]
                i, current_output = self.solve(opcode, operand, i, current_output)
                if opcode == 5 and not desired_output.startswith(current_output[:-1]):
                    break
            if current_output[:-1] == desired_output:
                return n
        return -1


    def solve(self, opc: int, oper: int, ip: int, output: str):
        if opc == 0:
            num = self.A
            power = self.combo_op(oper)
            den = 2 ** power
            div = int(num/den)
            self.A = div
            ip += 2
        elif opc == 1:
            lhs = self.B
            rhs = oper
            xor = lhs^rhs
            self.B = xor
            ip += 2
        elif opc == 2:
            num = self.combo_op(oper)
            mod = num % 8
            self.B = mod
            ip += 2
        elif opc == 3:
            if self.A != 0:
                ip = oper
            else:
                ip += 2
        elif opc == 4:
            lhs = self.B
            rhs = self.C
            xor = lhs^rhs
            self.B = xor
            ip += 2
        elif opc == 5:
            num = self.combo_op(oper)
            mod = num % 8
            output += str(mod) +','
            ip += 2
        elif opc == 6:
            num = self.A
            power = self.combo_op(oper)
            den = 2 ** power
            div = int(num/den)
            self.B = div
            ip += 2
        elif opc == 7:
            num = self.A
            power = self.combo_op(oper)
            den = 2 ** power
            div = int(num/den)
            self.C = div
            ip += 2
        return ip, output
    
    def combo_op(self, op):
        if 0 <= op <= 3:
            return op
        elif op == 4:
            return self.A
        elif op == 5:
            return self.B
        elif op == 6:
            return self.C
        elif op == 7:
            raise ValueError('Invalid combo operator')


class Day17:
    def __init__(self, filename):
        with open(filename) as f:
            regs, program = f.read().split('\n\n')
            regs = regs.split('\n')
            A_val = int(regs[0][12:])
            B_val = int(regs[1][12:])
            C_val = int(regs[2][12:])
            program = program[9:]
            prog = [int(o) for o in program.split(',')]
            self.computer = computer(A_val, B_val, C_val, prog)

    def part1(self):
        output = self.computer.run()
        print(output)
    
    def part2(self):
        lowest_output_program = self.computer.find_A_reg()
        print(f'\n{lowest_output_program}')

start = time.time()
puzzle = Day17("inputs/day17.txt")
puzzle.part1()
puzzle.part2()
end = time.time()
print(f'Elapsed time: {end - start}s')