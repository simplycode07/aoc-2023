with open("sample.txt", "r") as file:
    tests = file.readlines()

sum = 0
for test in tests:
    l = 0
    r = len(test) - 1

    while (l<=r):
        if not test[l].isdigit():
            l += 1
        elif not test[r].isdigit():
            r -= 1

        else:
            break

    sum += int(test[l]) * 10 + int(test[r])

print(sum)
