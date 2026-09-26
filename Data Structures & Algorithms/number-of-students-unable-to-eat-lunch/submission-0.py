class ListNode():
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None

class Queue():
    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def enqueue(self, enqueue_val):
        enqueue_node = ListNode(enqueue_val)
        if self.head.next is self.tail: # empty queue
            self.head.next = enqueue_node
            self.tail.prev = enqueue_node
            enqueue_node.prev = self.head
            enqueue_node.next = self.tail
        else: # nonempty
            old_enqueue = self.head.next
            self.head.next = enqueue_node
            old_enqueue.prev = enqueue_node
            enqueue_node.next = old_enqueue
            enqueue_node.prev = self.head
        self.size += 1
    
    def dequeue(self):
        if self.head.next is self.tail: # empty queue
            return None
        else:
            dequeue_node = self.tail.prev
            new_dequeue = dequeue_node.prev
            new_dequeue.next = self.tail
            self.tail.prev = new_dequeue
            self.size -= 1
            return dequeue_node.val
    
    def peek(self):
        if self.head.next is self.tail: # empty queue
            return None
        else:
            return self.tail.prev.val
    

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        # Build queue
        lunch_line = Queue()
        for s in students:
            lunch_line.enqueue(s)

        # Simulate lunch line
        n_students = len(students)
        n_rotations = 0

        sandwiches = sandwiches[::-1]

        while n_rotations < n_students:
            if sandwiches[-1] == lunch_line.peek():
                sandwiches.pop()
                lunch_line.dequeue()
                n_students -= 1
                n_rotations = 0
            else:
                lunch_line.enqueue(lunch_line.dequeue())
                n_rotations += 1
        
        return lunch_line.size





        