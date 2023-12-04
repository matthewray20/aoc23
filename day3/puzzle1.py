import re

# check if character is a symbol
def is_symbol(c: str) -> bool:
    return not c.isnumeric() and c != '.'

# check if a symbol exists in a string
def contains_symbol(string: str) -> bool:
    for char in string:
        if is_symbol(char): return True
    return False


# find and sum part numbers
def part_numbers(engine: [str]) -> int:
    # set variables
    count = 0
    engine_length = len(engine)
    engine_width = len(engine[0])
    for line in range(engine_length):
        # find all numbers
        matches = re.finditer(r'\d+', engine[line])
        for match in matches:
            is_part_num = False
            # set width constraints
            start, end = match.start(), match.end()
            if start > 0: start -= 1
            if end < engine_width: end += 1
            # check relevant windows
            if line > 0 and contains_symbol(engine[line - 1][start:end]): is_part_num = True
            if contains_symbol(engine[line][start:end+1]): is_part_num = True
            if line < engine_length - 1 and contains_symbol(engine[line + 1][start:end]): is_part_num = True
            # add part number if necessary
            if is_part_num: count += int(match.group())

    return count


# open and read file
def main() -> None:
    with open('puzzle_input.txt', 'r') as f:
        whole_input = [line.strip() for line in f]
    print('The sum of all engine part numbers is:', part_numbers(whole_input))



if __name__ == "__main__":
    main()