import unittest

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @classmethod
    def make(cls, x, lt, rt):
        rval = cls(x)
        rval.left = lt
        rval.right = rt
        return rval


def groupby(l, key):
    rval = []

    first = True
    cur = []

    for el in l:
        if first:
            first = False
            cur.append(el)
        else:
            if key(el) == key(prev):
                cur.append(el)
            else:
                rval.append(cur)
                cur = [el]
        prev = el
    rval.append(cur)
    return rval


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if root is None:
            return []

        def level_order_r(t):
            def level_order_r_helper(t, depth, width):
                rval = [(depth, (-1 if depth % 2 else 1) * width, t.val)]
                if t.left is not None:
                    rval.extend(level_order_r_helper(t.left, depth + 1, (depth + 1) * width))
                if t.right is not None:
                    rval.extend(level_order_r_helper(t.right, depth + 1, (depth + 1) * width + 1))
                return rval
            return level_order_r_helper(t, 0, 0)

        with_depth = level_order_r(root)
        rval = []
        for all_in_level in groupby(sorted(with_depth), lambda x: x[0]):
            this_level = []
            for level, prio, val in all_in_level:
                this_level.append(val)
            rval.append(this_level)
        return rval


class SolutionTest(unittest.TestCase):
    def test_1(self):
        self.assertEquals(
            Solution().zigzagLevelOrder(
                TreeNode.make(
                    3,
                    #TreeNode.make(20, TreeNode(-15), TreeNode(-7)),
                    TreeNode(9),
                    TreeNode.make(20, TreeNode(15), TreeNode(7))
                )
            ),
            [
                [3],
                [20,9],
                [15,7]
            ]
        )

    def test_2(self):
        self.assertEquals(Solution().zigzagLevelOrder(None), [])
