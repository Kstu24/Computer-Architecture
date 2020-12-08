import sys

# a machine that simply executes an instruction

# op-code - they represent the instruction that is supposed to be executed
PRINT_HI = 1
HALT = 2
PRINT_NUM = 3
SAVE = 4 # save a value in a given register
PRINT_REGISTER = 5 # print value stored in register
ADD = 6 # takes in two registers, A and B and adds both values contained in the registers and stores it in reg A

memory = [
    PRINT_HI,
    SAVE, # SAVE 65 2 means save the value 65 into reg 2
    65,
    2,
    SAVE, # SAVE 20 3 means save the value 20 into reg 3
    20,
    3,
    ADD, # ADD 2 3 means add the values stored in reg 2 and reg 3 and store the result in reg 2
    2,
    3,
    PRINT_REGISTER, # PRINT_REGISTER 2 means print the value stored in register 2
    2,
    HALT,
]

program_counter = 0 # points to the current instruction we need to execute next
running = True
registers = [0] * 8

# keep looping while not halted
while running:
    command_to_execute = memory[program_counter]

    if command_to_execute == PRINT_HI:
        print("hi")
        program_counter += 1
    elif command_to_execute == PRINT_NUM:
        number_to_print = memory[program_counter + 1]
        print(f"{number_to_print}")
        program_counter += 2
    elif command_to_execute == HALT:
        running = False
        program_counter += 1
    elif command_to_execute == SAVE:
        value_to_save = memory[program_counter + 1]
        register_to_save_it_in = memory[program_counter + 2]
        registers[register_to_save_it_in] = value_to_save
        program_counter += 3
    elif command_to_execute == PRINT_REGISTER:
        register_to_print = memory[program_counter + 1]
        print(f"{registers[register_to_print]}")
        program_counter += 2
    elif command_to_execute == ADD:
        register_a = memory[program_counter + 1]
        register_b = memory[program_counter + 2]
        sum_of_registers = registers[register_a] + registers[register_b]
        registers[register_a] = sum_of_registers
        program_counter += 3
    else:
        print(f"Unknown instruction {command_to_execute}")
        sys.exit(1)

# Day 2
a = 0b1001
b = 0b0110

c = a & b #0b0000
d = a | b #0b1111
e = a ^ b #0b1111
print(format(e, '04b'))

# Meanings of the bits in the first byte of each instruction: `AABCDDDD`

# * `AA` Number of operands for this opcode, 0-2

INSTRUCTION = 0b10000010 # >> 6 --> 0b100001 & 0b001100 --> 0b10
PC = 0
number_of_times_to_increment_pc =  ((INSTRUCTION >> 6) & 0b11) + 1
PC += number_of_times_to_increment_pc

try:
    with open(sys.argv[1]) as my_file:
        for line in my_file:
            comment_split = line.split("#")
            maybe_binary_number = comment_split[0]

            try:
                x = int(maybe_binary_number, 2)
                print("{:08b}: {:d}".format(x, x))
            except:
                print(f"failed to cast {maybe_binary_number} to an int")
                continue
except FileNotFoundError:
    print("file not found...")
