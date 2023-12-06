with open("input.txt", "r") as file:
    lines = file.readlines()

total_points = 0
for line in lines:
    points = 0
    line = line.split(": ")[1].strip().split(" | ")

    winning_numbers = line[0].replace("  ", " ").split(" ")
    lott_numbers = line[1].replace("  ", " ").split(" ")

    # winning_numbers = [int(i) for i in winning_numbers]
    # lott_numbers = [int(i) for i in lott_numbers]

    for num in lott_numbers:
        if num in winning_numbers:
            if points:
                points *= 2
            else:
                points = 1



    print(f"points - {points}")
    total_points += points

print(total_points)

