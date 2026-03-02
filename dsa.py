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

s = Stack()

while True:
    print("\n--- STACK MENU ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        value = input("Enter value to push: ")
        s.push(value)

    elif choice == '2':
        s.pop()

    elif choice == '3':
        s.peek()

    elif choice == '4':
        s.display()

    elif choice == '5':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")
