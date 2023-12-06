
import re
import numpy as np
from puzzle1 import ways_to_win_races


# get the single number from the multiple number strngs
def find_num(string):
    return int(''.join([n for n in re.findall(r'\d+', string)]))

# combine the time and distance into format to reuse ways_to_win_races from puzzle1.py
def parse_races(data):
    time = find_num(data[0])
    distance = find_nums(data[1])
    return np.array([[time, distance]])
    


def main():
    with open('puzzle_input.txt', 'r') as f:
        data = [line for line in f]
    races = parse_races(data)
    total = np.prod(np.array([ways_to_win_races(race) for race in races]))
    print('The product of all ways to win a race is', total)



if __name__ == "__main__":
    main()