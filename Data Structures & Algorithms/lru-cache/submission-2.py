class ListNode:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.tail = ListNode(-1, -1)
        self.head = ListNode(-1, -1)
        self.tail.next, self.head.prev = self.head, self.tail
        self.hm = {}
        self.size = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.hm:
            return -1
        node = self.hm[key]
        self.moveToTop(node, False)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = None
        # if new unused key
        if key not in self.hm:
            node = ListNode(key, value)
            self.hm[key] = node
            self.size += 1
            self.moveToTop(node, True)
        else:
            node = self.hm[key]
            node.val = value
            self.moveToTop(node, False)

        if self.size > self.capacity:
            self.hm.pop(self.tail.next.key)
            self.tail.next.next.prev = self.tail
            self.tail.next = self.tail.next.next
            self.size -= 1

    def moveToTop(self, node, new):
        if not new:
            node.prev.next = node.next
            node.next.prev = node.prev
        
        node.prev = self.head.prev
        node.next = self.head
        self.head.prev.next = node
        self.head.prev = node
