def intersect(seeds):
    for seed in seeds:
        pass
    return [(0,0)]

with open("sample.txt", "r") as file:
    seeds, *blocks = file.read().split("\n\n")

seeds = [int(i) for i in seeds.split(":")[1].split()]
grouped_seeds = []
for i in range(0, len(seeds), 2):
    grouped_seeds += [[seeds[i], seeds[i+1]]]

print(grouped_seeds)

intersection = intersect(grouped_seeds)

for block in blocks:
    ranges_list = []
    for line in block.splitlines()[1:]:
        ranges_list.append([int(i) for i in line.split()])
    
    new = []
    for seeds in intersection:
        for i in range(seeds[0], seeds[0]+seeds[1]):
            for dest_start, source_start, range_len in ranges_list:
                if i in range(source_start, source_start+range_len):
                    diff_from_start = i - source_start + dest_start
                    new.append(diff_from_start)
                    # print(i)
                    break

            # if the seed is not in range 
            else:
                new.append(i)

        seeds = new

# print(min(seeds))
