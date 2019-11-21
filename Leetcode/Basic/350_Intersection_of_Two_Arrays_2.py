class Solution:
    def intersect(self, nums1, nums2):
        '''
        1. sort the two arrays.
        2. compare the elements in the two arrays
        '''
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)

        result = []

        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        
        return result

print(Solution().intersect([4,9,5], [9,4,9,8,4]))