
import math

from puzzle1 import Infinite
from puzzle1 import parse_input, follow_graph_until


# finds the lowest common multiple of a list of numbers
# brute force bad prg way
def lcm(nums):
    result = 1
    for i in nums:
        result = result * i // math.gcd(result, i)
    return result


def follow_graph_multiple(graph, steps):
    start_nodes = [node for node in graph.keys() if node.endswith("A")]
    counts = []
    for node in start_nodes:
        steps.reset()
        counts.append(follow_graph_until(graph, steps, node, lambda x: x.endswith('Z'))) #(node, follow_graph(graph, steps)))

    return lcm(counts)



def main():
    with open('puzzle_input.txt', 'r') as f:
        graph, steps = parse_input([line.strip() for line in f])
    total_steps = follow_graph_multiple(graph, steps)
    
    print('The total number of steps taken is:', total_steps)



if __name__ == "__main__":
    main()