with open("sample.txt", "r") as file:
    lines = file.readlines()

def get_diff_last(line:list):
    last_elements = [line[-1]]
    while len(set(line)) > 1 or line[0] != 0:
        for i in range(len(line) - 1):
            line[i] = line[i+1] - line[i]

        line.pop()
        last_elements.append(line[-1])
    
    return last_elements

sum = 0
for line in lines:
    last_elements = get_diff_last([int(i) for i in line.split()])

    for i in last_elements[::-1]:
        sum += i

    print(last_elements)


print(sum)
