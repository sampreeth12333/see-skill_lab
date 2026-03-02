class Stack:
    def __init__(self):
        self.stack = []

    # Push element into stack
    def push(self, item):
        self.stack.append(item)
        print(f"{item} pushed into stack.")

    # Pop element from stack
    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
        else:
            removed = self.stack.pop()
            print(f"{removed} popped from stack.")

    # Peek top element
    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print(f"Top element is: {self.stack[-1]}")

    # Check if stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Display stack
    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack elements are:", self.stack)
