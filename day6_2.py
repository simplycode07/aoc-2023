with open("input.txt", "r") as file:
    data = file.readlines()

time = int(data[0].split(":")[1].strip().replace(" ", "" ))
distance = int(data[1].split(":")[1].strip().replace(" ", "" ))

num = 0
for speed in range(time):
    distance_covered = speed*(time-speed)
    if distance_covered > distance:
        num = speed
        break

print(time - 2*num + 1)
