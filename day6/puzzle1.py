
import re
import numpy as np

# read the numbers from the input
def find_nums(string):
    return [int(n) for n in re.findall(r'\d+', string)]

# collect the time and distace numbers and combine 
def parse_races(data):
    times = find_nums(data[0])
    distances = find_nums(data[1])
    return np.array([race for race in zip(times, distances)])

# count the number of ways to win a race
def ways_to_win_races(race):
    button_hold_time = np.arange(0, race[0])
    distance_travel = (race[0] - button_hold_time) * button_hold_time
    num_winning_ways = (len(button_hold_time[distance_travel > race[1]]))
    return num_winning_ways


def main():
    with open('puzzle_input.txt', 'r') as f:
        data = [line for line in f]
    races = parse_races(data)
    total = np.prod(np.array([ways_to_win_races(race) for race in races]))
    print('The product of all ways to win a race is', total)


if __name__ == "__main__":
    main()