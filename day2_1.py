with open("input", "r") as file:
    tests = file.readlines()


def test_cases(cases):
    cubes_dict = {"red":12,
                  "green":13,
                  "blue":14}
    for case in cases:
        sub_cases = case.split(", ")
        for j in sub_cases:
            j = j.split(" ")

            if int(j[0]) > cubes_dict[j[1]]:
                return False

    return True

sum = 0
for id, test in enumerate(tests):
    cases = test[:-1].split(": ")[1].split("; ")
    if test_cases(cases):
        sum += id + 1


print(sum)
