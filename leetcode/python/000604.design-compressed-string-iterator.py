class StringIterator:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def __init__(self, compressedString: str):
        self.data = []

        i = 0
        while i < len(compressedString):
            ch = compressedString[i]
            i += 1

            num_start = i
            while i < len(compressedString) and compressedString[i].isdigit():
                i += 1
            count = int(compressedString[num_start:i])

            self.data.append([ch, count])

        self.idx = 0

    # Time complexity: O(1)
    # Space complexity: O(1)
    def next(self) -> str:
        if self.hasNext():
            ch = self.data[self.idx][0]
            self.data[self.idx][1] -= 1
            if self.data[self.idx][1] == 0:
                self.idx += 1
            return ch
        else:
            return " "

    # Time complexity: O(1)
    # Space complexity: O(1)
    def hasNext(self) -> bool:
        return self.idx != len(self.data)


class StringIterator2:
    # Time complexity: O(1)
    # Space complexity: O(1)
    def __init__(self, compressedString: str):
        self.data = compressedString
        self.idx = 0
        self.ch = " "
        self.count = 0

    # Time complexity: O(1)
    # Space complexity: O(1)
    def next(self) -> str:
        if not self.hasNext():
            return " "

        if self.count == 0:
            self.ch = self.data[self.idx]
            self.idx += 1

            while self.idx < len(self.data) and self.data[self.idx].isdigit():
                self.count = self.count * 10 + int(self.data[self.idx])
                self.idx += 1

        self.count -= 1
        return self.ch

    # Time complexity: O(1)
    # Space complexity: O(1)
    def hasNext(self) -> bool:
        return self.idx != len(self.data) or self.count != 0


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
