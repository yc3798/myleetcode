# Design a HashMap without using any built-in hash table libraries.

# To be specific, your design should include these functions:

# put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
# get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.


# INDEX INTO THE ARRAY 
# keys[i] = k --> values[k] = value

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values = []
        self.keys = [] # store "index into self.values" for key i
        self.index = -1 # track the largest index in values


    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        print("Command: put ", key, value)
        if key > len(self.keys)-1:
            # allocate more space for keys
            self.keys.extend([-1 for i in range(key - (len(self.keys)-1))])

        if self.keys[key] != -1: # key already inserted, upsert
            self.values[self.keys[key]] = value 
            print("Upserted value: ", self.values[self.keys[key]])

        else: # key not present, insert at index + 1
            self.keys[key] = self.index + 1
            self.values.append(value)
            self.index += 1
            print("Inserted value: ",  self.values[self.index])
            # print("Total number of keys(index): ",  self.index + 1)

        
    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        print("Command: get key ", key)
        if key >= len(self.keys) or self.keys[key] == -1:
            print("key ", key, " not present!")
            return -1
        if self.values[self.keys[key]] == "deleted":
            print("key ", key, " was deleted.")
            return -1
       
        else:
            print(key, ":", self.values[self.keys[key]])
            return self.values[self.keys[key]]


    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        print("Command: remove key ", key)
        if key < len(self.keys) and self.keys[key] != -1:
            self.values[self.keys[key]] = "deleted"
        else:
            print("key ", key, " not present")
    
    def printHashMap(self) -> None:
        for k in self.keys:
            if self.keys[k] != -1:
                print("key: ", k, "value: ", self.values[self.keys[k]])



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

hashMap = MyHashMap()
hashMap.put(1, 1)         
hashMap.put(2, 2)  
hashMap.get(2)        
hashMap.get(1)           # returns 1
hashMap.get(3)           # returns -1 (not found)
# hashMap.printHashMap()
hashMap.put(2, 1)         # update the existing value
hashMap.get(2);            # returns 1 
hashMap.remove(2);         # remove the mapping for 2
hashMap.get(2);            # returns -1 (not found) 