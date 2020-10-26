import time
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.frequence_buckets = {}
        self.value_store = {}

    def get(self, key: int) -> int:
        value = -1
        if key in self.value_store:
            value, frequence = self.value_store[key]
            self.frequence_buckets[frequence].pop(key)
            frequence += 1
            if frequence not in self.frequence_buckets:
                self.frequence_buckets[frequence] = {}
            self.frequence_buckets[frequence][key] = time.time()
            self.value_store[key][1] += 1
        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return 
        if key not in self.value_store:
            if len(self.value_store) >= self.capacity:
                for freq in self.frequence_buckets:
                    if self.frequence_buckets[freq]:
                        nonempty_freq = freq
                        break
                discard_key, smallest_time = None, time.time()
                for _key, _time in self.frequence_buckets[nonempty_freq].items():
                    if _time < smallest_time:
                        discard_key = _key
                        smallest_time = _time
                self.frequence_buckets[nonempty_freq].pop(discard_key)
                self.value_store.pop(discard_key)

            self.value_store[key] = [value, 0]
            if 0 not in self.frequence_buckets:
                self.frequence_buckets[0] = {}
            self.frequence_buckets[0][key] = time.time()
        else:
            # 类似get操作
            self.value_store[key][0] = value
            value, frequence = self.value_store[key]
            self.frequence_buckets[frequence].pop(key)
            frequence += 1
            if frequence not in self.frequence_buckets:
                self.frequence_buckets[frequence] = {}
            self.frequence_buckets[frequence][key] = time.time()
            self.value_store[key][1] += 1

import collections
class Node:
    def __init__(self, key, val, pre=None, nex=None, freq=0):
        self.pre = pre
        self.nex = nex
        self.freq = freq
        self.val = val
        self.key = key
    
    def inseart(self, nex):
        nex.pre = self
        nex.nex = self.nex
        self.nex.pre = nex
        self.nex = nex

def create_linked_list():
    head = Node(0, 0)
    tail = Node(0, 0)
    head.nex = tail
    tail.pre = head
    return (head, tail)

class LFUCache_v2:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.minFreq = 0
        self.freqMap = collections.defaultdict(create_linked_list)
        self.keyMap = {}
    
    def delete(self, node):
        if node.pre:
            node.pre.nex = node.nex
            node.nex.pre = node.pre
            if node.pre is self.freqMap[node.freq][0] and node.nex is self.freqMap[node.freq][-1]:
                self.freqMap.pop(node.freq)
            return node.key
    
    def increase(self, node):
        node.freq += 1
        self.delete(node)
        self.freqMap[node.freq][-1].pre.inseart(node)
        if node.freq == 1:
            self.minFreq = 1
        elif self.minFreq == node.freq - 1:
            head, tail = self.freqMap[node.freq - 1]
            if head.nex is tail:
                self.minFreq = node.freq
    
    def get(self, key):
        if key in self.keyMap:
            self.increase(self.keyMap[key])
            return self.keyMap[key].val
        return -1

    def put(self, key:int, value:int)->None:
        if self.capacity != 0:
            if key in self.keyMap:
                node = self.keyMap[key]
                node.val = value
            else:
                node = Node(key, value)
                self.keyMap[key] = node
                self.size += 1
            if self.size > self.capacity:
                self.size -= 1
                deleted = self.delete(self.freqMap[self.minFreq][0].nex)
                self.keyMap.pop(deleted)
            self.increase(node)

# Your LFUCache object will be instantiated and called as such:
cache = LFUCache(2)
cache.get(2)
cache.put(2,6)
cache.get(1)
cache.put(1,5)
cache.put(1,2)
cache.get(1)
cache.get(2)