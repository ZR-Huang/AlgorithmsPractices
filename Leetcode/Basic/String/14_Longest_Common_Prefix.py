import unittest


class TestSolutionMethods(unittest.TestCase):
    def test_longestCommonPrefix(self):
        s = Solution()

        strs = ["flower","flow","flight"]
        self.assertEqual(s.longestCommonPrefix(strs), "fl")

        strs = ["dog","racecar","car"]
        self.assertEqual(s.longestCommonPrefix(strs), "")

        strs = ["dog"]
        self.assertEqual(s.longestCommonPrefix(strs), "dog")

        strs = []
        self.assertEqual(s.longestCommonPrefix(strs), "")


class Solution:
    def longestCommonPrefix(self, strs)->str:
        common_prefix = []

        # check whether "" in the list or the list is not empty
        if "" in strs or not strs:
            return ""

        # if just one word in the list
        if len(strs) == 1:
            return strs[0]
        
        min_len = min(list(map(lambda s: len(s), strs)))
        end = False
        for i in range(min_len):
            for j in range(1, len(strs)):
                if strs[0][i] == strs[j][i]:
                    continue
                else:
                    end = True
                    break
            if end:
                break
            else:
                common_prefix.append(strs[0][i])
        
        return "".join(common_prefix)


if __name__ == "__main__":
    unittest.main()