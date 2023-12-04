
# calculate the points for the scratch it card
def calculate_points(card: str) -> int:
    # remove 'Card   x: '
    truncate_first = 9
    #truncate_first = 7 ### TEST TRUNCATE
    card = card[truncate_first:] 
    
    # variabes
    step_size = 3
    """
    start_idx_winning = 0
    start_idx_scratched = 32
    num_winning = 10
    num_scratched = 25
    """
    #### TEST VARIABLES
    start_idx_winning = 0
    start_idx_scratched = 17
    num_winning = 5
    num_scratched = 8

    # easy pattern so no need for re - just loop over
    winning = [card[i:i+step_size] for i in range(start_idx_winning, step_size * num_winning, step_size)]
    scratched = [card[i:i+step_size] for i in range(start_idx_scratched, step_size * num_scratched + start_idx_scratched, step_size)]
    matched = [i for i in scratched if i in winning]
    
    #calc points
    num_match = len(matched)
    points = 2 ** (num_match - 1) if num_match > 0 else 0
    
    return points


# main - read file and print output
def main() -> None:
    with open('puzzle_input.txt') as f:
        points = sum([calculate_points(line) for line in f])
    print(f'The total number of points won by the cards is {points}')


if __name__ == "__main__":
    main()