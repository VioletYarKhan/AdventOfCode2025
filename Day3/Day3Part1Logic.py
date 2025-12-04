maxBanks = []

TARGET_LEN = 12

with open("Day3/Day3Input.txt", "r") as input_text:
    banks = input_text.read().splitlines()
    for bank in banks:
        k = TARGET_LEN
        stack = []

        remaining = len(bank)

        for digit in bank:
            # While we can pop, and popping gives a bigger number
            while stack and digit > stack[-1] and len(stack) - 1 + remaining >= k:
                stack.pop()
            stack.append(digit)
            remaining -= 1

        # Keep only the first k digits
        best = stack[:k]

        maxBanks.append(int("".join(best)))

    print(sum(maxBanks))
