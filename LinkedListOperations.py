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
            temp = temp.next
            length += 1
        return length

    def display(self):
        l = self.length()
        print(f"Length of the linked list is = {l}")
        
        if l == 0:
            print("Nothing to display")
        else:
            temp = self.head
            while temp.next:
                print(temp.data)
                temp = temp.next
            print(temp.data)

    def push(self, val):
        if self.head is None:
            self.head = Node(val)
            return

        temp = self.head # temp is pointing to the node. Make sure use temp to point to the node instead of node.next
        while temp.next:
            temp = temp.next

        temp.next = Node(val)




if __name__ == "__main__":
    ll = LinkedList()
    ll.push(3)
    ll.push(4)
    ll.push(5)
    ll.display()

