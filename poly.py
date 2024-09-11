class Node:
    def __init__(self, co, ex):
        self.co = co
        self.ex = ex
        self.next = None

class Poly:
    def __init__(self):
        self.head = None
        self.temp = None


    def create(self, co, ex):
        newnode = Node(co, ex)
        if self.head is None:
            self.head = newnode
            self.temp = newnode
        else:
            self.temp.next = newnode
            self.temp = newnode

    def display(self):
        self.temp = self.head
        while self.temp is not None:
            if self.temp.next is None:
                print(f"{self.temp.co}x^{self.temp.ex}")
            else:
                print(f"{self.temp.co}x^{self.temp.ex}", end=" + ")
            self.temp = self.temp.next

def add_poly(poly1, poly2):

    obj = Poly()

    p1 = poly1.head
    p2 = poly2.head

    while p1 is not None and p2 is not None:
        if p1.ex > p2.ex:
            obj.create(p1.co, p1.ex)
            p1 = p1.next
        elif p1.ex < p2.ex:
            obj.create(p2.co, p2.ex)
            p2 = p2.next
        else:
            obj.create(p1.co + p2.co, p1.ex)
            p1 = p1.next
            p2 = p2.next

    while p1 is not None:
        obj.create(p1.co, p1.ex)
        p1 = p1.next
    while p2 is not None:
        obj.create(p2.co, p2.ex)
        p2 = p2.next

    return obj


def input_():
    obj = Poly()
    while True:
        co = int(input("Enter coefficient: "))
        ex = int(input("Enter exponent: "))
        obj.create(co, ex)
        prompt = input("Do you want to continue? (Yes (or) No): ")
        if prompt.lower() == "no":
            break
    return obj

poly1 = input_()
print("Done!")
poly2 = input_()
print("Done!")

print("Polynomial 1:")
poly1.display()
print("Polynomial 2:")
poly2.display()
print("Resultant Polynomial: ")
result = add_poly(poly1, poly2)
result.display()