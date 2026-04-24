class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
    
    def __repr__(self):
        return str(self.__dict__)


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.cache = {}
    
    def __str__(self):
        return str(self.__dict__)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._move_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._move_to_head(node)
        else:
            if len(self.cache) >= self.capacity:
                self._remove_tail()

            new_node = Node(key, value)
            self._add_to_head(new_node)
            self.cache[key] = new_node

    def _remove_node(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

    def _add_to_head(self, node):
        node.prev = None
        node.next = self.head

        if self.head:
            self.head.prev = node

        self.head = node

        if self.tail is None:
            self.tail = node

    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_to_head(node)

    def _remove_tail(self):
        if self.tail is None:
            return

        key_to_remove = self.tail.key
        self._remove_node(self.tail)
        del self.cache[key_to_remove]

obj = LRUCache(3)
print(obj)
print(obj.get(1))
obj.put(1,1)
print(obj.get(1))
obj.put(2,2)
print(obj.get(2))
obj.put(3,3)
print(obj.get(3))
obj.put(4,4)
print(obj.get(4))
print(obj)