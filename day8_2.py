from math import lcm

with open("input.txt", "r") as file:
    directions, *instructions = file.read().strip().split("\n")
    del instructions[0]

inst_dict = {}
loc = []

for instruction in instructions:
    choices = instruction.split("=")[1].strip()[1:-1]
    inst_dict[instruction.split("=")[0].strip()] = (choices.split(",")[0].strip(), choices.split(",")[1].strip())
    
    last_char = instruction.split("=")[0].strip()
    if last_char[-1] == "A":
        loc.append(last_char)


def num_steps(node):
    count = 0
    while node[-1] != "Z":
        dir = directions[count % len(directions)]
        
        if dir == "L":
            node = inst_dict[node][0]

        else:
            node = inst_dict[node][1]
        count += 1

    return count

list_nums = [num_steps(n) for n in loc]

print(lcm(*list_nums))
