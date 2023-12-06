
with open("input.txt", "r") as file:
    lines = file.readlines()

n = len(lines)
m = len(lines[0])

def is_symbol(i, j):
    if not (0<=i<n and 0<=j<m):
        return False

    return lines[i][j] != "." and not lines[i][j].isdigit()

def look_around(x1, x2, y1, y2):
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            if is_symbol(j,i):
                return True

    return False

ans = 0
for i, line in enumerate(lines):
    start = 0
    j = 0

    while j<m:
        start = j
        num = ""
        while j<m and line[j].isdigit():
            num += line[j]
            j += 1

        if num == "":
            j += 1
            continue

        num = int(num)

        if look_around(start-1, j, i-1, i+1):
            print(num)
            ans += num

print(f"answer: {ans}")
