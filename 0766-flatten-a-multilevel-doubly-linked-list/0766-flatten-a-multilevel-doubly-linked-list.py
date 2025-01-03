"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        if not head: return head
        stack = []
        cur = head
        while cur:
            if cur.child:
                if cur.next:
                    stack.append(cur.next)
                cur.next = cur.child
                cur.child.prev = cur
                cur.child = None
            elif not cur.next and stack:
                cur.next = stack.pop()
                cur.next.prev = cur

            cur = cur.next
                
        return head        