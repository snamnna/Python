class Heap:
    def __init__(self):
        self._heap = []
        self._size = 0

    def _float(self):
        """
        Float the last element of the heap until the heap is in order
        """
        # Laitetaan indexiksi size - 1 eli viimeinen paikka
        index = self._size - 1
        
        while index > 0:
            # Lasketaan vanhemman indeksi ( // operaatio suorittaa kokonaislukujen jakolaskun ja palauttaa
            # lopputuloksen kokonaislukuina)
            parent_index = (index - 1) // 2
            # Jos nykyinen index on pienempi kuin sen parent, näiden paikkaa vaihdetaan
            if self._heap[index] < self._heap[parent_index]:
                self._heap[index], self._heap[parent_index] = self._heap[parent_index], self._heap[index]
            # Laitetaan indexiksi parentin indexi, sillä niiden paikkoja on vaihdettu
            index = parent_index