from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        temp = []
        head_pointer = head
        ans = head
        while head_pointer != None:
            count += 1
            temp.append(head_pointer.val)
            head_pointer= head_pointer.next
            
        div = count // k
        for i in range(div):
            temp_group = temp[i*k:(i+1)*k]
            for j in range(k):
                head.val = temp_group[k - j - 1]
                head = head.next
        return ans

                
