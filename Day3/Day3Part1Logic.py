maxBanks = []

with open("Day3/Day3Input.txt", "r") as input_text:
    banks = input_text.read().splitlines()
    for bank in banks:
        max = 0
        for index in range(len(bank)):
            for digit2 in bank[index+1:]:
                currnum = int(str(bank[index] + digit2))
                if (currnum > max):
                    max = currnum
        maxBanks.append(max)
    print(sum(maxBanks))