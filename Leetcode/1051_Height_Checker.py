class Solution:
    def heightChecker(self, heights):
        '''
        sort the heights array and compare the new and the old.
        '''
        # sorted_heights = sorted(heights)
        old_heights = heights[:]
        # self.heap_sort(heights)
        heights = self.count_sort(heights)
        print(heights)
        result = 0 
        for old, new in zip(old_heights, heights):
            if old != new:
                result += 1
        return result


    def heap_sort(self, array):
        for i in range(int((len(array)-2)/2), -1, -1):
            self.down_adjust(array, i, len(array))

        for i in range(len(array)-1, 0, -1):
            array[i], array[0] = array[0], array[i]
            self.down_adjust(array, 0, i)
        

    def down_adjust(self, array, parent_index, length):
        temp = array[parent_index]

        child_index = 2*parent_index + 1

        while child_index < length:
            if child_index + 1< length and array[child_index+1] > array[child_index]:
                child_index += 1
            
            if temp > array[child_index]:
                break
            
            array[parent_index] = array[child_index]
            parent_index = child_index
            child_index = 2*child_index + 1
        
        array[parent_index] = temp

    
    def count_sort(self, array):
        max_value, min_value = max(array), min(array)
        d = max_value - min_value
        count_array = [ 0 for _ in range(d+1)]
        result = [0 for _ in range(len(array))]

        for elem in array:
            count_array[elem-min_value] += 1
        
        for i in range(1, len(count_array)):
            count_array[i] += count_array[i-1]
        
        for i in range(len(array)-1, -1, -1):
            result[count_array[array[i]-min_value]-1] = array[i]
            count_array[array[i]-min_value] -= 1
        
        return result


print(Solution().heightChecker([1,1,4,2,1,3]))
            
