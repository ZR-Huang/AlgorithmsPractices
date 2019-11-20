class Solution:
    def heightChecker(self, heights):
        
        def merge_sort(start, end):
            if start == end:
                return 
            
            mid = int((start + end)/2)

            merge_sort(start, mid)
            merge_sort(mid+1, end) 
            
            