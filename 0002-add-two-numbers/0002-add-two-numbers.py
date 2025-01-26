# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # def reverse(head):
        #     prev = None
        #     while head:
        #         temp = head.next
        #         head.next = prev
        #         prev = head
        #         head = temp
        #     return prev
        
        # l1 = reverse(l1)
        # l2 = reverse(l2)

        temp = ListNode()
        res = temp
        carry = 0
        while l1 and l2:
            curVal = l1.val + l2.val + carry
            if curVal >= 10:
                carry = 1
                curVal = curVal % 10
            else:
                carry = 0
            temp.next = ListNode(curVal)
            temp = temp.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            curVal = carry + l1.val
            carry = 0
            if curVal >= 10:
                carry = 1
                curVal = curVal % 10
            else:
                carry = 0
            l1 = l1.next
            temp.next = ListNode(curVal)
            temp = temp.next
        while l2:
            curVal = carry + l2.val
            carry = 0
            if curVal >= 10:
                carry = 1
                curVal = curVal % 10
            else:
                carry = 0
            l2 = l2.next
            temp.next = ListNode(curVal)
            temp = temp.next
        
        if carry == 1:
            temp.next = ListNode(carry)
            temp = temp.next
        
        return res.next
        
        

