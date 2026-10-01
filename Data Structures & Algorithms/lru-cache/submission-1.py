class ListNode:

    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None
    
    def snip(self):
        r_node = self.next
        l_node = self.prev
        r_node.prev = l_node
        l_node.next = r_node

class Deque:

    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def push(self, node: ListNode):
        r_node = self.head.next
        self.head.next = node
        node.next = r_node
        node.prev = self.head
        r_node.prev = node
        self.size += 1
    
    def pop(self):
        pop_node = self.tail.prev
        l_node = self.tail.prev.prev
        self.tail.prev = l_node
        l_node.next = self.tail
        self.size -= 1
        return pop_node.val

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}
        self.q = Deque()

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        # clip node then push it
        node.snip()
        self.q.push(node)
        self.q.size -= 1 # track size appropriately
        return node.val[0]

    def put(self, key: int, value: int) -> None:
        if key not in self.map:
            node = ListNode((value, key))
            self.map[key] = node
            # push
            self.q.push(node)
        else:
            node = self.map[key]
            node.val = (value, key)
            node.snip()
            self.q.push(node)
            self.q.size -= 1
        if self.q.size > self.cap:
            pop_key = self.q.pop()[1]
            self.map.pop(pop_key)



