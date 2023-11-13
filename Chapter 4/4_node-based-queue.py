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
            