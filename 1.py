# Day 1: Sonar Sweep

def depth_increase_count(depths):
    increased_count = 0

    depths_split = depths.split()

    for index, line in enumerate(depths_split):
        if index == 0:
            pass
        else:
            prev_line = depths_split[index - 1]
            if int(line) > int(prev_line):
                increased_count += 1
    return increased_count


with open("./inputs/day1part1.txt", "r+") as file:
    part1_input = file.read()
file.close()

part1_count = depth_increase_count(part1_input)
print(f"Part 1 increases: {part1_count}")


with open("./inputs/day1part2.txt", "r+") as file:
    part2_input = file.read()
file.close()

part2_count = depth_increase_count(part2_input)
print(f"Part 2 increases: {part2_count}")