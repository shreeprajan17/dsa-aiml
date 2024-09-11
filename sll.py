class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.temp = None

    def create(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.temp = newnode
        else:
            self.temp.next = newnode
            self.temp = self.temp.next

    def display(self):
        self.temp = self.head
        while self.temp is not None:
            print(self.temp.data, end=" ")
            self.temp = self.temp.next
        print()

    def insert_at_front(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    def insert_at_middle(self, data, pos):
        newnode = Node(data)
        self.temp = self.head
        i = 1
        while i < pos - 1:
            self.temp = self.temp.next
            i += 1
        newnode.next = self.temp.next
        self.temp.next = newnode

    def insert_at_end(self, data):
        newnode = Node(data)
        self.temp = self.head
        while self.temp.next is not None:
            self.temp = self.temp.next
        self.temp.next = newnode

    def delete_at_front(self):
        self.head = self.head.next

    def delete_at_mid(self, pos):
        i = 1
        self.temp = self.head
        while i < pos - 1:
            self.temp = self.temp.next
            i += 1
        self.temp.next = self.temp.next.next

    def delete_at_end(self):
        self.temp = self.head
        while self.temp.next.next is not None:
            self.temp = self.temp.next
        self.temp.next = None


obj = LinkedList()
while True:
    print("1.Create\n2.Display\n3.Insert At Front\n4.Insert At Middle\n"
          "5.Insert At End\n6.Delete at front\n7. Delete at end\n"
          "8.Delete at Mid\n9.Exit\n")

    choice = int(input("Enter a choice: "))
    if choice == 1:
        data = int(input("Enter data: "))
        obj.create(data)
    elif choice == 2:
        obj.display()
    elif choice == 3:
        data = int(input("Enter data to insert at front: "))
        obj.insert_at_front(data)
    elif choice == 4:
        data = int(input("Enter data to insert at middle: "))
        pos = int(input("Enter position: "))
        obj.insert_at_middle(data, pos)
    elif choice == 5:
        data = int(input("Enter data to insert at end: "))
        obj.insert_at_end(data)
    elif choice == 6:
        obj.delete_at_front()
    elif choice == 7:
        obj.delete_at_end()
    elif choice == 8:
        pos = int(input("Enter position: "))
        obj.delete_at_mid(pos)
    else:
        print("Invalid Choice! Enter Again!")