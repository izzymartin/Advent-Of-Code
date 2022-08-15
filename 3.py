# Day 3: Binary Diagnostic

# function for part 1
#   finds the power rate on the submarine
def diag_power_rate(diag_report):
    diag_report_split = diag_report.split("\n")

    bit_list = [0] * len(diag_report_split[0])
    gamma_rate_list = [0] * len(diag_report_split[0])
    gamma_rate_string = ""
    epsilon_rate_list = [0] * len(diag_report_split[0])
    epsilon_rate_string = ""
    entry_number = len(diag_report_split)

    for line in diag_report_split:
        for index, bit in enumerate(line):
            bit_list[index] += int(bit)
    for index, bits in enumerate(bit_list):
        if bits > (entry_number/2):
            gamma_rate_list[index] = 1
        else:
            epsilon_rate_list[index] = 1
    for element in gamma_rate_list:
        gamma_rate_string += str(element)
    gamma_rate = int(gamma_rate_string,2)
    for element in epsilon_rate_list:
        epsilon_rate_string += str(element)
    epsilon_rate = int(epsilon_rate_string,2)
    return gamma_rate * epsilon_rate

# function for part 1
#   finds the life support rating of the submarine
def diag_life_support_rating(diag_report):
    diag_report_split = diag_report.split("\n")

    oxygen_list = diag_report_split.copy()
    co2_list = diag_report_split.copy()
    bit_position = 0

    # Looping through list and counting numbers of 1s in each bit position
    while (bit_position < len(diag_report_split[0])):
        bit_count = 0
        line_count = len(oxygen_list) - 1
        for line in oxygen_list:
            bit_count += int(line[bit_position])
        if bit_count >= len(oxygen_list)/2:
            major_bit = 1
        else:
            major_bit = 0
        while (line_count >= 0):
            if int(oxygen_list[line_count][bit_position]) != major_bit:
                if len(oxygen_list) > 1:
                    del oxygen_list[line_count]
            line_count -= 1
        bit_position += 1

    bit_position = 0
    while (bit_position < len(diag_report_split[0])):
        bit_count = 0
        line_count = len(co2_list) - 1
        for line in co2_list:
            bit_count += int(line[bit_position])
        if bit_count >= len(co2_list)/2:
            major_bit = 0
        else:
            major_bit = 1
        while (line_count >= 0):
            if int(co2_list[line_count][bit_position]) != major_bit:
                if len(co2_list) > 1:
                    del co2_list[line_count]
            line_count -= 1
        bit_position += 1

    oxygen_gen_rating = int(oxygen_list[0],2)
    co2_scrub_rating = int(co2_list[0],2)

    return oxygen_gen_rating * co2_scrub_rating

# open test and data file
with open("inputs/day3test.txt", "r+") as file:
    test_input = file.read()
file.close()

with open("inputs/day3data.txt", "r+") as file:
    data_input = file.read()
file.close()


# call each function with test and data for part 1 and part 2
test_power_rate = diag_power_rate(test_input)
print(f"Part 1 test power rate: {test_power_rate}")

data_power_rate = diag_power_rate(data_input)
print(f"Part 1 test power rate: {data_power_rate}")

test_life_support_rating = diag_life_support_rating(test_input)
print(f"Part 2 test life support rating: {test_life_support_rating}")

data_life_support_rating = diag_life_support_rating(data_input)
print(f"Part 2 data life support rating: {data_life_support_rating}")