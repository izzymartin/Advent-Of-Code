# Day 2: Dive!

# function for part 1
#   counts the position of the sub using commands
def sub_position(commands):
    forward_count = 0
    depth_count = 0

    commands_split = commands.split("\n")

    for line in commands_split:
        line_split = line.split()
        if line_split[0] == "forward":
            forward_count += int(line_split[1])
        elif line_split[0] == "up":
            depth_count -= int(line_split[1])
        elif line_split[0] == "down":
            depth_count += int(line_split[1])
    return forward_count * depth_count

# function for part 2
#   counts the position of the sub using commands including aim
def sub_aim_position(commands):
    forward_count = 0
    depth_count = 0
    aim_count = 0

    commands_split = commands.split("\n")

    for line in commands_split:
        line_split = line.split()
        if line_split[0] == "forward":
            forward_count += int(line_split[1])
            depth_count += aim_count * int(line_split[1])
        elif line_split[0] == "up":
            aim_count -= int(line_split[1])
        elif line_split[0] == "down":
            aim_count += int(line_split[1])
    return forward_count * depth_count

# open test and data file
with open("inputs/day2test.txt", "r+") as file:
    test_input = file.read()
file.close()

with open("inputs/day2data.txt", "r+") as file:
    data_input = file.read()
file.close()


# call each function with test and data for part 1 and part 2
test_position = sub_position(test_input)
print(f"Part 1 test position: {test_position}")

data_position = sub_position(data_input)
print(f"Part 1 data position: {data_position}")

test_aim_position = sub_aim_position(test_input)
print(f"Part 2 test position: {test_aim_position}")

data_aim_position = sub_aim_position(data_input)
print(f"Part 2 data position: {data_aim_position}")