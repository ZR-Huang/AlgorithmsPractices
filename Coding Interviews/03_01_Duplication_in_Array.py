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

    def test_duplicate_v2(self):
        s = Solution()

        duplication = [-1]
        arr = [2,3,1,0,2,5,3]
        s.duplicate_v2(arr, duplication)
        self.assertIn(duplication, [[2], [3]])

        duplication = [-1]
        arr = [0, 1, 3, 4, 5, 5]
        s.duplicate_v2(arr, duplication)
        self.assertIn(duplication, [[5]])

        duplication = [-1]
        arr = [2,1,3,1,4]
        s.duplicate_v2(arr, duplication)
        self.assertIn(duplication, [[1]])

class Solution:
    def duplicate(self, numbers, duplication):
        """
        If there are duplications in the numbers, 
        store any of them in the duplication[0] and 
        return True. Otherwise, return False.

        This time and space complexity are O(n) and O(n) respectively.
        """
        # create a hashmap for the numbers array
        hashmap = [-1 for _ in range(len(numbers))]
        for n in numbers:
            if hashmap[n] != -1:
                duplication[0] = n
                break
            else:
                hashmap[n] = 1

        return True

    def duplicate_v2(self, numbers, duplication):
        """
        We note the numbers in the array range from 0~n-1.
        If there is no duplication, the number i will be arranged 
        at the index i after sorting the array.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        if len(numbers) <= 0:
            return False
        
        for num in numbers:
            if num < 0 or num > len(numbers)-1:
                return False
        
        # Step 1. Traversal the array
        for i in range(len(numbers)):
            while numbers[i] != i:
                # when the numbers not in the right position,
                # we check the numbers[numbers[i]]
                if numbers[i] == numbers[numbers[i]]:
                    duplication[0] = numbers[i]
                    return True
                # Step 2. swap numbers[i] and numbers[numbers[i]] to 
                # arrange the num into the right position
                tmp = numbers[i]
                numbers[i] = numbers[numbers[i]]
                numbers[tmp] = tmp

        return False


if __name__ == '__main__':
    unittest.main()