with open("input", "r") as file:
    tests = file.readlines()


def test_cases(cases):
    cubes_dict = {"red":0,
                  "green":0,
                  "blue":0}
    for case in cases:
        sub_cases = case.split(", ")
        for j in sub_cases:
            j = j.split(" ")

            if int(j[0]) > cubes_dict[j[1]]:
                cubes_dict[j[1]] = int(j[0])

    return cubes_dict

sum = 0
for id, test in enumerate(tests):
    cases = test[:-1].split(": ")[1].split("; ")
    cubes_dict = test_cases(cases)
    power = 1
    for i in cubes_dict.values():
        power *= i

    sum += power

print(sum)
