with open("input.txt", "r") as file:
    data = file.readlines()

times = [int(i) for i in data[0].split(":")[1].strip().split()]
distances = [int(i) for i in data[1].split(":")[1].strip().split()]

ans = 1
for time, distance in zip(times, distances):
    num_ways = 0
    for speed in range(time):
        distance_covered = speed*(time-speed)
        if (distance_covered > distance):
            num_ways += 1
            print(f"for i = {speed} distance = {distance_covered} num_ways = {num_ways}")


    ans *= num_ways
    print("\n\n")


print(f"Answer is {ans}")
