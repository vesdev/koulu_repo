correct_smallest = 0
correct_biggest = 0
biggest = 0
smallest = -1

with open("../assets/KT_13_01_2025.txt", "r") as f:
    int_lines = [int(line) for line in f]

    correct_smallest = min(int_lines)
    correct_biggest = max(int_lines)

    for line in int_lines:
        if biggest < line:
            biggest = line
        elif smallest > line or smallest == -1:
            smallest = line

with open("../assets/KT_ratkaisu_15_01_2025.txt", "w") as f:
    f.write(f"pienin luku on {smallest} ja isoin luku on {biggest}.\n")

    if smallest == correct_smallest:
        f.write(f"{smallest} on oikein\n")
    else:
        f.write(f"{smallest} on vaara, oikea luku on {correct_smallest}.\n")

    if biggest == correct_biggest:
        f.write(f"{biggest} on oikein\n")
    else:
        f.write(f"{biggest} on vaara, oikea luku on {correct_biggest}.\n")
