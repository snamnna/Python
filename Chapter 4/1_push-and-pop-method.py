class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'<Node: {self.data}>'


class Stack:
    def __init__(self):
        self._top = None
        self._size = 0

    def __len__(self):
        return self._size

    def peek(self):
        """
        Returns the value of the top node without altering the stack
        """
        return self._top.data if self._top else None

    def push(self, data):
        """
        Add an element to the stack

        Parameters:
        - 'data': Data/value being added

        Returns: None
        """
        
        # Kun uusi node luodaan, data on se mitä node sisältää
        # ja self._top asetetaan noden seuraavaksi nodeksi

        # Luodaan uusi node
        new_node = Node(data, self._top)
        
        # Asetetaan uusi node topiksi, sillä vain päälle saa laittaa asioita
        self._top = new_node
        
        # Kasvatetaan stackin kokoa yhdellä lisäämisen jälkeen
        self._size += 1

    def pop(self):
        """
        Remove the top node from the stack and return its content

        Parameters: None

        Returns: The content of the node or None if stack is empty
        """
        # Jos on olemassa top, poistetaan se, sillä muuta ei saa poistaa
        if self._top:
            popped = self._top.data
            # Asetetaan uusi top olemaan vanhasta topista seuraava
            self._top = self._top.next
            # Vähennetään stackista yksi
            self._size -= 1
            return popped
        else:
            return None

    def __repr__(self):
        
        
        #Tehdään lista elementeille ja aloitetaan päällimmäisestä elementistä
        elements = []
        current = self._top
        # Niin kauan kun arvoja on, lisätään niitä listaan
        while current:
            elements.append(str(current.data))
            current = current.next
        plural = 's' if self._size != 1 else ''
        return f"<Stack ({self._size} element{plural}): [{', '.join(elements)}]>"