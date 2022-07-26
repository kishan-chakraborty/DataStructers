class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def length(self):
        length = 0
        temp = self.head
        while temp:
            length += 1
        return length

    def display(self):
        l = self.length()
        print(f"Length of the linked list is = {l}")
        
        if l == 0:
            print("Nothing to display")
        else:
            temp = self.head
            while temp:
                print(temp.data)
                temp = temp.next

    def push(self, val):
        temp = self.head
        while temp:
            temp = temp.next
        
        temp = Node(val)
        return self




if __name__ == "__main__":
    ll = LinkedList()
    while True:
        print("1. Display\n2. Push\n3. Pop\n4. Enter at a particular index.\n5. Delete from a particular index.\n6. Break\n")
        task = int(input("Enter operation"))

        match task:
            case 1:
                ll.display()

            case 2:
                push_val = int(input("Enter value to push."))
                ll.push(push_val)

            case 3:
                pop(ll)

            case 4:
                index = int(input("Enter index"))
                val = int(input("Enter value"))
                enter_at_index(ll, index, val)

            case 5:
                index = int(input("Enter index"))
                del_from_index(ll, index)

            case default:
                break

