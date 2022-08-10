# Day 1: Sonar Sweep

# function for part 1
#   counts the number of depth increases from one line to the next
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


# function for part 2
#   counts the number of depth increases using a 3 depth sliding window
def depth_sliding_window_count(depths):
    increased_count = 0

    depths_split = depths.split()

    for index, line in enumerate(depths_split):
        if index <= 2:
            pass
        else:
            prev_window = int(depths_split[index - 1]) + int(depths_split[index - 2]) + int(depths_split[index - 3])
            cur_window = int(depths_split[index]) + int(depths_split[index - 1]) + int(depths_split[index - 2])
            if cur_window > prev_window:
                increased_count += 1
    return increased_count


# open test and data file
with open("inputs/day1test.txt", "r+") as file:
    part1_input = file.read()
file.close()

with open("inputs/day1data.txt", "r+") as file:
    part2_input = file.read()
file.close()

# call each function with test and data for part 1 and part 2
test_count = depth_increase_count(part1_input)
print(f"Part 1 test input increases: {test_count}")

data_count = depth_increase_count(part2_input)
print(f"Part 1 data input increases: {data_count}")

test_window = depth_sliding_window_count(part1_input)
print(f"Part 2 test input sliding window increases: {test_window}")

data_window = depth_sliding_window_count(part2_input)
print(f"Part 2 data input sliding window increases: {data_window}")