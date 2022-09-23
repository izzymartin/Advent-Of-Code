# Day 7: The Treachery of Whales

# helper function to find all the elements of a specified length in a list
def find_elements_by_length(input_list, length):
    output = []
    for element in input_list:
        if len(element) == length:
            output.append(element)
    return output

# function for part 1
#   count the easy digits to decode
def easy_digit_decoder(input):
    input_split = input.split("\n")
    unique_num_count = 0
    unique_num = [2, 3, 4, 7]
    for line in input_split:
        for digit in line.split(" | ")[1].split():
            if len(digit) in unique_num:
                unique_num_count += 1
    return unique_num_count


# function for part 2
#   decode digits and sum the resulting numbers
def digit_decoder(input):
    input_split = input.split("\n")
    output = 0
    for line in input_split:
        split_line = line.split(" | ")
        coded_digits = split_line[0].split()
        result_coded = split_line[1].split()
        # Finding a: Take digits for 7 and remove digits from 1
        a = find_elements_by_length(coded_digits,3)[0]
        for character in find_elements_by_length(coded_digits,2)[0]:
            if character in a:
                a = a.replace(character, '')
        # Finding f: Compare digits for 1 to all coded digits with a length of 6
        #            f will exist in all 3 of the length 6 coded digits
        f = find_elements_by_length(coded_digits,2)[0]
        for digit in find_elements_by_length(coded_digits,6):
            if f[0] not in digit:
                f = f.replace(f[0], '')
                break
            if f[1] not in digit:
                f = f.replace(f[1], '')
                break
        # Finding c: 1 contains c & f, and f is known
        c = find_elements_by_length(coded_digits,2)[0]
        c = c.replace(f, '')
        # Finding d: find common segments in length 6 coded digits
        #            remove a and find which overlaps with #4 digit
        d = find_elements_by_length(coded_digits,5)[0]
        for digit in find_elements_by_length(coded_digits,5):
            for character in d:
                if character not in digit:
                    d = d.replace(character, '')
        d = d.replace(a, '')
        for digit in d:
            if digit in find_elements_by_length(coded_digits,4)[0]:
                d = digit
                break
        # Finding g: Find common segments in length 6 coded digits
        #            Remove known segments a and d
        g = find_elements_by_length(coded_digits, 5)[0]
        for digit in find_elements_by_length(coded_digits, 5):
            for character in g:
                if character not in digit:
                    g = g.replace(character, '')
        g = g.replace(a, '')
        g = g.replace(d, '')
        # Finding b: Length 4 coded digit minus known segments
        b = find_elements_by_length(coded_digits, 4)[0]
        b = b.replace(c, '')
        b = b.replace(f, '')
        b = b.replace(d, '')
        # Finding e: Length 7 coded digit minus all known
        e = find_elements_by_length(coded_digits,7)[0]
        e = e.replace(a, '')
        e = e.replace(b, '')
        e = e.replace(c, '')
        e = e.replace(d, '')
        e = e.replace(f, '')
        e = e.replace(g, '')

        output_string = ""
        for digit in result_coded:
            output_digit = ""
            # Decode digits using previously found key
            if a in digit:
                output_digit += "a"
            if b in digit:
                output_digit += "b"
            if c in digit:
                output_digit += "c"
            if d in digit:
                output_digit += "d"
            if e in digit:
                output_digit += "e"
            if f in digit:
                output_digit += "f"
            if g in digit:
                output_digit += "g"

            # Convert to usable number format
            if output_digit == "abcefg":
                output_string += "0"
            elif output_digit == "cf":
                output_string += "1"
            elif output_digit == "acdeg":
                output_string += "2"
            elif output_digit == "acdfg":
                output_string += "3"
            elif output_digit == "bcdf":
                output_string += "4"
            elif output_digit == "abdfg":
                output_string += "5"
            elif output_digit == "abdefg":
                output_string += "6"
            elif output_digit == "acf":
                output_string += "7"
            elif output_digit == "abcdefg":
                output_string += "8"
            elif output_digit == "abcdfg":
                output_string += "9"
            else:
                output_string = "0"
        output += int(output_string)

    return output


with open("inputs/day8test.txt", "r+") as file:
    test_input = file.read()
file.close()

with open("inputs/day8data.txt", "r+") as file:
    data_input = file.read()
file.close()

# call each function with test and data for part 1 and part 2
test_easy_digit_decoder = easy_digit_decoder(test_input)
print(f"Part 1 test digit decoder: {test_easy_digit_decoder}")

data_easy_digit_decoder = easy_digit_decoder(data_input)
print(f"Part 1 data digit decoder: {data_easy_digit_decoder}")

test_digit_decoder = digit_decoder(test_input)
print(f"Part 2 test digit decoder: {test_digit_decoder}")

data_digit_decoder = digit_decoder(data_input)
print(f"Part 2 test digit decoder: {data_digit_decoder}")