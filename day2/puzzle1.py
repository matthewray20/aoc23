

import re

# Check if games are possible (i.e any colour pulled oout of bag is less than number of colours in bag)
def possible_game(game: str, conditions: dict) -> int:
    game_no = int(re.search(r'Game \d+', game).group()[5:])
    pattern = r'(?P<num>\d+) (?P<col>red|green|blue)' # Number of one or more digit, space, red or green or blue
    return game_no if all([int(match.group('num')) <= conditions[match.group('col')] for match in re.finditer(pattern, game)]) else 0
    
# open file and sum lines
def main() -> None:
    conditions = {'red': 12, 'green': 13, 'blue': 14}
    with open("puzzle_input.txt", 'r') as f:
        total = sum([possible_game(game, conditions) for game in f])
    print("The sum of line numbers for possible games is:", total)


# run main
if __name__ == "__main__":
    main()