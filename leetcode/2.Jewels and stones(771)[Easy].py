class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        J_map = {}
        num_of_jewels = 0
        for item in J:
            J_map[item] = True
        
        for item in S:
            if item in J_map:
                num_of_jewels += 1
                
        return num_of_jewels
