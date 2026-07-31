class ListNode:

    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0 # the greatest valid index is self.size - 1

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        if index > self.size // 2 - 1:
            # from tail
            curr = self.tail.prev
            for i in range(self.size - 1 - index):
                curr = curr.prev
        else:
            # from head
            curr = self.head.next
            for i in range(index):
                curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        new_head = ListNode(val)

        if self.head.next is self.tail:
            self.head.next = new_head
            self.tail.prev = new_head
            new_head.next = self.tail
            new_head.prev = self.head
        else:
            old_head = self.head.next
            self.head.next = new_head
            new_head.prev = self.head
            new_head.next = old_head
            old_head.prev = new_head
        
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_tail = ListNode(val)

        if self.tail.prev is self.head:
            self.tail.prev = new_tail
            self.head.next = new_tail
            new_tail.next = self.tail
            new_tail.prev = self.head
        else:
            old_tail = self.tail.prev
            self.tail.prev = new_tail
            new_tail.next = self.tail
            new_tail.prev = old_tail
            old_tail.next = new_tail
        
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        # current node at index gets moved up
        if index > self.size:
            return None
        if index == self.size:
            self.addAtTail(val)
            return None
        elif index == 0:
            self.addAtHead(val)
            return None
        if index > self.size // 2 - 1:
            # from tail
            curr = self.tail.prev
            for i in range(self.size - 1 - index):
                curr = curr.prev
        else:
            # from head
            curr = self.head.next
            for i in range(index):
                curr = curr.next
        left = curr.prev
        new = ListNode(val)
        left.next = new
        new.prev = left
        curr.prev = new
        new.next = curr
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return None
        if index > self.size // 2 - 1:
            # from tail
            curr = self.tail.prev
            for i in range(self.size - 1 - index):
                curr = curr.prev
        else:
            # from head
            curr = self.head.next
            for i in range(index):
                curr = curr.next
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)