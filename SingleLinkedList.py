class Node:
    def __init__(self, data= None, next= None):
        self.data= data
        self.next= next

class LinkedList:
    def __init__(self):
        self.head= None

    def pop(self, data):
        node= Node(data, self.head)
        self.head= node

    def insert_at_index_k(self, k, val):
        if k> self.length():
            print('invalid index, Length of the linked list is:', self.length())
            return

        else:
            node_k= Node(val)
            ptr= self.head
            for _ in range(k- 1):
                ptr= ptr.next

            node_k.next= ptr.next
            ptr.next= node_k

    def delete_k(self, k):
        if k< 0 or k>= self.length():
            print('Invalid index')
            return 

        elif k== 0:
            self.head= self.head.next
            return
        else:
            count= 0
            ptr= self.head
            while ptr:
                if count== k- 1:
                    ptr.next= ptr.next.next
                    break

                ptr= ptr.next
                count+= 1

    def length(self):
        length= 0
        ptr= self.head
        while ptr:
            length+= 1
            ptr= ptr.next
        return length

    def Print(self):
        if self.head is None:
            print('Empty linked list')
            return

        else:
            itr= self.head
            val= ' '
            while itr:
                val+= str(itr.data)+ '-->'
                itr= itr.next

            print(val)

if __name__== '__main__':
    ll= LinkedList()
    ll.pop(5)
    ll.pop(6)
    ll.insert_at_index_k(2, 99)
    ll.delete_k(1)
    ll.Print()