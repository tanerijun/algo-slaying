from typing import Optional

# Initial version: a bit convoluted

# class Node:
#     def __init__(
#         self,
#         value: tuple[int, int] = (-1, -1),  # contains (key, value)
#         prev: Optional["Node"] = None,
#         next: Optional["Node"] = None,
#     ):
#         self.value = value
#         self.prev = prev
#         self.next = next

# class LRUCache:
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.map = {}  # map key to Node
#         self.leftDummy = Node()  # point right to least recently used
#         self.rightDummy = Node()  # point left to most recently used
#         self.leftDummy.next = self.rightDummy
#         self.rightDummy.prev = self.leftDummy

#     def _insert_most_recent(self, node: Node) -> None:
#         node.prev = self.rightDummy.prev
#         node.next = self.rightDummy
#         self.rightDummy.prev.next = node
#         self.rightDummy.prev = node

#     def _delete_node(self, node: Node) -> None:
#         node.prev.next = node.next
#         node.next.prev = node.prev
#         node.prev = None
#         node.next = None

#     def _update_most_recent(self, node: Node) -> None:
#         self._delete_node(node)
#         self._insert_most_recent(node)

#     def get(self, key: int) -> int:
#         if not key in self.map:
#             return -1

#         node = self.map[key]
#         self._update_most_recent(node)
#         return node.value[1]

#     def put(self, key: int, value: int) -> None:
#         if key in self.map:
#             node = self.map[key]
#             node.value = (key, value)
#             self._update_most_recent(node)
#             return

#         if len(self.map) + 1 > self.capacity:
#             node = self.leftDummy.next
#             self._delete_node(node)
#             del self.map[node.value[0]]

#         node = Node((key, value))
#         self.map[key] = node
#         self._insert_most_recent(node)

#     def print_cache(self) -> str:
#         res = []
#         for k, v in self.map.items():
#             res.append(f"{k} => {v.value[1]}")

#         return ", ".join(res)


# Simplified and cleaned
# class Node:
#     def __init__(
#         self,
#         key: int,
#         val: int,
#         prev: Optional["Node"] = None,
#         next: Optional["Node"] = None,
#     ):
#         self.key = key
#         self.val = val
#         self.prev = prev
#         self.next = next


# class LRUCache:
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.map = {}  # map key to Node
#         self.leftDummy = Node(-1, -1)  # points right to least recently used node
#         self.rightDummy = Node(-1, -1)  # points left to most recently used node
#         self.leftDummy.next = self.rightDummy
#         self.rightDummy.prev = self.leftDummy

#     def _insert(self, node: Node):
#         node.next = self.rightDummy
#         node.prev = self.rightDummy.prev
#         self.rightDummy.prev.next = node
#         self.rightDummy.prev = node

#     def _delete(self, node: Node):
#         node.prev.next = node.next
#         node.next.prev = node.prev

#     def get(self, key: int) -> int:
#         if not key in self.map:
#             return -1

#         node = self.map[key]
#         self._delete(node)
#         self._insert(node)
#         return node.val

#     def put(self, key: int, value: int) -> None:
#         if key in self.map:
#             node = self.map[key]
#             self._delete(node)

#         node = Node(key, value)
#         self.map[key] = node
#         self._insert(node)

#         if len(self.map) > self.capacity:
#             lru = self.leftDummy.next
#             self._delete(lru)
#             del self.map[lru.key]

# Even cleaner: remove and insert also handles changes to map


class Node:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.map = {}
        self.capacity = capacity
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.remove(node)
            self.insert(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(self.map[key])
        if len(self.map) == self.capacity:
            self.remove(self.tail.prev)
        self.insert(Node(key, value))

    def remove(self, node):
        del self.map[node.key]
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        self.map[node.key] = node
        node.next = self.head.next
        node.next.prev = node
        node.prev = self.head
        self.head.next = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# For testing purposes
# res = []
# cache = LRUCache(2)
# res.append(cache.put(2, 1))
# res.append(cache.put(1, 1))
# res.append(cache.put(2, 3))
# res.append(cache.put(4, 1))
# res.append(cache.print_cache())
# res.append(cache.get(1))
# res.append(cache.get(2))

# for r in res:
#     print(r)
