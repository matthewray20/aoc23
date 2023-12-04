

import re

# Check if games are possible (i.e any colour pulled oout of bag is less than number of colours in bag)
def min_possible_game(game: str) -> int:
    game_no = int(re.search(r'Game \d+', game).group()[5:])
    pattern = r'(?P<num>\d+) (?P<col>red|green|blue)' # Number of one or more digit, space, red or green or blue
    count = {'red': 0, 'blue': 0, 'green': 0}
    for match in re.finditer(pattern, game): 
        num, col = int(match.group('num')), match.group('col')
        if num > count[col]:
            count[col] = num
    return count['red'] * count['green'] * count['blue']
    
# open file and sum lines
def main() -> None:
    with open("puzzle_input.txt", 'r') as f:
        total = sum([min_possible_game(game) for game in f])
    print("The sum of line numbers for possible games is:", total)


# run main
if __name__ == "__main__":
    main()