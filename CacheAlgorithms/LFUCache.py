from CacheAlgorithms.DoubleLinkedList import DoubleLinkedList, Node

class LFUNode(Node):
    def __init__(self, key, value):
        self.freq = 0
        super(LFUNode, self).__init__(key, value)

class LFUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}
        # key: frequency, value: the double-linked list of the frequency
        self.freq_map = {}
        self.size = 0

    # update the frequency of one node
    def __updateFreq(self, node):
        freq = node.freq

        # remove the node from the former (freq, double-linked list) map
        node = self.freq_map[freq].remove(node)
        if self.freq_map[freq].size==0:
            del self.freq_map[freq]

        # update the (freq, double-linked list)map by the node with its new freq
        freq += 1
        node.freq = freq
        if freq not in self.freq_map:
            self.freq_map[freq] = DoubleLinkedList()
        self.freq_map[freq].appendTail(node)

    def get(self, key):
        if key not in self.map:
            return "don't contain this key: "+str(key)
        node = self.map.get(key)
        self.__updateFreq(node)
        return "this is the value of the input key: " + str(node.value)

    def put(self, key, value):
        if self.capacity == 0:
            return

        # cache already has the key 缓存命中
        if key in self.map:
            node = self.map.get(key)
            node.value = value
            self.__updateFreq(node)

        # cache not has the key 缓存没有命中
        else:
            # remove the node with the least freq from the (key-node)map and the (freq, double-linked list) map
            if self.capacity == self.size:
                minFreq = min(self.freq_map)
                node = self.freq_map[minFreq].pop()
                del self.map[node.key]
                self.size -= 1
            node = LFUNode(key, value)
            node.freq = 1
            self.map[key] = node
            # 前面删完节点后没有频率为1的节点时得新建一个频率为1对应的双向链表
            if node.freq not in self.freq_map:
                self.freq_map[node.freq] = DoubleLinkedList()
            node = self.freq_map[node.freq].appendTail(node)
            self.size += 1

    def print(self):
        print('**********')
        for k, v in self.freq_map.items():
            print('frequency = %d' % k)
            self.freq_map[k].print()
        print('**********')
        print()

if __name__ == '__main__':
    cache = LFUCache(2)
    cache.put(1,1)
    cache.print()
    cache.put(2,2)
    cache.print()
    print(cache.get(1))
    cache.print()
    cache.put(3,3)
    cache.print()
    print(cache.get(2))
    cache.print()
    print(cache.get(3))
    cache.print()
    cache.put(4,4)
    cache.print()
    print(cache.get(1))
    cache.print()
    print(cache.get(3))
    cache.print()
    print(cache.get(4))
    cache.print()




