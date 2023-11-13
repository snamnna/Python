class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Queue:
    def __init__(self):
        # Merkitään jonon alku ja loppu None, size 0
        self.front = None
        self.end = None
        self.size = 0
        
    # Enqueue metodi
    def enqueue(self, data):
        # Luodaan uusi node
        new_node = Node(data)
        # Jos jono on tyhjä, tehdään uudesta nodesta ensimmäinen ja viimeinen
        if self.size == 0:
            self.front = self.end = new_node
        # Muutoin osoitetaan edellisestä endistä uuteen ja laitetaan
        # uusi olemaan end
        else:
            self.end.next = new_node
            self.end = new_node
        self.size += 1
            
    def dequeue(self):
        if self.size == 0:
            return None
        # Otetaan ylös poistettavan tiedot
        data = self.front.data
        # Asetetaan uusi front
        self.front = self.front.next
        # Vähennetään jonosta yksi
        self.size -= 1
        # Jos jonossa ei ole ketään, end on tyhjä
        if self.size == 0:
            self.end = None
        return data
    
    def __repr__(self):
        elements = []
        current = self.front
        while current:
            elements.append(str(current.data))
            current = current.next
        elements.reverse()
        if self.size == 0:
            return f'<Queue (0 elements): []>'
        return f'<Queue ({self.size} element{"s" if self.size != 1 else ""}): [{", ".join(elements)}]>'
    
    def is_empty(self):
        return self.size == 0
            
def get_pairs(numbers):
    even_queue = Queue()
    odd_queue = Queue()
    result = []

    for num in numbers:
        if num % 2 == 0:
            if not odd_queue.is_empty():
                result.append((num, odd_queue.dequeue()))
            else:
                even_queue.enqueue(num)
        else:
            if not even_queue.is_empty():
                result.append((even_queue.dequeue(), num))
            else:
                odd_queue.enqueue(num)

    # Check for remaining elements in even_queue and odd_queue
    while not even_queue.is_empty() and not odd_queue.is_empty():
        result.append((even_queue.dequeue(), odd_queue.dequeue()))

    return result

print(get_pairs([74, 21, 18, 22, 71, 77, 82, 16, 77, 32, 90, 37, 98, 31, 59, 37, 99, 46, 28, 65]))
# Expected: [(74, 21), (18, 71), (22, 77), (82, 77), (16, 37), (32, 31), (90, 59), (98, 37), (46, 99), (28, 65)]

print(get_pairs([93, 55, 9, 36, 83, 98, 77, 97, 26, 81, 72, 48, 18, 20, 2, 88, 82, 51, 58, 30]))
# Expected: [(36, 93), (98, 55), (26, 9), (72, 83), (48, 77), (18, 97), (20, 81), (2, 51)]

print(get_pairs([79, 38, 36, 40, 26, 14, 30, 71, 97, 91, 86, 27, 71, 28, 70, 60, 70, 96, 67, 16]))
# Expected: [(38, 79), (36, 71), (40, 97), (26, 91), (14, 27), (30, 71), (86, 67)]

print(get_pairs([8, 95, 61, 69, 43, 67, 8, 23, 55, 5, 54, 68, 4, 96, 19, 57, 52, 52, 89, 54]))
# Expected: [(8, 95), (8, 61), (54, 69), (68, 43), (4, 67), (96, 23), (52, 55), (52, 5), (54, 19)]
