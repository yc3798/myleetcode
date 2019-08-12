class LRUCache:
    # Approach 1: use a list to record "least used"
    #
    def __init__(self, capacity: int):
        self.usage = []
        self.capacity = capacity
        self.cache = {}
        self.currsize = 0

    def get(self, key: int) -> int:
        """
        Get value of the key if existed in cache, otherwise return -1
        """

        if key in self.cache:
            self.usage.remove(key)
            self.usage.append(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        """
        Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
        """
        if key in self.cache:
            self.cache[key] = value
            self.usage.remove(key)
            self.usage.append(key)
        else:
            if self.currsize == self.capacity:
                rm = self.usage.pop(0)  # pop the first one, which is least used item
                self.cache.pop(rm)
                self.currsize -= 1
            self.cache[key] = value
            self.currsize += 1
            self.usage.append(key)





            # Your LRUCache object will be instantiated and called as such:
            # obj = LRUCache(capacity)
            # param_1 = obj.get(key)
            # obj.put(key,value)