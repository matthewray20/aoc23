


import unittest
from puzzle1 import Infinite
from puzzle1 import parse_input, follow_graph



class TestInfinite(unittest.TestCase):
    def test_example1(self):
        test_over = range(10)
        inf = Infinite(test_over)
        test_range = list(test_over).extend(list(test_over))
        for n in test_over:
            self.assertEqual(n, inf.get_next())


class TestParseInput(unittest.TestCase):
    def test_example1(self):
        expected_steps = Infinite(['L', 'L', 'R'])
        expected_graph = {
            'AAA': ('BBB', 'BBB'),
            'BBB': ('AAA', 'ZZZ'),
            'ZZZ': ('ZZZ', 'ZZZ')
        }
        inp = [
            'LLR',
            '',
            'AAA = (BBB, BBB)',
            'BBB = (AAA, ZZZ)',
            'ZZZ = (ZZZ, ZZZ)'
        ]
        graph, steps = parse_input(inp)
        self.assertEqual(graph, expected_graph)
        self.assertEqual(steps, expected_steps)


class TestFollowGraph(unittest.TestCase):
    def test_example1(self):
        inp = [
            'LLR',
            '',
            'AAA = (BBB, BBB)',
            'BBB = (AAA, ZZZ)',
            'ZZZ = (ZZZ, ZZZ)'
        ]
        graph, steps = parse_input(inp)
        self.assertEqual(follow_graph(graph, steps), 6)




if __name__ == "__main__":
    unittest.main()