left = lambda i: i * 2 +1
right = lambda i: i * 2 + 2
parent = lambda i: (i - 1) // 2

def less(x, y):
    return x < y

def greater(x, y):
    return x > y

def HeapSort(arr, cmp=greater):
    def heapify(arr, curr_pos, max_pos):
        m_pos, l, r = curr_pos, left(curr_pos), right(curr_pos)
        while l < max_pos:
            if l < max_pos and cmp(arr[l], arr[m_pos]):
                m_pos = l
            if r < max_pos and cmp(arr[r], arr[m_pos]):
                m_pos = r
            if m_pos != curr_pos:
                arr[m_pos], arr[curr_pos] = arr[curr_pos], arr[m_pos]
                curr_pos = m_pos
                l, r = left(curr_pos), right(curr_pos)
            else:
                break
    
    curr_pos = parent(len(arr)-1)
    max_pos = len(arr)
    while curr_pos >= 0:
        heapify(arr, curr_pos, max_pos)
        curr_pos -= 1

    # sort 
    while max_pos > 1:
        arr[0], arr[max_pos-1] = arr[max_pos-1], arr[0]
        max_pos -= 1
        heapify(arr, 0, max_pos)
    

arr = [3,2,1,4,10,6,7]
HeapSort(arr)
print(arr)