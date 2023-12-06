with open("input.txt", "r") as file:
    tests = file.readlines()

sum = 0
num_dict = {"nine":"n9e",
            "eight":"e8t",
            "seven":"s7n",
            "six":"s6x",
            "five":"f5e",
            "four":"f4ur",
            "three":"t3e",
            "two":"t2o",
            "one":"o1n",
            "zero":"z0o"}

for test in tests:
    for word_num, num in num_dict.items():
        test = test.replace(word_num, num)
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
