class HashItem():
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    def __repr__(self):
        return f'{{{self.key}: {self.value}}}'

class HashTable():
    def __init__(self, size=256):
        self.size = size
        self.slots = [None] * size
        self.used_slots = 0
    
    def __repr__(self):
        text = ''
        for index, slot in enumerate(self.slots):
            if slot:
                text += f', {index}: {slot}'
        plural = '' if self.used_slots == 1 else 's'
        return f'<HashTable ({self.used_slots} element{plural}): [{text.lstrip(", ")}]'

    def _hash(self, key):
        """
        Hashing function. Can be changed for a custom one.
        """
        return len(key) % self.size

    def _find_free_slot(self, start):
        """
        Starting from 'start' find the next free slot available.
        
        Parameters:
        - 'start': Starting point for the search.

        Returns: The index of the next free slot or None if no free slots
        """
        # Etsitään siitä paikasta mistä parametrina saatu arvo haluaa aloittaa
        current = start
        
        # Niin kauan kun current paikassa on jotain (eli niin kauan kunnes löydetään tyhjä)
        while self.slots[current]:
            # Lisätään current muuttujaan aina yksi, mutta jos taulukon loppu saavutettiin
            # aloitetaan taulukon alusta
            current = (current + 1) % self.size
            
            # Jos mennään taas samaan pisteeseen mistä aloitettiin, on koko taulukko käyty läpi
            # ja tyhjää ei löytynyt
            if current == start:
                return None
          
        # Kun ollaan tultu pois loopista, current on tyhjä arvo, palautetaan se
        return current