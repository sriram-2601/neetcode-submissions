class MyHashSet:

    def __init__(self):
        self.hashSet = [False] * 1000001

    def add(self, key):
        self.hashSet[key] = True

    def remove(self, key):
        self.hashSet[key] = False

    def contains(self, key):
        return self.hashSet[key]