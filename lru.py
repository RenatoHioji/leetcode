class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev, self.next = None, None
    

class Solution:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        
        self.left.next = self.right
        self.right.prev = self.left
        
    def remove(self, node):
        prev = node.prev
        _next = node.next
        
        prev.next = _next
        _next.prev = prev
    
    def insert(self, node):
        prev = self.left
        _next = self.left.next
        prev.next = node
        _next.prev = node
        
        node.next = _next
        node.prev = prev
        
    def get(self, key: int):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key:int, value: int):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.capacity:
            lru = self.right.prev
            self.remove(lru)
            del self.cache[lru.key]
        