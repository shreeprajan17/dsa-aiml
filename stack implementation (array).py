class Stack:

    def __init__(self, size):
        self.stack = [None] * size
        self.top = -1
        self.size = size

    def push(self, data):
        if self.top >= self.size - 1:
            print("Stack Overflow")
        else:
            self.top += 1
            self.stack[self.top] = data

    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
        else:
            item = self.stack[self.top]
            self.top -= 1
            return item

    def peek(self):
        if self.top == -1:
            print("Stack is Empty")
        else:
            return self.stack[self.top]

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.size - 1

    def display(self):
        if self.top == -1:
            print("Stack is Empty")
        else:
            print("Stack contents:", self.stack[:self.top + 1])


stack_size = int(input("Enter the size of the stack: "))
obj = Stack(stack_size)

while True:
    print("\n1. Push\n2. Pop\n3. Peek\n4. Display\n5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        if obj.is_full():
            print("Cannot push. Stack is full.")
        else:
            data = int(input("Enter data: "))
            obj.push(data)
    elif choice == 2:
        if obj.is_empty():
            print("Cannot pop. Stack is empty.")
        else:
            print(f"Popped: {obj.pop()}")
    elif choice == 3:
        if obj.is_empty():
            print("Cannot peek. Stack is empty.")
        else:
            print(f"Peeked: {obj.peek()}")
    elif choice == 4:
        obj.display()
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice, please try again.")
