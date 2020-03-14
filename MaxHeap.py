class MaxHeap:
    def __init__(self, size):
        if not isinstance(size, int):
            raise TypeError(f'The value must be type of int received {type(val)}')
        self._heap = [None] * (size + 1)
        self._maxSize = size
        self._size = 1

    def insert(self, val):
        if not isinstance(val, int):
            raise TypeError(f'The value must be type of int received {type(val)}')
        if self._size > self._maxSize:
            raise TypeError(f'The heap is full!')
        i = self._size
        self._heap[i] = val
        self._size = self._size + 1
        while i > 1 and (self._heap[i//2] is None or self._heap[i] > self._heap[i//2]):
            self._heap[i], self._heap[i//2] = self._heap[i//2], self._heap[i]
            i = i//2

    def delete(self):
        self._heap[1],self._heap[self._size - 1] = self._heap[self._size - 1], None
        self._size = self._size - 1 
        i = 1
        while 2*i < self._size and (self._heap[2*i] is not None):
            rightChild = self._heap[2*i + 1]
            if (rightChild is None) and (self._heap[i] < self._heap[2*i]):
                self._heap[i], self._heap[2*i] = self._heap[2*i], self._heap[i]
                i = 2*i
            elif (rightChild is not None):
                if self._heap[i] < rightChild or self._heap[i] < self._heap[2*i]:
                    if rightChild > self._heap[2*i]:
                        self._heap[i], self._heap[2*i+1] = self._heap[2*i+1], self._heap[i]
                        i = 2*i + 1
                    else:
                        self._heap[i], self._heap[2*i] = self._heap[2*i], self._heap[i]
                        i = 2*i

    def size(self):
        return self._size - 1

    def __str__(self):
        return str(self._heap[1:])