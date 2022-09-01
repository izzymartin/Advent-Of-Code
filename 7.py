# Day 7: The Treachery of Whales

# function for part 1
#   calculates the minimum fuel usage to align crabs into position
def alignment_fuel(input):
    input_split = [int(y) for y in input.split(",")]
    position_fuel = [0]*max(input_split)
    for position in range(max(input_split)):
        for crab in input_split:
            position_fuel[position] += abs(crab - position)
    return min(position_fuel)


# function for part 2
#   calculates the minimum fuel usage to align crabs into position, using the expensive fuel cost
def alignment_fuel_expensive(input):
    input_split = [int(y) for y in input.split(",")]
    position_fuel = [0]*max(input_split)
    for position in range(max(input_split)):
        for crab in input_split:
            position_fuel[position] += sum([num for num in range(abs(crab - position) + 1)])
    return min(position_fuel)


with open("inputs/day7test.txt", "r+") as file:
    test_input = file.read()
file.close()

with open("inputs/day7data.txt", "r+") as file:
    data_input = file.read()
file.close()

# call each function with test and data for part 1 and part 2
test_alignment_fuel = alignment_fuel(test_input)
print(f"Part 1 test crab alignment fuel consumption: {test_alignment_fuel}")

data_alignment_fuel = alignment_fuel(data_input)
print(f"Part 1 data crab alignment fuel consumption: {data_alignment_fuel}")

test_alignment_fuel_expensive = alignment_fuel_expensive(test_input)
print(f"Part 2 test crab alignment fuel consumption: {test_alignment_fuel_expensive}")

data_alignment_fuel_expensive = alignment_fuel_expensive(data_input)
print(f"Part 2 data crab alignment fuel consumption: {data_alignment_fuel_expensive}")

