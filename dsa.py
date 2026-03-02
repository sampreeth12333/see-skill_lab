class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"{item} pushed into stack.")

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
        else:
            removed = self.stack.pop()
            print(f"{removed} popped from stack.")

    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print(f"Top element is: {self.stack[-1]}")

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack elements are:", self.stack)
