class MaxHeap:
    def __init__(self):
        self.heap = []

    def __str__(self):
        return str(self.heap)

    def __len__(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def peek(self):
        return self.heap[0] if self.heap else None

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2

            if self.heap[index] > self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    def delete(self):
        if not self.heap:
            return -1

        if len(self.heap) == 1:
            return self.heap.pop()

        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        popped = self.heap.pop()

        self._heapify_down(0)
        return popped

    def _heapify_down(self, index):
        n = len(self.heap)

        while True:
            largest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < n and self.heap[left] > self.heap[largest]:
                largest = left

            if right < n and self.heap[right] > self.heap[largest]:
                largest = right

            if largest == index:
                break

            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            index = largest

    def build_heap(self, arr):
        self.heap = arr[:]
        n = len(self.heap)

        for i in range((n // 2) - 1, -1, -1):
            self._heapify_down(i)

    def heap_sort(self):
        result = []
        while not self.is_empty():
            result.append(self.delete())
        return result