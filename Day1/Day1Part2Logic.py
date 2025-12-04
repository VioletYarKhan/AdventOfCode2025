import time
dial = []

for i in range(100):
    dial.append(i)

index = 50
count = 0

starttime = time.time()

print("Current dial position:", dial[index])

with open("Day1/Day1Input.txt", "r") as file:
    input_data = file.read().splitlines()
    for line in input_data:
        dir = line[0]
        amount = int(line[1:])
        print("Instruction:", dir+str(amount))
        if dir == "L":
            for step in range(amount):
                index = index - 1
                if (index == -1):
                    index = 99
                if (index == 0):
                    count += 1
        elif dir == "R":
            for step in range(amount):
                index = index + 1
                if (index == 100):
                    index = 0
                if (index == 0):
                    count += 1

        print("Current dial position:", dial[index])
        print("Times Passed 0 so far:", count)

            

    print("Final dial position:", dial[index])
    print("Number of times dial passed 0:", count)

    print("Execution Time (seconds):", time.time() - starttime)