class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.lookup = {}
        

    def insert(self, val: int) -> bool:
        if val in self.lookup.keys():
            return False
        self.arr.append(val)
        self.lookup[val] = len(self.arr) - 1 # We store the index of the val by this eqn
        return True
        
        

    def remove(self, val: int) -> bool:
        if val not in self.lookup.keys():
            return False
        
        if self.lookup[val] == len(self.arr) - 1:
            del self.lookup[val]
            self.arr.pop()
            return True

        
        valIndex = self.lookup[val] # Get the index of the val variable

        self.arr[valIndex], self.arr[-1] = self.arr[-1], self.arr[valIndex] # Swap the positions of the last element in the arr with the val element

        del self.lookup[val] # del the index lookup of val

        
        self.lookup[self.arr[valIndex]] = valIndex # Assign the swapped element its new index on the index lookup map 
        
        self.arr.pop() # Pop the element to get constant lookup TC
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)
    
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()