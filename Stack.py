"""

Designed on Principle of LIFO
Last in first out

"""
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        if self.head:
            new_element.next = self.head
        self.head = new_element

    def delete_first(self):
        element_to_delete = None
        if self.head:
            element_to_delete = self.head
            self.head = self.head.next
        return element_to_delete

    def printlist(self):
        """
        Print all values present in Elements of LinkedList
        :return:
        """
        current_element = self.head
        items = []
        while current_element:
            items.append(current_element.value)
            current_element = current_element.next
        return items

class Stack(object):
    def __init__(self, top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        self.ll.insert_first(new_element)

    def pop(self):
        return self.ll.delete_first()

    def printList(self):
        return self.ll.printlist()


# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)
# Test stack functionality
stack.push(e2)
stack.push(e3)
print stack.pop().value
print stack.pop().value
print stack.pop().value
print stack.pop()
stack.push(e4)
print stack.pop().value
