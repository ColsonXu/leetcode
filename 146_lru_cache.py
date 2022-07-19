class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hashmap = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left


    def append(self, node):
        node.prev = self.right.prev
        node.next = self.right
        node.prev.next = node
        node.next.prev = node


    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
            self.append(self.hashmap[key])
            return self.hashmap[key].val
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
        self.hashmap[key] = Node(key, value)
        self.append(self.hashmap[key])
        if len(self.hashmap) > self.cap:
            rm = self.left.next
            self.remove(rm)
            del self.hashmap[rm.key]
