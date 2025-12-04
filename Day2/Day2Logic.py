import regex

pattern1 = regex.compile(r"^([\d]{1,})\1$")
pattern2 = regex.compile(r"^([\d]{1,})\1{1,}$")


invalid_ids_p1 = []
invalid_ids_p2 = []

with open("Day2/Day2Input.txt", "r") as file:
    input_data = file.read()
    input_data = input_data.split(",")
    for ids in input_data:
        ends = ids.split("-")
        for i in range(int(ends[0]), int(ends[1]) + 1):
            if pattern1.match(str(i)):
                invalid_ids_p1.append(int(i))
            if pattern2.match(str(i)):
                invalid_ids_p2.append(int(i))

    print(f"Total sum of invalid IDs for part 1: {sum(invalid_ids_p1)}")
    print(f"Total sum of invalid IDs for part 2: {sum(invalid_ids_p2)}")