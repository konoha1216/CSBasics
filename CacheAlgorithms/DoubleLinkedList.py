class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        val = '{%d: %d}' % (self.key, self.value)
        return val

    def __repr__(self):
        val = '{%d: %d}' % (self.key, self.value)
        return val

class DoubleLinkedList:
    def __init__(self, capacity = 0xffff):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.size = 0

    # 从头部添加节点 add a node at the head
    def _addHead(self, node):
        if not self.head:
            self.head = node
            self.tail = node
            self.head.next = None
            self.head.prev = None
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
            self.head.prev = None
        self.size += 1
        return node

    # 从尾部添加节点 add a node at the tail
    def _addTail(self, node):
        if not self.tail:
            self.tail = node
            self.head = node
            self.tail.next = None
            self.tail.prev = None
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            self.tail.next = None
        self.size += 1
        return node

    # 删除尾部节点 remove the tail node
    def _removeTail(self):
        if not self.tail:
            return
        node = self.tail
        if node.prev:
            self.tail = node.prev
            self.tail.next = None
        else:
            self.tail = self.head = None
        self.size -= 1
        return node
    # 删除头部节点 remove the head node
    def _removeHead(self):
        if not self.head:
            return
        node = self.head
        if node.next:
            self.head = node.next
            self.head.prev = None
        else:
            self.head = self.tail = None
        self.size -= 1
        return node

    # 任意节点删除 remove a node
    def _removeNode(self, node):
        if not node:
            node = self.tail
        if node == self.tail:
            self._removeTail()
        elif node == self.head:
            self._removeHead()
        else:
            node.next.prev = node.prev
            node.prev.next = node.next
            self.size -= 1
        return node

    # 封装函数 api function
    # 弹出首个节点 pop
    def pop(self):
        return self._removeHead()

    # 头部添加节点 add at head
    def appendHead(self, node):
        return self._addHead(node)

    # 尾部添加节点 add at tail
    def appendTail(self, node):
        return self._addTail(node)

    # 删除节点 remove
    def remove(self, node=None):
        return self._removeNode(node)

    # 打印当前链表
    def print(self):
        p = self.head
        line = ''
        while p:
            line += '%s' % p
            p = p.next
            if p:
                line += '=>'
        print(line)


if __name__ == '__main__':
    l = DoubleLinkedList(10)
    nodes = []
    for i in range(10):
        nodes.append(Node(i, i))

    l.appendTail(nodes[0])
    l.print()
    l.appendTail(nodes[1])
    l.print()
    l.pop()
    l.print()
    l.appendTail(nodes[2])
    l.print()
    l.appendHead(nodes[3])
    l.print()
    l.appendTail(nodes[4])
    l.print()
    l.remove(nodes[2])
    l.print()
    l.remove()
    l.print()
