"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        cur = head
        nodeMap = {}

        while cur:
            nodeMap[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            nodeMap[cur].next = nodeMap.get(cur.next)
            nodeMap[cur].random = nodeMap.get(cur.random)
            cur = cur.next

        return nodeMap[head]        
            