""" linked list """

class Stack:
    """ LIFO Stack using lists """
    def __init__(self):
        self.items = [] # builtin list data type

    def push(self, value):
        """ add a new item into the list """
        self.items.append(value) # builtin append list method

    def pop(self):
        """ remove an item from the list """
        if len(self.items) == 0: # empty list
            return None
        return self.items.pop() # non-empty list # builtin pop list method

    def size(self):
        """ get size """
        return len(self.items)

class Queue:
    """ FIFO queue with lists """
    def __init__(self):
        self.items = []

    def size(self):
        """ get size """
        return len(self.items)

    def enqueue(self, item):
        """ new last item """
        self.items.append(item)

    def dequeue(self):
        """ first item out """
        if self.size() == 0:
            return None
        return self.items.pop(0)

    def show_queue(self):
        """ show queue """
        print(self.items)
