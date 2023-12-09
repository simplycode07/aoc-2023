with open("input.txt", "r") as file:
    lines = file.readlines()

def get_diff_first(line):
    first_elements = [line[0]]
    while len(set(line)) > 1 or line[0] != 0:
        for i in range(len(line) - 1):
            line[i] = line[i+1] - line[i]
        
        line.pop()
        first_elements.append(line[0])
    
    return first_elements


total = 0
for line in lines:
    first_elements = get_diff_first([int(i) for i in line.split()])
    sum = 0
    for i in first_elements[::-1]:
        sum = i - sum
    print(sum)
    total += sum
print(total)
