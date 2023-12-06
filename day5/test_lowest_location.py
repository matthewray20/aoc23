

import unittest
import numpy as np
from puzzle1 import get_seeds, create_maps, Mapping, Map, find_lowest


class TestGetSeeds(unittest.TestCase):
    def test_example1(self):
        self.assertTrue((get_seeds('seeds: 79 14 55 13') == [79, 14, 55, 13]).all())
    
    def test_example2(self):
        self.assertTrue((get_seeds('seeds: 364807853 408612163 302918330 20208251 1499552892 200291842 3284226943 16030044 2593569946 345762334 3692780593 17215731 1207118682 189983080 2231594291 72205975 3817565407 443061598 2313976854 203929368') == 
        [364807853, 408612163, 302918330, 20208251, 1499552892, 200291842, 3284226943, 16030044, 2593569946, 345762334, 3692780593, 17215731, 1207118682, 189983080, 2231594291, 72205975, 3817565407, 443061598, 2313976854, 203929368]).all())



class TestCreateMapping(unittest.TestCase):
    def test_example1(self):
        self.assertTrue((create_maps([
            'seed-to-soil map:',
            '50 98 2',
            '52 50 48',
            '',
            'soil-to-fertilizer map:',
            '0 15 37',
            '37 52 2',
            '39 0 15',
            '',
            'fertilizer-to-water map:',
            '49 53 8',
            '0 11 42',
            '42 0 7',
            '57 7 4',
            '',
            'water-to-light map:',
            '88 18 7',
            '18 25 70',
            '',
            'light-to-temperature map:',
            '45 77 23',
            '81 45 19',
            '68 64 13',
            '',
            'temperature-to-humidity map:',
            '0 69 1',
            '1 0 69',
            '',
            'humidity-to-location map:',
            '60 56 37',
            '56 93 4'
            ]) == [
                Map().add(Mapping(98, 50, 2)).add(Mapping(50, 52, 48))._set_name('seed-to-soil map'),
                Map().add(Mapping(15, 0, 37)).add(Mapping(52, 37, 2)).add(Mapping(0, 39, 15))._set_name('soil-to-fertilizer map'),
                Map().add(Mapping(53, 49, 8)).add(Mapping(11, 0, 42)).add(Mapping(0, 42, 7)).add(Mapping(7, 57, 4))._set_name('fertilizer-to-water map'),
                Map().add(Mapping(18, 88, 7)).add(Mapping(25, 18, 70))._set_name('water-to-light map'),
                Map().add(Mapping(77, 45, 23)).add(Mapping(45, 81, 19)).add(Mapping(64, 68, 13))._set_name('light-to-temperature map'),
                Map().add(Mapping(69, 0, 1)).add(Mapping(0, 1, 69))._set_name('temperature-to-humidity map'),
                Map().add(Mapping(56, 60, 37)).add(Mapping(93, 56, 4))._set_name('humidity-to-location map')
            ]).all())



class TestLowestLocation(unittest.TestCase):
    def test_example1(self):
        seeds = np.array([79, 14, 55, 13], dtype=np.int64)
        maps = [
                Map().add(Mapping(98, 50, 2)).add(Mapping(50, 52, 48))._set_name('seed-to-soil map'),
                Map().add(Mapping(15, 0, 37)).add(Mapping(52, 37, 2)).add(Mapping(0, 39, 15))._set_name('soil-to-fertilizer map'),
                Map().add(Mapping(53, 49, 8)).add(Mapping(11, 0, 42)).add(Mapping(0, 42, 7)).add(Mapping(7, 57, 4))._set_name('fertilizer-to-water map'),
                Map().add(Mapping(18, 88, 7)).add(Mapping(25, 18, 70))._set_name('water-to-light map'),
                Map().add(Mapping(77, 45, 23)).add(Mapping(45, 81, 19)).add(Mapping(64, 68, 13))._set_name('light-to-temperature map'),
                Map().add(Mapping(69, 0, 1)).add(Mapping(0, 1, 69))._set_name('temperature-to-humidity map'),
                Map().add(Mapping(56, 60, 37)).add(Mapping(93, 56, 4))._set_name('humidity-to-location map')
            ]
        self.assertEqual(find_lowest(maps, seeds), 35)


if __name__ == "__main__":
    unittest.main()