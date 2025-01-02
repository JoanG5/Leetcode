class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = Node(0, 0)  # Dummy head
        self.tail = Node(0, 0)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
        node.prev = node.next = None
    
    def add_to_front(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def pop_tail(self):
        tail_node = self.tail.prev
        self.remove(tail_node)
        return tail_node


class LRUCache(object):

    def __init__(self, capacity):
        self.cache = {}
        self.llist = LinkedList()
        self.size = 0
        self.capacity = capacity
        

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.llist.remove(node)
            self.llist.add_to_front(node)
            return node.val
        return -1
        

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.llist.remove(node)
            self.llist.add_to_front(node)
        else:
            if self.size == self.capacity:
                tail = self.llist.pop_tail()
                del self.cache[tail.key]
                self.size -= 1
            new_node = Node(key, value)
            self.llist.add_to_front(new_node)
            self.cache[key] = new_node
            self.size += 1


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)