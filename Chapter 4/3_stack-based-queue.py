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
        return self._top.data if self._top else None

    def push(self, data):
        new_node = Node(data, self._top)
        self._top = new_node
        self._size += 1

    def pop(self):
        if self._top:
            popped = self._top.data
            self._top = self._top.next
            self._size -= 1
            return popped
        else:
            return None

    def is_empty(self):
        return self._size == 0
    
    def __iter__(self):
        current = self._top
        while current:
            yield current.data
            current = current.next

def check_balance(text):
    stack = Stack()
    opening_brackets = '({['
    closing_brackets = ')}]'
    pair_count = 0

    for i, char in enumerate(text, start=0):
        if char in opening_brackets:
            stack.push((char, i))
        elif char in closing_brackets:
            if stack.is_empty():
                return f"Match error at position {i}"
            top = stack.pop()
            
            pair_count += 1
            if (top[0] == '(' and char != ')') or (top[0] == '{' and char != '}') or (top[0] == '[' and char != ']'):
                return f"Match error at position {i}"

    if not stack.is_empty():
        top = stack.pop()
        return f"Match error at position {top[1]}"

    return f"Ok - {pair_count}"


class StackBasedQueue():
    
    # Luodaan stackit ja laitetaan size 0
    def __init__(self):
        self._size = 0
        self._InboundStack = Stack()
        self._OutboundStack = Stack()
        
    def __repr__(self):
        plural = '' if self._size == 1 else 's'
        values = [c for c in self._InboundStack]
        values.extend([c for c in self._OutboundStack][::-1])
        return f'<StackBasedQueue ({self._size} element{plural}): [{", ".join(values)}]>'

    def enqueue(self, data):
        # Pushataan tuleva data inboundiin päällimmäiseksi
        self._InboundStack.push(data)
        # Kasvatetaan kokoa yhdellä
        self._size += 1

    def dequeue(self):
        # Jos outbound on tyhjä
        if self._OutboundStack.is_empty():
            # Kun inbound ei ole tyhjä
            while not self._InboundStack.is_empty():
                # Popataan inboundista päällimmäinen outboundiin
                self._OutboundStack.push(self._InboundStack.pop())
        # Jos outbound ei ole tyhjä
        if not self._OutboundStack.is_empty():
            # Vähennetään koosta yksi
            self._size -= 1
            # Palautetaan poistettu juttu
            return self._OutboundStack.pop()
        else:
            return None