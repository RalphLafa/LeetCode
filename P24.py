from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        ans = head
        while head and head.next:
            prev = head
            cur = prev.next
            adj = cur.next
            
            cur.next = prev
            prev = cur
            

            head = adj

    
        return ans  