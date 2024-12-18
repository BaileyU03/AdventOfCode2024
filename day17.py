class Computer:
    def __init__(self, reg_a, reg_b, reg_c, program):
        self.reg_a = reg_a
        self.reg_b = reg_b
        self.reg_c = reg_c
        self.program = program
        self.pointer = 0
        self.output = ""

    def run(self):
        while self.pointer < len(self.program) - 1:
            opcode = self.program[self.pointer]
            operand = self.program[self.pointer + 1]
            self.compute(opcode, operand)
            self.pointer += 2
        self.output = self.output[1:]
        print(self.output)

    def compute(self, opcode, operand):
        if opcode == 0:
            self.adv_0(operand)
        if opcode == 1:
            self.bxl_1(operand)
        if opcode == 2:
            self.bst_2(operand)
        if opcode == 3:
            self.jnz_3(operand)
        if opcode == 4:
            self.bxc_4()
        if opcode == 5:
            self.out_5(operand)
        if opcode == 6:
            self.bdv_6(operand)
        if opcode == 7:
            self.cdv_7(operand)

    def get_combo(self, operand):
        if operand == 4:
            return self.reg_a
        if operand == 5:
            return self.reg_b
        if operand == 6:
            return self.reg_c
        return operand

    def adv_0(self, operand):
        self.reg_a = self.reg_a // (2 ** self.get_combo(operand))

    def bxl_1(self, operand):
        self.reg_b = self.reg_b ^ operand

    def bst_2(self, operand):
        self.reg_b = self.get_combo(operand) % 8

    def jnz_3(self, operand):
        if self.reg_a > 0:
            self.pointer = operand - 2

    def bxc_4(self):
        self.reg_b = self.reg_b ^ self.reg_c

    def out_5(self, operand):
        self.output += "," + str(self.get_combo(operand) % 8)

    def bdv_6(self, operand):
        self.reg_b = self.reg_a // (2 ** self.get_combo(operand))

    def cdv_7(self, operand):
        self.reg_c = self.reg_a // (2 ** self.get_combo(operand))


with open("files/day17.txt", "r") as f:
    reg_a = int(f.readline().split(": ")[1])
    reg_b = int(f.readline().split(": ")[1])
    reg_c = int(f.readline().split(": ")[1])
    f.readline()
    program = list(map(int, f.readline().split(": ")[1].split("\n")[0].split(",")))

computer = Computer(reg_a, reg_b, reg_c, program)
computer.run()
