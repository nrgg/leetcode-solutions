import unittest


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)

        is_vowel = lambda x: x.lower() in "aeiou"

        idxs = [i for i in range(len(s)) if is_vowel(s[i])]

        for i in range(len(idxs) // 2):
            tmp = s[idxs[i]]
            s[idxs[i]] = s[idxs[len(idxs) - i - 1]]
            s[idxs[len(idxs) - i - 1]] = tmp

        return "".join(s)

class SolutionTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Solution().reverseVowels("hello"), "holle")

    def test_2(self):
        self.assertEqual(Solution().reverseVowels("leetcode"), "leotcede")

    def test_3(self):
        self.assertEqual(Solution().reverseVowels("xyzgr"), "xyzgr")

    def test_4(self):
        self.assertEqual(Solution().reverseVowels("aA"), "Aa")
