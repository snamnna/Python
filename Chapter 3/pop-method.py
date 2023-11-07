class ListNode():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def __repr__(self):
        return f'<ListNode: {self.data}>'

class SinglyLinkedList():
    def __init__(self):
        self._head = None

    def __repr__(self):
        current_node = self._head
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        return f'<SinglyLinkedList: [{values.lstrip(", ")}]>'
     
    def append(self, value):
        """
        Append a value to the end of the list

        Parameters:
        - 'value': The data to append

        Returns: None
        """
        # Create the node with the value
        node = ListNode(value)
        # If list is empty just point the header to the new node
        if not self._head:
            self._head = node
        else:
            # if list is not empty, search for the last element and point it to the new node
            current_node = self._head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = node

    def pop(self):
        # Jos listassa ei ole mitään, palautetaan None
        if self._head == None:
            return None
        
        # Tämänhetkinen node jota käydään läpi
        current = self._head
        
        # Pidetään kirjaa myös edellisestä nodesta, sillä sitä on muokattava
        previous = None
        
        # Jos loopattavalla nodella on seuraava node, siirrytään looppaamaan sitä ja
        # asetetaan nykyinen siitä edelliseksi nodeksi
        while current.next:
            previous = current
            current = current.next
            
        # Jos nykyinen node on head eli listan ensimmäinen node, laitetaan että
        # head on nyt tyhjä
        if current == self._head:
            self._head = None
        # Jos ei, laitetaan poistettua nodea edellinen node osoittamaan tyhjään
        # koska se node poistetaan, johon se ennen osoitti
        else:
            previous.next = None
            
        # Otetaan talteen noden sisältö ennen sen poistamista
        value = current.data
        
        # Poistetaan node
        del(current)
        
        return value