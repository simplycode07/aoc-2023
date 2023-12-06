with open("input.txt", "r") as file:
    seeds, *blocks = file.read().split("\n\n")

seeds = [int(i) for i in seeds.split(":")[1].split()]

for block in blocks:
    ranges_list = []
    for line in block.splitlines()[1:]:
        ranges_list.append([int(i) for i in line.split()])
    print(ranges_list)
    
    new = []
    for i in seeds:
        for dest_start, source_start, range_len in ranges_list:
            if i in range(source_start, source_start+range_len):
                diff_from_start = i - source_start + dest_start
                new.append(diff_from_start)
                break

        # if the seed is not in range 
        else:
            new.append(i)

        seeds = new

print(min(seeds))

