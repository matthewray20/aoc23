

"""
A class to take an array of objects that returns the next index, but repeats when it reaches the end
"""
class Infinite:
    def __init__(self, to_repreat):
        self.to_repreat = to_repreat if isinstance(to_repreat, list) else list(to_repreat)
        self.length = len(to_repreat)
        self.index = 0
    
    def get_next(self):
        to_return = self.to_repreat[self.index]
        self.index = (self.index + 1) % self.length
        return to_return
    
    def __eq__(self, other):
        # for testing
        return self.to_repreat == other.to_repreat and self.index == other.index
    
    def reset(self):
        self.index = 0



def parse_input(inp):
    steps_string = inp[0]
    steps = Infinite(steps_string)

    graph = {}
    for line in inp[2:]:
        graph[line[:3]] = (line[7:10], line[12:15])
    
    return graph, steps


def follow_graph_until(graph, steps, start_node, fcn):
    curr_node = start_node
    count = 0
    while not fcn(curr_node):
        direction = steps.get_next()
        if direction == 'L' and graph[curr_node][0] is not None:
            curr_node = graph[curr_node][0]
        elif direction == 'R' and graph[curr_node][1] is not None:
            curr_node = graph[curr_node][1]
        else:
            raise TypeError(f'Cannot move in direction "{direction}" to a child that is None')

        count += 1
    return count


def follow_graph(graph, steps):
    return follow_graph_until(graph, steps, 'AAA', lambda x: x == 'ZZZ')


def main():
    with open('puzzle_input.txt', 'r') as f:
        graph, steps = parse_input([line.strip() for line in f])
    total_steps = follow_graph(graph, steps)
    
    print('The total number of steps taken is:', total_steps)



if __name__ == "__main__":
    main()