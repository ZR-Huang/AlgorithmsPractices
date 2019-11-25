class DictionaryOrder():
    def next_permutation(self, nums):
        '''
        nums: list[int] e.g. [1,2,3]
        '''
        # step 1. find the bound of reversed zone
        index = self.findTransferPoint(nums)
        if index == 0:
            return 
        
        # step 2. exchange the previous digit with the digit 
        # which is greater than it and is the smallest in the reversed
        # zone.
        self.exchangeHead(nums, index)
        # step 3. adjust the reverse order to the order
        self.reverse(nums, index)
        return nums
        

    def findTransferPoint(self, nums):
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                return i
        return 0

    def exchangeHead(self, nums, index):
        for i in range(len(nums)-1, 0, -1):
            if nums[index-1] < nums[i]:
                nums[index-1], nums[i] = nums[i], nums[index-1]
                break
        

    def reverse(self, nums, index):
        i, j = index, len(nums)-1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


print(DictionaryOrder().next_permutation([1,2,3,5,4]))