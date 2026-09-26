import copy

# implement doubly-linked ListNode
class ListNode:

    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None

# implement Queue
class Dequeue:

    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def push(self, push_val):
        push_node = ListNode(push_val)
        push_node_front = self.head.next
        push_node_front.prev = push_node
        self.head.next = push_node
        push_node.prev = self.head
        push_node.next = push_node_front
        self.size += 1
    
    def pop(self):
        if self.head.next is self.tail:
            return None
        pop_node = self.tail.prev
        new_end = pop_node.prev
        new_end.next = self.tail
        self.tail.prev = new_end
        self.size -= 1
        return pop_node.val
    
    def peek(self):
        if self.head.next is self.tail:
            return None
        return self.tail.prev.val

class MyStack:

    def __init__(self):
        self.q = Dequeue()
        self.temp_q = Dequeue()

    def push(self, x: int) -> None:
        self.q.push(x)

    def pop(self) -> int:
        if self.q.size == 0:
            return None
        while self.q.size > 1:
            self.temp_q.push(self.q.pop())
        out = self.q.pop()
        self.q = self.temp_q
        self.temp_q = Dequeue()
        return out        

    def top(self) -> int:
        if self.q.size == 0:
            return None
        return self.q.head.next.val

    def empty(self) -> bool:
        return self.q.size == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()