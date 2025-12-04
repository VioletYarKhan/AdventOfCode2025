
dial = []

for i in range(100):
    dial.append(i)

index = 50
count = 0

with open("Day1/Day1Input.txt", "r") as file:
    input_data = file.read().splitlines()
    for line in input_data:
        dir = line[0]
        amount = int(line[1:])
        print("Current dial position:", dial[index])
        print("Direction:", dir, "Amount:", amount)
        if dir == "L":
            nextpos = index - amount
            print(nextpos)
            index = nextpos % len(dial)
        elif dir == "R":
            nextpos = index + amount
            print(nextpos)
            index = nextpos % len(dial)
        if (index == 0):
            count += 1

    print("Final dial position:", dial[index])
    print("Number of times dial landed on 0:", count)