# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        temp_list = head
        stack = []
        while temp_list:
            stack.append(temp_list)
            temp_list = temp_list.next
        
        n = len(stack)
        temp_list = head
        for _ in range(n // 2):
            temp = temp_list.next
            temp_list.next = stack.pop()
            temp_list.next.next = temp
            temp_list = temp
            
        
        if temp_list:
            temp_list.next = None

        