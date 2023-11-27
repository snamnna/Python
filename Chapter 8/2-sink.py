class Heap:
    def __init__(self):
        self._heap = []
        self._size = 0

    def _float(self):
        # Start at the end of the heap
        index = self._size - 1
        # Calculate index of parent element
        parent_index = (index-1) // 2
        # While not at Root node and value less than its parent
        while index > 0 and self._heap[index] < self._heap[parent_index]:
            # swap value with its parent
            self._heap[index], self._heap[parent_index] = self._heap[parent_index], self._heap[index]
            # Update indices
            index = parent_index
            parent_index = (index-1) // 2

    def insert(self, value):
        # Add the value to the heap
        self._heap.append(value)
        # Update size of the heap
        self._size += 1
        # And float the last element of the heap
        self._float()

    def _sink(self):
        """
        Sinks the root node of the heap until the heap is in order
        """
        index = 0
        # Niin kauan kun nodella on ainakin yksi child
        while index * 2 + 1 < self._size:
            # Jos on kaksi lasta, valitaan pienimmän arvon omaava
            if index * 2 + 2 < self._size:
                child_index = min(index * 2 + 1, index * 2 + 2, key = lambda x: self._heap[x])
            # Jos vain yksi lapsi
            else:
                child_index = index * 2 + 1
            # Jos parent on isompi kuin child, vaihdetaan paikkoja
            if self._heap[index] > self._heap[child_index]:
                self._heap[index], self._heap[child_index] = self._heap[child_index], self._heap[index]
                # Laitetaan indexiksi lapsen index jonka kanssa vaihto tapahtui
                index = child_index
