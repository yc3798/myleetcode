import random
class RandomizedSet:
    # we need a list and a dictionary
    # self.d = {} # value, index
    # self.vals = [] # vals
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {} # value, index
        self.vals = [] # vals


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.d:
            self.d[val] = len(self.vals)
            self.vals.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        Pop the last item and replace the "val" in self.vals
        """
        if val in self.d:
            pos = self.d[val] # current pos of val
            if pos == len(self.vals) - 1: # current is at last
                self.vals.pop()
                del self.d[val] 
                return True                

            tempval = self.vals.pop(-1) # pop the last item 
            self.vals[pos] = tempval
            self.d[tempval] = pos # update the position
            del self.d[val] # remove entry in d
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        if len(self.vals) > 0:
            n = random.randint(0, len(self.vals) - 1)
            return self.vals[n]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


# // Init an empty set.
# RandomizedSet randomSet = new RandomizedSet();

# // Inserts 1 to the set. Returns true as 1 was inserted successfully.
# randomSet.insert(1);

# // Returns false as 2 does not exist in the set.
# randomSet.remove(2);

# // Inserts 2 to the set, returns true. Set now contains [1,2].
# randomSet.insert(2);

# // getRandom should return either 1 or 2 randomly.
# randomSet.getRandom();

# // Removes 1 from the set, returns true. Set now contains [2].
# randomSet.remove(1);

# // 2 was already in the set, so return false.
# randomSet.insert(2);

# // Since 2 is the only number in the set, getRandom always return 2.
# randomSet.getRandom();