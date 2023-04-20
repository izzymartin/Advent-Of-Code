# Day 4: Giant Squid

# function for part 1
#   findings the winning bingo board and computes the final score
def bingo(board):
    bingo_numbers = []
    bingo_boards = []
    checked_numbers = []
    board_split = board.split("\n")
    temp_board = [[0]*5]*5
    # Parsing the given text into bingo numbers and bing boards
    #   NOTE: This does require correct formatting of the text files
    for index, line in enumerate(board_split):
        if index == 0:
            bingo_numbers = line.split(",")
        elif line != "":
            temp_board[(index-2)%6] = line.split()
            if (index-2)%6 == 4:
                bingo_boards.append(temp_board)
                temp_board = [[0] * 5] * 5
    # Skipping the first 4 numbers because you need 5 for a bingo
    for i in range(4):
        checked_numbers.append(bingo_numbers.pop(0))
    found_win = 0
    while len(bingo_numbers) != 0:
        checked_numbers.append(bingo_numbers.pop(0))
        for board_loop in range(len(bingo_boards)):
            for row in range(5):
                row_match_count = sum(bingo_boards[board_loop][row][column] in checked_numbers for column in range(5))
                if row_match_count == 5:
                    winning_board = board_loop
                    found_win = True
                    break
            for column in range(5):
                column_match_count = sum(bingo_boards[board_loop][row][column] in checked_numbers for row in range(5))
                if column_match_count == 5:
                    winning_board = board_loop
                    found_win = True
                    break
            if found_win:
                break
        if found_win:
            break

    if found_win:
        unmarked_num_count = 0
        for row in range(5):
            for column in range(5):
                if bingo_boards[winning_board][row][column] not in checked_numbers:
                    unmarked_num_count += int(bingo_boards[winning_board][row][column])
        return unmarked_num_count * int(checked_numbers[-1])
    else:
        return 0


# function for part 2
#   findings the last winning bingo board and computes the final score
def bingo_last(board):
    bingo_numbers = []
    bingo_boards = []
    checked_numbers = []
    board_split = board.split("\n")
    temp_board = [[0]*5]*5
    # Parsing the given text into bingo numbers and bing boards
    #   NOTE: This does require correct formatting of the text files
    for index, line in enumerate(board_split):
        if index == 0:
            bingo_numbers = line.split(",")
        elif line != "":
            temp_board[(index-2)%6] = line.split()
            if (index-2)%6 == 4:
                bingo_boards.append(temp_board)
                temp_board = [[0] * 5] * 5
    # Skipping the first 4 numbers because you need 5 for a bingo
    for i in range(4):
        checked_numbers.append(bingo_numbers.pop(0))
    found_wins = [0]*len(bingo_boards)
    while len(bingo_numbers) != 0:
        checked_numbers.append(bingo_numbers.pop(0))
        for board_loop in range(len(bingo_boards)):
            for row in range(5):
                row_match_count = sum(bingo_boards[board_loop][row][column] in checked_numbers for column in range(5))
                if row_match_count == 5:
                    found_wins[board_loop] = 1
                    if sum(found_wins) == len(bingo_boards):
                        losing_board = board_loop
                        break
            for column in range(5):
                column_match_count = sum(bingo_boards[board_loop][row][column] in checked_numbers for row in range(5))
                if column_match_count == 5:
                    found_wins[board_loop] = 1
                    if sum(found_wins) == len(bingo_boards):
                        losing_board = board_loop
                        break
            if sum(found_wins) == len(bingo_boards):
                break
        if sum(found_wins) == len(bingo_boards):
            break

    if sum(found_wins) == len(bingo_boards):
        unmarked_num_count = 0
        for row in range(5):
            for column in range(5):
                if bingo_boards[losing_board][row][column] not in checked_numbers:
                    unmarked_num_count += int(bingo_boards[losing_board][row][column])
        return unmarked_num_count * int(checked_numbers[-1])
    else:
        return 0


with open("inputs/day4test.txt", "r+") as file:
    test_input = file.read()
file.close()

with open("inputs/day4data.txt", "r+") as file:
    data_input = file.read()
file.close()

# call each function with test and data for part 1 and part 2
test_bingo_score = bingo(test_input)
print(f"Part 1 test bingo score: {test_bingo_score}")

data_bingo_score = bingo(data_input)
print(f"Part 1 data bingo score: {data_bingo_score}")

test_losing_bingo_score = bingo_last(test_input)
print(f"Part 2 test bingo score: {test_losing_bingo_score}")

data_losing_bingo_score = bingo_last(data_input)
print(f"Part 2 test bingo score: {data_losing_bingo_score}")