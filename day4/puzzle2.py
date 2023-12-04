
# from puzzle1 just renamed and not points calculation
# calculate the points for the scratch it card
def calculate_copies(card: str) -> int:
    # remove 'Card   x: '
    truncate_first = 9
    #truncate_first = 7 ### TEST TRUNCATE
    card = card[truncate_first:] 
    
    # variabes
    step_size = 3
    
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
    """
    # easy pattern so no need for re - just loop over
    winning = [card[i:i+step_size] for i in range(start_idx_winning, step_size * num_winning, step_size)]
    scratched = [card[i:i+step_size] for i in range(start_idx_scratched, step_size * num_scratched + start_idx_scratched, step_size)]
    matched = [i for i in scratched if i in winning]
    
    num_match = len(matched)
    
    return num_match


def count_copies(cards: [str]) -> int:
    # list to hold the number of each card
    tally = [1 for _ in cards] # always have one initial card for each
    # calculate winners and card copies
    for ind, card in enumerate(cards):
        num_winners = calculate_copies(card)
        for i in range(1, num_winners + 1):
            tally[ind + i] += tally[ind]
    return sum(tally)


def main() -> None:
    with open('puzzle_input.txt', 'r') as f:
        whole_input = [line for line in f]
    total = count_copies(whole_input)
    
    print('The total number of cards is', total)



if __name__ == "__main__":
    main()