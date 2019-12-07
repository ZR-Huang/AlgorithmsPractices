import unittest

class TestSolutionMethods(unittest.TestCase):
    def test_firstUniqChar(self):
        s = Solution()
        # test the examples 
        string = "leetcode"
        self.assertEqual(s.firstUniqChar(string), 0)

        string = "loveleetcode"
        self.assertEqual(s.firstUniqChar(string), 2)

        # test the special cases
        string = "aabbccdd"
        self.assertEqual(s.firstUniqChar(string), -1)

        string = ""
        self.assertEqual(s.firstUniqChar(string), -1)

        string = "a"
        self.assertEqual(s.firstUniqChar(string), 0)

        # test the wrong answer cases
        string = "itwqbtcdprfsuprkrjkausiterybzncbmdvkgljxuekizvaivszowqtmrttiihervpncztuoljftlxybpgwnjb"
        self.assertEqual(s.firstUniqChar(string), 61)

    def test_firstUniqChar_v2(self):
        s = Solution()
        # test the examples 
        string = "leetcode"
        self.assertEqual(s.firstUniqChar_v2(string), 0)

        string = "loveleetcode"
        self.assertEqual(s.firstUniqChar_v2(string), 2)

        # test the special cases
        string = "aabbccdd"
        self.assertEqual(s.firstUniqChar_v2(string), -1)

        string = ""
        self.assertEqual(s.firstUniqChar_v2(string), -1)

        string = "a"
        self.assertEqual(s.firstUniqChar_v2(string), 0)

        # test the wrong answer cases
        string = "itwqbtcdprfsuprkrjkausiterybzncbmdvkgljxuekizvaivszowqtmrttiihervpncztuoljftlxybpgwnjb"
        self.assertEqual(s.firstUniqChar_v2(string), 61)


class Solution:
    def firstUniqChar(self, s)->int:
        if len(s) == 0:
            return -1
        
        if len(s) == 1:
            return 0
        
        hashmap = {}
        for index, c in enumerate(s):
            if c in hashmap:
                hashmap[c]['count'] += 1
            else:
                hashmap[c] = {'count':1, 'index':index}
        
        result = len(s)
        for _, value in hashmap.items():
            if value['count'] == 1 and value['index'] < result:
                result = value['index']
        
        if result == len(s):
            result = -1
        return result


    def firstUniqChar_v2(self, s)->int:
        """
        The `items()` method of the dict object has a low performance.
        """
        if len(s) == 0:
            return -1
        
        if len(s) == 1:
            return 0
        
        hashmap = {}
        for c in s:
            hashmap[c] = hashmap[c] + 1 if c in hashmap else 1
        
        for index, c in enumerate(s):
            if hashmap[c] == 1:
                return index
        
        return -1


if __name__ == "__main__":
    unittest.main()