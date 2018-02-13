import random
import copy

# PUZZLE VARIABLES
lowest_number = 1
highest_number = 9
number_of_tries = 10  # Number of times the puzzle should be tried to be solved
solution = 66  # What the end result should show
puzzle = "a + 13 * a / a + a + 12 * a - a - 11 + a * a / a - 10"

# PROGRAM START BELOW, DO NOT CHANGE
unknown_numbers = puzzle.count("a")
print("unknown numbers: ", unknown_numbers)
numbers = []
for j in range(number_of_tries):
    temp_solution = None
    while temp_solution != solution:
        temp_puzzle = copy.copy(puzzle)
        numbers.clear()
        for i in range(unknown_numbers):
            while True:
                random_number = random.randint(lowest_number, highest_number)
                if random_number not in numbers:
                    numbers.append(random_number)
                    break
            found_a = temp_puzzle.find("a")
            temp_puzzle = temp_puzzle[: found_a] + str(numbers[i]) + temp_puzzle[found_a + 1:]
        temp_solution = eval(temp_puzzle)
    print("solution {} found: ".format(j+1), numbers)


