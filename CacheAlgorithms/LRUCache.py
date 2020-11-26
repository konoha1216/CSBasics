from CacheAlgorithms.DoubleLinkedList import DoubleLinkedList, Node

class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}
        self.list = DoubleLinkedList(self.capacity)

    def get(self, key):
        if key in self.map:
            node = self.map.get(key)
            self.list.remove(node)
            self.list.appendHead(node)
            return "this is the value of the input key: "+ str(node.value)
        else:
            return "don't contain this key: "+str(key)

    def put(self, key, value):
        if key in self.map:
            node = self.map.get(key)
            self.list.remove(node)
            node.value = value
            self.list.appendHead(node)
        else:
            node = Node(key, value)
            # cache is full
            if self.list.size == self.list.capacity:
                oldNode = self.list.remove()
                self.map.pop(oldNode.key)
                self.list.appendHead(node)
                self.map[key] = node
            # cache not full
            else:
                self.list.appendHead(node)
                self.map[key] = node
    def print(self):
        self.list.print()


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(2,2)
    cache.print()
    cache.put(1,1)
    cache.print()
    cache.put(3,3)
    cache.print()
    print(cache.get(1))
    cache.print()
    print(cache.get(2))
    cache.print()
    print(cache.get(3))
    cache.print()