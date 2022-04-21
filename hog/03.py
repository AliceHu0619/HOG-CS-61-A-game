class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []

    def add(self, key: int) -> None:
        if not self.data:
            self.data.append(key)
        else:
            if not self.contains(key):
                insort(self.data, key)

    def remove(self, key: int) -> None:
        if self.data:
            idx = bisect_left(self.data, key)
            if idx < len(self.data) and self.data[idx] == key:
                self.data.pop(idx)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if not self.data:
            return False
        idx = bisect_left(self.data, key)
        return self.data[idx] == key if idx < len(self.data) else False
