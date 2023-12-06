
import numpy as np
from puzzle1 import Mapping, Map
from puzzle1 import create_maps, find_lowest

def parse_seed_ranges(seed_str):
    seed_specs = [int(n) for n in seed_str[7:].split()]
    seed_ranges = []
    for i in range(0, len(seed_specs), 2):
        # range start, range end, range length
        seed_ranges.append((seed_specs[i], seed_specs[i] + seed_specs[i+1], seed_specs[i+1]))
    return seed_ranges


def get_seeds(seed_ranges, num_chunks):
    # count total num seeds
    num_seeds = np.sum(np.array([sr[2] for sr in seed_ranges], dtype=np.int64))

    # try all in one
    seeds = np.zeros(num_seeds, dtype=np.int64)
    index = 0
    for start, end, length in seed_ranges:
        #print('setting', seeds[index: index + length])
        #print('which is length', len(seeds[index: index + length]))
        #print('with', np.arange(start, end))
        #print('which is length', len(np.arange(start, end)))
        seeds[index: index + length] = np.arange(start, end)
        #print()
        index += length
    
    return seeds
    

"""
This does run but takes a bit of time
Can optimise more but didn't have time
-- single core, cpu only, no algorithmic optimisation 
Run on M1 Pro (16GB memory)
Timing details: 264.73s user 934.03s system 71% cpu 27:57.81 total
"""


def main():
    with open('puzzle_input.txt', 'r') as f:
        whole_input = [line.strip() for line in f]
    # create mappings and ranges
    seed_ranges = parse_seed_ranges(whole_input[0])
    print('made seed ranges')
    mappings = create_maps(whole_input[2:])
    print('created maps')
    
    # split computation to reduce memory usage
    #chunks = 4
    #for i in range(chunks):
    seeds = get_seeds(seed_ranges, 1)
    print('created seeds array')
    lowest = find_lowest(mappings, seeds)
    #final_lowest = np.min(lowest)
    print('The lowest location found from the initial seeds is:', lowest) #final_lowest)


if __name__ == "__main__":
    main()