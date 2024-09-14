# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        stack = []
        temp_head = head
        while temp_head:
            stack.append(temp_head)
            temp_head = temp_head.next
        
        n = len(stack)
        temp_head = head
        for _ in range(n // 2):
            temp = temp_head.next
            temp_head.next = stack.pop()
            temp_head.next.next = temp
            temp_head = temp_head.next.next
        
        if temp_head: temp_head.next = None


        