left = lambda i: i*2+1
right = lambda i: i*2+2
parent = lambda i: (i-1) // 2

def less(x, y):
    return x < y

def greater(x, y):
    return x > y

class Heap():
    def __init__(self, array=None, IS_MIN_HEAP=True):
        self._heap = []
        self._cmp = less if IS_MIN_HEAP else greater
        if array:
            self._heap = list(array)
            self.build_heap()

    @property
    def top(self):
        return self._heap[0]

    @property
    def heapsize(self):
        return len(self._heap)

    def __swap__(self, i, j):
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    def build_heap(self):
        '''
        Start from the parent of the last leaf nodes.
        '''
        curr_pos = parent(self.heapsize-1)
        max_pos = self.heapsize
        # maintain heap property for every node except leaves
        while curr_pos >= 0:
            self.heapify(curr_pos, max_pos)
            curr_pos -= 1

    def heapify(self, curr_pos, max_pos):
        '''
        transform the subtree rooted with curr_pos into heap
        '''
        m_pos = curr_pos
        l, r = left(curr_pos), right(curr_pos)
        while l < max_pos:
            if l < max_pos and self._cmp(self._heap[l], self._heap[m_pos]):
                m_pos = l
            if r < max_pos and self._cmp(self._heap[r], self._heap[m_pos]):
                m_pos = r
            if m_pos != curr_pos:
                self.__swap__(m_pos, curr_pos)
                curr_pos = m_pos
                l, r = left(curr_pos), right(curr_pos)
            else:
                break
    
    def push(self, value):
        '''
        insert a node into last position and 
        exchange it to the appropriate position to keep heap property.
        '''
        self._heap.append(value)
        curr_pos = self.heapsize -1
        parent_pos = parent(curr_pos)
        while curr_pos > 0 and self._cmp(self._heap[curr_pos], self._heap[parent_pos]):
            self.__swap__(curr_pos, parent_pos)
            curr_pos, parent_pos = parent_pos, parent(parent_pos)
        self.heapify(0, self.heapsize)
    
    def pop(self):
        '''
        exchange the root node and the last node 
        and maintain the heap from the root.
        '''
        self.__swap__(0, -1)
        value = self._heap.pop()
        self.heapify(0, self.heapsize)
        return value

    def show(self):
        print(self._heap)


arr = [5,3,2,6,7,1,10]
maxh = Heap(arr, False)
minh = Heap(arr)
maxh.show()
minh.show()

maxh.push(-1)
minh.push(-1)
maxh.show()
minh.show()

maxh.pop()
minh.pop()
maxh.show()
minh.show()
