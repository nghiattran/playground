def swap(arr, first, second):
    arr[first] = arr[first] + arr[second]
    arr[second] = arr[first] - arr[second]
    arr[first] = arr[first] - arr[second]


class Heap:
    _values = []
    def __init__(self, arr):
        if arr:
            self._values = arr
            self.build_heap()

    def parent(self, i):
        if i % 2 == 0:
            return int((i - 1) / 2)
        return int(i / 2)

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def heapify(self, i):
        left = self.left_child(i)
        right = self.right_child(i)

        if left < len(self._values) and self._values[left] > self._values[i]:
            largest = left
        else:
            largest = i

        if right < len(self._values) and self._values[right] > self._values[largest]:
            largest = right

        if largest != i:
            swap(self._values, i, largest)
            self.heapify(largest)

    def build_heap(self):
        for i in range(int((len(self._values) / 2) - 1), -1, -1):
            self.heapify(i)

    def heap_sort(self):
        self.build_heap()
        for i in range(len(self._values) - 1, -1, -1):
            swap(self._values, 0, i)
            self.heapify(i)
        return self._values

    def get_arr(self):
        return self._values

    def extract_max(self):
        if len(self._values) == 0:
            print('Overflow')
            return

        max = self._values[0]
        self._values[0] = self._values[len(self._values) - 1]
        self._values.pop()
        self.heapify(0)
        return max

arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
heap = Heap(arr)
print(heap.get_arr())
print(heap.extract_max())