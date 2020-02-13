class Solution:
    '''
    Computing the subset of the array can be considered as the selection of 
    every element of the array. Thus, the DFS algorithm is used to 
    search all the possible combinations. This method also called 
    backtrack algorithm.
    '''
    def subsets(self, nums):
        result = []
        n = len(nums)

        def select_elem(i, n, selected_list):
            result.append(selected_list)
            for j in range(i, n):
                select_elem(j+1, n, selected_list+[nums[j]])

        select_elem(0, n, [])
        return result

print(Solution().subsets([1,2,3]))