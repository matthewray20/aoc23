
import re

# check if a and b are touching
def touching(a: re.Match, b: re.Match) -> bool:
    x1, x2, y1, y2 = a.start(), a.end(), b.start(), b.end()
    return (x1 <= y2 and x2 >= y1) or (y1 <= x2 and y2 >= x1)


# calculate the sum of gear ratios in the engine
def gear_ratios(engine: [str]) -> int:
    # set variables
    count = 0
    engine_length = len(engine)
    engine_width = len(engine[0])
    for line in range(engine_length):
        matches = re.finditer(r'\*', engine[line])
        for match in matches:
            found_gear = False
            # set width constraints
            start, end = match.start(), match.end()
            if start > 0: start -= 1
            if end < engine_width: end += 1
            # check relevant windows
            nums = []
            for window in [engine[line + i] for i in [-1, 0, 1] if (line - i >= 0 and line - i < engine_length)]:
                neighbours = re.finditer(r'\d+', window)
                for neighbour in neighbours:
                    if touching(neighbour, match):
                        nums.append(int(neighbour.group()))
            if len(nums) == 2:
                count += nums[0] * nums[1]
    return count

# open and read file
def main() -> None:
    with open('puzzle_input.txt', 'r') as f:
        whole_input = [line.strip() for line in f]
    print('The sum of all gear ratios is:', gear_ratios(whole_input))


if __name__ == "__main__":
    main()