import unittest

class TestSolutionMethods(unittest.TestCase):

    def test_reverseString(self):
        s = Solution()

        input_s = ["h","e","l","l","o"]
        s.reverseString(input_s)
        self.assertEqual(input_s, ["o","l","l","e","h"])

        input_s = ["H","a","n","n","a","h"]
        s.reverseString(input_s)
        self.assertEqual(input_s, ["h","a","n","n","a","H"])

        # test for special input
        input_s = []
        s.reverseString(input_s)
        self.assertEqual(input_s, [])

        input_s = ['A']
        s.reverseString(input_s)
        self.assertEqual(input_s, ['A'])



class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length = len(s)
        if length < 2:
            return
        
        for i in range((length+1) // 2):
            s[i], s[~i] = s[~i], s[i]
        
        return


if __name__ == '__main__':
    unittest.main()
    