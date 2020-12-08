#!/usr/bin/env python3

class Instruction:
    def __init__(self, input):
        parsed = input.strip().split(" ")
        self.type = parsed[0]
        self.number = int(parsed[1])
        self.done = False
    
    def __repr__(self):
        return self.type + ": " + str(self.number)

instructions = []
with open('input.txt') as file:
    for command in file.readlines():
        inst = Instruction(command)
        instructions.append(inst)

acc = 0
instruction_number = 0

instruction = instructions[instruction_number]
while instruction.done is False:
    if instruction.type == "nop":
        instruction_number += 1
    elif instruction.type == "acc":
        acc += instruction.number
        instruction_number += 1
    elif instruction.type == "jmp":
        instruction_number += instruction.number
    else:
        raise Exception()
    
    instruction.done = True
    instruction = instructions[instruction_number]

print(acc)
