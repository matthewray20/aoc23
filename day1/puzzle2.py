import re

# Find the first and last numbers including string numbers
def find_real_calibration_value(jumbled: str) -> int:
    number_strings = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
    }

    matches = ['' for _ in range(len(jumbled))]
    all_number_options = [n for kv in number_strings.items() for n in kv]
    for number in all_number_options:
        curr_idx = 0
        idx = jumbled.find(number)
        #print(number, jumbled, number in jumbled)
        while idx >= 0:
            matches[idx] = number_strings[number] if number in number_strings else number
            curr_idx = idx + 1
            idx = jumbled.find(number, curr_idx)
    matches = [match for match in matches if match.isnumeric()]
    return int(matches[0] + matches[-1])

    
# open file and sum values
def main() -> None:
    with open("puzzle_input.txt", 'r') as f:
        total = sum((find_real_calibration_value(line) for line in f))
    print(f"The sum of all real calibration values is: {total}")
    
"""
Initially tried using re module, got good results but was a bug.
AoC on reddit: The right calibration values for string "eighthree" is 83 and for "sevenine" is 79
Because re consumes the pattern it matches, matching "eight" leaves "hree" remaining
I didn't see an easy fix while still using re, so moved to .find because it gives index and doesn't consume
"""
        

# run main
if __name__ == "__main__":
    main()