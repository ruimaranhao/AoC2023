#!/usr/bin/python3

def solution1_adapted(input_lines):
    calories = []
    total = 0
    max_total = 0
    max_elf = 0

    for _, line in enumerate(input_lines):
        # If the line is empty, we have reached the end of an Elf's inventory
        if line.strip() == "":
            # Calculate the total Calories for the current Elf
            calories.append(total)
            # Check if this is the Elf with the most Calories
            if total > max_total:
                max_total = total
                max_elf += 1 
            total = 0
        else:
            # Add the Calories from the current item to the total
            total += int(line)

    # Print the Elf with the most Calories and their total Calories
    print("Elf %d is carrying the most Calories: %d" % (max_elf + 1, max_total))


def solution2_adapted(input_line):
    calories = []
    total = 0
    top_three = []
    elf_cnt = 1 #MY CHANGES

    for _, line in enumerate(input_lines):
        if line.strip() == "":
            calories.append(total)
            # If the new Elf has more Calories than the least of the top three Elves,
            # remove the least Elf and add the new Elf to the list
            if len(top_three) < 3:
                top_three += [(elf_cnt, total)]
            elif total > min(top_three, key = lambda t: t[1])[1]: #MY CHANGES
                top_three = [(elf_cnt, total)] + [x for x in top_three if x[1] != min([x[1] for x in top_three])]
            elf_cnt += 1
            total = 0
        else:
            total += int(line)

    # Calculate the total Calories carried by the top three Elves
    top_three_calories = sum([x[1] for x in top_three])

    # Print the top three Elves and their total Calories
    print("Top three Elves:")
    for elf, cals in top_three:
        print("Elf %d: %d Calories" % (elf, cals))
    print("Total Calories carried by top three Elves: %d" % top_three_calories)    


input_lines = ["1000", "2000", "3000",  "",  
               "4000",  "",  
               "5000",  "6000",  "",  
               "7000",  "8000",  "9000",  "",  
               "10000", ""]
print("Solution 1")
solution1_adapted(input_lines)
print("Solution 2")
solution2_adapted(input_lines)

print("===============================")
with open('puzzle.in') as f:
    input_lines = list(map(lambda x: x.strip(), f.readlines()))
print("Solution 1")
solution1_adapted(input_lines)
print("Solution 2")
solution2_adapted(input_lines)
