with open("input.txt", "r") as file:
    lines = file.readlines()

card_map = {}

for line in lines:
    points = 0
    id = int(line.split(": ")[0].split(" ")[-1])

    if (id) in card_map:
        card_map[id] += 1
    else:
        card_map[id] = 1

    line = line.split(": ")[1].strip().split(" | ")

    winning_numbers = line[0].replace("  ", " ").split(" ")
    lott_numbers = line[1].replace("  ", " ").split(" ")

    # winning_numbers = [int(i) for i in winning_numbers]
    # lott_numbers = [int(i) for i in lott_numbers]

    for num in lott_numbers:
        if num in winning_numbers:
            points += 1
    
    # points *= card_map[id]

    for i in range(1, points+1):
        if (id+i) in card_map:
            card_map[id+i] += card_map[id]
        else:
            card_map[id+i] = card_map[id]

    print(f"points - {points}")

total = 0
for i in card_map.values():
    total += i

print(total)
