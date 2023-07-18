from typing import Any


class Stack:
    """
    Description:
    You are tasked with implementing a Stack data structure in Python,
    which follows the Last In, First Out (LIFO) principle.
    The Stack class should have the following methods:

    push(item): Adds an item to the top of the Stack.
    pop(): Removes the top item from the Stack and returns its value.
        - Raises an exception if the Stack is empty.
    peek(): Returns the value of the top item without removing it.
        - Raises an exception if the Stack is empty.
    is_empty(): Returns True if the Stack is empty, False otherwise.
    """
    def __init__(self):
        self.stack = []

    def push(self, item: Any):
        self.stack.append(item)

    def pop(self):
        if self.stack is None or len(self.stack) == 0:
            raise ValueError("Stack is empty, so can't remove top item from the stack")
        del self.stack[0]

    def peek(self):
        if self.stack is None or len(self.stack) == 0:
            raise ValueError("Stack is empty, so can't peek at the top item in stack")
        return self.stack[0]

    def is_empty(self):
        if self.stack is None or len(self.stack) == 0:
            return True
        return False
