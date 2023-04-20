# Day 6: Lanternfish

# function for part 1
#   Calculates lanternfish lifecycle
def lanternfish(input, days):
    input_split = [int(y) for y in input.split(",")]
    fish_pool = []
    # Convert fish life input, to list count the number of fish x days old
    for fish_life in range(9):
        fish_pool.append(input_split.count(fish_life))
    day_count = 0
    while day_count != days:
        new_fish = fish_pool.pop(0)
        fish_pool.append(new_fish)
        fish_pool[6] += new_fish
        day_count += 1
    return sum(fish_pool)


with open("inputs/day6test.txt", "r+") as file:
    test_input = file.read()
file.close()

with open("inputs/day6data.txt", "r+") as file:
    data_input = file.read()
file.close()

# call each function with test and data for part 1 and part 2
test_lanternfish = lanternfish(test_input, 80)
print(f"Part 1 test lanternfish life cycle: {test_lanternfish}")

data_lanternfish = lanternfish(data_input, 80)
print(f"Part 1 data lanternfish life cycle: {data_lanternfish}")

test_lanternfish = lanternfish(test_input, 256)
print(f"Part 1 test lanternfish life cycle: {test_lanternfish}")

data_lanternfish = lanternfish(data_input, 256)
print(f"Part 1 data lanternfish life cycle: {data_lanternfish}")
