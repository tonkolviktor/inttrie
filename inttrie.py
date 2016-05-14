import math
class IntDecimalStorage:
    def __init__(self, number):
        self.number = number
    def __hash__(self):
        return hash(self.number)
    def __getitem__(self, index):
        if index >= len(self):
            raise IndexError("IntDecimalStorage index out of range")
        return (self.number / (10 ** index) ) % 10 # TODO make it char
    def __len__(self):
        return int(math.log10(self.number))+1

class IntDecimalTrie:
    def __init__(self):
        self.data = {}

    def insert(self, iterable, value):
        parent = self.data
        for i in iterable:
            if i in parent:
                parent = parent[i]
                continue
            parent[i] = {'_value': None}
            parent = parent[i]
        parent['_value'] = value

    def contains(self, iterable):
        parent = self.data
        for i in iterable:
            if i in parent:
                parent = parent[i]
                continue
            return False
        return parent['_value'] != None
    def __str__(self):
        return str(self.data)
