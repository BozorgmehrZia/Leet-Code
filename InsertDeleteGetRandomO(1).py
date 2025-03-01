# 380. Insert Delete GetRandom O(1)
# Implement the RandomizedSet class:
# RandomizedSet() Initializes the RandomizedSet object.
# bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
# int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
# You must implement the functions of the class such that each function works in average O(1) time complexity.
import random


class RandomizedSet:

    def __init__(self):
        # Store the index of each val in self.arr.
        self.indices = {}
        # Store all vals.
        self.arr = []

    def insert(self, val: int) -> bool:
        # Return False if val is already present as requested.
        if val in self.indices: return False

        # Append val to the array.
        # Store its index in the hashmap
        self.arr.append(val)
        self.indices[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        # Return False if val is not present as requested.
        if val not in self.indices: return False

        # Get the index of the val that needs to be removed.
        i = self.indices[val]

        # Update the index of arr[-1] in the indices.
        self.indices[self.arr[-1]] = i

        # Move the last element to the i th position.
        self.arr[i] = self.arr[-1]

        # remove the last element, and remove the index of val
        self.indices.pop(val)
        self.arr.pop()

        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)