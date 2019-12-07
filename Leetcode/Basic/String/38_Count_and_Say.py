import unittest


class TestSolutionMethods(unittest.TestCase):
    def test_countAndSay(self):
        s = Solution()

        self.assertEqual(s.countAndSay(1), '1')
        self.assertEqual(s.countAndSay(2), '11')
        self.assertEqual(s.countAndSay(3), '21')
        self.assertEqual(s.countAndSay(4), '1211')
        self.assertEqual(s.countAndSay(5), '111221')



class Solution:
    def countAndSay(self, n: int)->str:
        if n == 1:
            return "1"
        
        _current = ["1", '1']
        for _ in range(n-2):
            i, j = 0, 0  # Use the double pointers method
            _new = []
            while j<len(_current):
                if j == len(_current) -1:
                    _new += [str(j-i+1), _current[i]]
                    break
                if _current[j] == _current[j+1]:
                    j+=1
                    continue
                else:
                    _new += [str(j-i+1), _current[i]]
                    j += 1
                    i = j

            _current = _new     
        
        return ''.join(_current)
        

if __name__ == "__main__":
    unittest.main()