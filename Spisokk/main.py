from http.client import NETWORK_AUTHENTICATION_REQUIRED


class Slivik:

    def __init__(self):

        element = []
        current = self.first_element

        while current:
            element.append(current.value)
            current = current.next
        return "[" + ', '.join(str(e) for e in element) + "]"

FMR = Slivik()
print
        
        self.data = None
        self.size = 0
        self.capacity = 1
        self.first_element = None
        self.last_element = None

    class Node:

        def __init__(self, value):
            self.value = value
            self.next = None

    def append(self, value):

        new_node = self.Node(value)

        if self.first.element is None:
            self.first_element = new_node
            self.last.element = new_node
        else:
            self.last_element.next = new_node
            self.last.element = new_node

        self.size += 1

FMR = Slivik()
print(FMR)
FMR.append('домой хачу(((')
print(FMR.first_element())