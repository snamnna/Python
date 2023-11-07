class ListNode():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def __repr__(self):
        return f'<ListNode: {self.data}>'

class SinglyLinkedList():
    def __init__(self):
        self._head = self._tail = None
        self._size = 0

    def __repr__(self):
        current_node = self._head
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        plural = '' if self._size == 1 else 's'
        return f'<SinglyLinkedList ({self._size} element{plural}): [{values.lstrip(", ")}]>'

    def __len__(self):
        return self._size

    def append(self, value):
        """
        Append a value to the end of the list

        Parameters:
        - 'value': The data to append

        Returns: None
        """
        # Create the node with the value
        new_node = ListNode(value)

        # If list is empty just point the header to the new node
        if not self._tail:
            self._head = new_node
            self._tail = new_node
        else:
            # if list is not empty, update the last element and point it to the new node
            self._tail.next = new_node
            self._tail = new_node

        # Update list's size
        self._size += 1

    def pop(self):
        
        # Palautetaan none jos lista on tyhjä
        if not self._size:
            return None
        
        # Jos lista on tyhjä, headin on oltava myös None
        if self._size == 0:
            self._head = None  

        if self._size == 1:
            previous = None
        else:
            # Loopataan listaa läpi kunnes löydetään toiseksi viimeinen node
            previous = self._head
            for _ in range(self._size - 2):
                previous = previous.next
                
        # Merkitään poistettavaksi tail eli viimeinen
        node_to_remove = self._tail
        
        # Jos ei ole edellistä nodea, kyseinen node on ensimmäinen ja sen poistamisen jälkeen
        # head on muutettava osoittamaan ei mihinkään
        if previous is None:
            self._head = None
            self._tail = None
        # Muutoin muutetaan poistettua solmua edeltävä solmu osoittamaan ei mihinkään
        else:
            previous.next = None
            # Päivitetään viimeinen node olemaan poistettua edeltävä
            self._tail = previous
            
        # Otetaan value muistiin, päivitetään listan kokoa ja poistetaan poistettava node
        value = node_to_remove.data
        self._size -= 1
        del(node_to_remove)
        return value