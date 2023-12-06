import numpy as np

class Mapping:
    def __init__(self, source_start, destination_start, length):
        self.source_start = source_start
        self.destination_start = destination_start
        self.source_end = source_start + length
    
    def __eq__(self, other):
        # for testing need equality check
        return (self.source_start == other.source_start and
            self.destination_start == other.destination_start and
            self.source_end == other.source_end)
    
    def _set_map(self, new_map):
        self.map = new_map
    
    def __repr__(self):
        return f'Mapping(name={self.name}, map={self.map})'



class Map:
    def __init__(self):
        self.mappings = []
        self.name = None
    
    def _set_name(self, name):
        self.name = name
        return self
    
    def add(self, mapping):
        self.mappings.append(mapping)
        return self

    def __eq__(self, other):
        # for testing
        return self.mappings == other.mappings
    
    def __call__(self, x):
        already_mapped = np.zeros(x.shape, dtype=bool)
        for mapping in self.mappings:
            #print(x)
            mask = ~already_mapped & (x >= mapping.source_start) & (x < mapping.source_end)
            x[mask] = mapping.destination_start + (x[mask] - mapping.source_start)
            already_mapped[mask] = True
        return x
    

def get_seeds(seeds):
    return np.array([int(num) for num in seeds[7:].split(' ')], dtype=np.int64)


def create_maps(data):
    # variables
    maps = []
    curr_name = ''
    curr_map = Map()
    # looping over data
    for line in data:
        if len(line) > 0 and line[0].isalpha():
            # get name for debugging and testing
            curr_name = line[:-1]
        elif len(line) > 0 and line[0].isnumeric():
            # make new mapping and combine
            nums = [int(num) for num in line.split(' ')]
            assert len(nums) == 3
            curr_map.add(Mapping(nums[1], nums[0], nums[2]))
        else:
            # add mapping to list and start fresh
            curr_map._set_name(curr_name)
            maps.append(curr_map)
            curr_map = Map()
    # since no last line to add final mapping, do here
    curr_map._set_name(curr_name)
    maps.append(curr_map)
    return np.array(maps)


def find_lowest(maps, seeds):
    # map each function to the array of seeds
    for map_i in maps:
        seeds = map_i(seeds)

    # get the lowest value
    return np.min(seeds)


def main():
    with open('puzzle_input.txt', 'r') as f:
        whole_input = [line.strip() for line in f]
    seeds = get_seeds(whole_input[0])
    mappings = create_maps(whole_input[2:])
    lowest = find_lowest(mappings, seeds)
    print('The lowest location found from the initial seeds is:', lowest)


if __name__ == "__main__":
    main()