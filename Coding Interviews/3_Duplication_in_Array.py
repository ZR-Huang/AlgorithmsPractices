import unittest

class TestSolutionMethods(unittest.TestCase):
    def test_duplicate(self):
        s = Solution()

        duplication = [-1]
        arr = [2,3,1,0,2,5,3]
        s.duplicate(arr, duplication)
        self.assertIn(duplication, [[2], [3]])

        duplication = [-1]
        arr = [0, 1, 3, 4, 5, 5]
        s.duplicate(arr, duplication)
        self.assertIn(duplication, [[5]])

        duplication = [-1]
        arr = [2,1,3,1,4]
        s.duplicate(arr, duplication)
        self.assertIn(duplication, [[1]])


class Solution:
    def duplicate(self, numbers, duplication):
        hashmap = [-1 for _ in range(len(numbers))]
        for n in numbers:
            if hashmap[n] != -1:
                duplication[0] = n
                break
            else:
                hashmap[n] = 1

        return True

if __name__ == '__main__':
    unittest.main()