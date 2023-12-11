




import unittest
from puzzle1 import parse_input
from puzzle2 import follow_graph_multiple




class TestFollowGraphMultiple(unittest.TestCase):
    def test_example1(self):
        inp = [
            'LR',
            '',
            '11A = (11B, XXX)',
            '11B = (XXX, 11Z)',
            '11Z = (11B, XXX)',
            '22A = (22B, XXX)',
            '22B = (22C, 22C)',
            '22C = (22Z, 22Z)',
            '22Z = (22B, 22B)',
            'XXX = (XXX, XXX)'
        ]
        graph, steps = parse_input(inp)
        self.assertEqual(follow_graph_multiple(graph, steps), 6)





if __name__ == "__main__":
    unittest.main()