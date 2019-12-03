import unittest

class TestSolutionMethods(unittest.TestCase):
    def test_find(self):
        s = Solution()
        matrix = [[1,2,8,9,10], [2,4,9,12,13], [4,7,10,13,14], [6,8,11,15,16]]
        
        target = 7
        self.assertEqual(s.find(target, matrix), True)

        target = 5
        self.assertEqual(s.find(target, matrix), False)


class Solution:
    def find(self, target, array):
        found = False
        if array:
            rows = len(array)
            columns = len(array[0])
            if rows > 0 and columns > 0:
                row = 0
                col = columns - 1
                while row < rows and col >=0:
                    if array[row][col] == target:
                        found = True
                        break
                    elif array[row][col] > target:
                        col -= 1
                    else:
                        row += 1
        
        return found


if __name__ == '__main__':
    unittest.main()