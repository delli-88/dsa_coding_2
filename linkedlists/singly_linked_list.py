class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return str(self.__dict__)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __repr__(self):
        return str(self.__dict__)

    def __str__(self):
        return " -> ".join(str(x) for x in self) + " -> None"

    def __len__(self):
        return self.length

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr.val
            curr = curr.next

    def is_empty(self):
        return self.length == 0

    def prepend(self, val):
        new_node = ListNode(val)

        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1

    def append(self, val):
        new_node = ListNode(val)

        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def insert(self, index, val):
        if index <= 0:
            self.prepend(val)
            return
        if index >= self.length:
            self.append(val)
            return

        new_node = ListNode(val)
        curr = self.head

        for _ in range(index - 1):
            curr = curr.next

        new_node.next = curr.next
        curr.next = new_node
        self.length += 1

    def delete_by_index(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")

        if index == 0:
            self.head = self.head.next
            if self.length == 1:
                self.tail = None
            self.length -= 1
            return

        curr = self.head
        for _ in range(index - 1):
            curr = curr.next

        to_delete = curr.next
        curr.next = to_delete.next

        if to_delete == self.tail:
            self.tail = curr

        self.length -= 1

    def delete_by_value(self, val):
        if self.is_empty():
            raise ValueError("List is empty")

        curr = self.head
        prev = None

        while curr:
            if curr.val == val:
                if prev is None:
                    self.head = curr.next
                    if self.head is None:
                        self.tail = None
                else:
                    prev.next = curr.next
                    if curr == self.tail:
                        self.tail = prev

                self.length -= 1
                return

            prev = curr
            curr = curr.next

        raise ValueError("Value not found")

    def find(self, val):
        curr = self.head
        index = 0

        while curr:
            if curr.val == val:
                return index
            curr = curr.next
            index += 1

        return -1

    def get(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")

        curr = self.head
        for _ in range(index):
            curr = curr.next

        return curr.val

    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def createLinkedList(self, head):

        if len(head)==0:
            return None
        
        for node in range(len(head)):
            self.append(head[node])
        
        return self.head

    def printLinkedList(self):
        return " -> ".join(str(x) for x in self) + " -> None"