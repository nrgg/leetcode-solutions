"""
Turns out the solution needs /Bezout's identity/
"""

import unittest
import heapq
import collections

class Configuration(collections.namedtuple("Configuration", ["jug_1", "jug_2", "jug_1_capacity", "jug_2_capacity"])):

    def neighbors(self):
        # pour 1 -> 2
        space_free_in_2 = self.jug_2_capacity - self.jug_2
        added_to_2 = min(space_free_in_2, self.jug_1)
        left_in_1 = self.jug_1 - added_to_2

        # pour 2 -> 1
        space_free_in_1 = self.jug_1_capacity - self.jug_1
        added_to_1 = min(space_free_in_1, self.jug_2)
        left_in_2 = self.jug_2 - added_to_1

        return [
            # empty jug 1
            Configuration(0, self.jug_2, self.jug_1_capacity, self.jug_2_capacity),

            # empty jug 2
            Configuration(self.jug_1, 0, self.jug_1_capacity, self.jug_2_capacity),

            # fill jug 1
            Configuration(self.jug_1_capacity, self.jug_2, self.jug_1_capacity, self.jug_2_capacity),

            # fill jug 2
            Configuration(self.jug_1, self.jug_2_capacity, self.jug_1_capacity, self.jug_2_capacity),

            # pour 1 -> 2
            Configuration(left_in_1, self.jug_2 + added_to_2, self.jug_1_capacity, self.jug_2_capacity),

            # pour 2 -> 1
            Configuration(self.jug_1 + added_to_1, left_in_2, self.jug_1_capacity, self.jug_2_capacity)
        ]

    def prio(self, z):
        return abs((self.jug_1 + self.jug_2) - z)


class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        initial = Configuration(0, 0, x, y)
        q = [(initial.prio(z), initial)]
        seen = set([initial])
        while len(q):
            prio, config = heapq.heappop(q)
            if prio == 0:
                return True
            for n in config.neighbors():
                if n in seen:
                    continue
                heapq.heappush(q, (n.prio(z), n))
                seen.add(n)
        return False


class SolutionTest(unittest.TestCase):
    def test_1(self):
        self.assertTrue(Solution().canMeasureWater(3,5,4))

    def test_2(self):
        self.assertFalse(Solution().canMeasureWater(2,6,5))

    def test_3(self):
        self.assertTrue(Solution().canMeasureWater(1,2,3))

    def test_4(self):
        self.assertTrue(Solution().canMeasureWater(22003, 31237, 123))

    def test_5(self):
        self.assertTrue(Solution().canMeasureWater(104579, 104593, 12444))
