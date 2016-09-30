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


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if root is None:
            return []

        d = {}
        q = [(root, 0, 0)]
        while q:
            t, depth, width = q.pop()
            if depth in d:
                d[depth].append(((-1 if depth % 2 else 1) * width, t.val))
            else:
                d[depth] = [((-1 if depth % 2 else 1) * width, t.val)]
            if t.left is not None:
                q.append((t.left, depth + 1, (depth + 1) * width))
            if t.right is not None:
                q.append((t.right, depth + 1, (depth + 1) * width + 1))
        rval = []
        for d, vals in sorted(d.items(), key=lambda x: x[0]):
            rval.append([val for width, val in sorted(vals)])
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
