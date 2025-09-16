from typing import Optional, List

import heapq
class ListNode:
    def __init__(self,val = 0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKlists(self, lists: List[Optional[ListNode]]) -> Optional[List[ListNode]]:
        heap = []
        def push_node(self, heap, node):
            if node:
                heapq.heappush(heap, (node.val, id(node),  node))
        for node in lists:
            push_node(heap, node)
        
        dummy = ListNode()
        current = dummy
        
        while heap:
            _, _, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            if node.next:
                push_node(heap, node.next)
        
        return dummy.next