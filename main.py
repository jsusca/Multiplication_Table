import re

running = True

print("\nWelcome to The Multiplication Table!")

while running:
    max_val = input("\nChoose your highest number: ")

    # Continues running if anything but int is input
    max_val = re.sub(r'[^\d]+', '', max_val)
    if max_val == "":
        continue

    max_val = int(max_val)

    # Determines max number of digits per integer in table
    max_length = len(str(max_val ** 2))

    # Columns
    for i in range(1, max_val + 1):
        # Rows
        for j in range(1, max_val + 1):
            print(str((j * i)).ljust(max_length, ' '), end=" "),
        print()
