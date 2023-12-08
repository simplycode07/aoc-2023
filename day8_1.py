from itertools import cycle

with open("input.txt", "r") as file:
    directions, *instructions = file.read().strip().split("\n")
    directions = cycle(directions)

    del instructions[0]

inst_dict = {}

for instruction in instructions:
    choices = instruction.split("=")[1].strip()[1:-1]
    inst_dict[instruction.split("=")[0].strip()] = (choices.split(",")[0].strip(), choices.split(",")[1].strip())

loc = "AAA"
steps = 0
for dir in directions:
    if loc == "ZZZ":
        break
    
    steps += 1
    if dir == "L":
        loc = inst_dict[loc][0]

    else:
        loc = inst_dict[loc][1]


print(steps)
