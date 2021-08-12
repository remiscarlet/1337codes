class MyCircularQueue:
    """
    Runtime: 97.76%
    Memory: 87.21%
    """

    def __init__(self, k: int):
        self.q = [-1] * k
        self.p = 0
        self.size = 0
        self.max_size = k

    def _incrementPointer(self):
        self.p = (self.p + 1) % self.max_size

    def enQueue(self, value: int) -> bool:
        if self.size == self.max_size:
            return False

        p = (self.p + self.size) % self.max_size
        self.q[p] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.Front() == -1:
            return False

        self.size -= 1
        self._incrementPointer()
        return True

    def Front(self) -> int:
        if self.size == 0:
            return -1

        val = self.q[self.p]
        return val

    def Rear(self) -> int:
        if self.size == 0:
            return -1

        p = (self.p + self.size - 1) % self.max_size
        val = self.q[p]
        return val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
