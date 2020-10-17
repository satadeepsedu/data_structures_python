class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def showList(self):
        if self.head is None:
            print ('\nList Empty.\n')
            return
        current = self.head
        while (current):
            print (current.data, end=' ')
            current = current.next

    def insertNodeBeginning(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insertNodeWithin(self,prev_data,current_data):
        node = Node(current_data)
        if self.head is None:
            print ('\nPrevious data is not present in linked list.\n')
        else:
            current = self.head
            while (current):
                if current.data == prev_data:
                    node.next = current.next
                    current.next = node
                    break
                current = current.next
            if current is None:
                print ('\nPrevious data is not present in linked list.\n')
    
    def insertNodeEnd(self,data,next=None):
        node = Node(data,next)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while (current.next):
                current = current.next
            current.next = node

    def deleteNodeKey(self,key):
        if self.head is None:
            print ('\nList Empty. No elements to delete.\n')
        elif self.head.data == key:
            temp = self.head
            self.head = self.head.next
            del(temp)
        else:
            current = self.head.next
            prev = self.head
            while (current):
                if current.data == key:
                    prev.next = current.next
                    del(current)
                    return
                prev = current
                current = current.next
            if current is None:
                print ('\nKey not found.\n')
    
    def deleteNodePos(self,position):
        if position < 1:
            print ('\nInvalid position value entered.\n')
        elif self.head is None:
            print ('\nList Empty. No elements to delete.\n')
        elif position == 1:
            temp = self.head
            self.head = self.head.next
            del(temp)
        else:
            curr = self.head.next
            prev = self.head
            for i in range(position-2):
                prev = curr
                curr = curr.next
            if curr is None:
                print ('\nPosition value entered is greater than the length of the list.\n')
            else:
                prev.next = curr.next
                del(curr)
    
    def deleteCompleteList(self):
        if self.head is None:
            print ('\nList already empty.\n')
        else:
            curr = self.head.next
            prev = self.head
            while (curr):
                del (prev)
                prev = curr
                curr = curr.next
            del(prev)
            self.head = None
    
    def findListLength(self):
        temp = self.head
        length = 0
        while (temp):
            length = length + 1
            temp = temp.next
        return (length)
    
    def searchElement(self,key):
        if self.head is None:
            print ('\nList Empty.\n')
        elif self.head.data == key:
            return (1)
        else:
            curr = self.head.next
            pos=2
            while (curr):
                if curr.data == key:
                    return (pos)
                pos = pos + 1
                curr = curr.next
        return (-1)

    def detectLoopAndFindLoopLength(self):
        if self.head is None:
            return (-1,[])
        else:
            temp = self.head
            node_list = []
            while (temp):
                if temp in node_list:
                    break
                else:
                    node_list.append(temp)
                    temp = temp.next
            if temp is None:
                return (-1,[])
            else:
                idx = node_list.index(temp)
                loop_length = len(node_list) - idx
                return (loop_length,node_list[idx:])



if __name__ == "__main__":
    ll = LinkedList()
    ll.head = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    ll.head.next = node2
    node2.next = node3
    print (f'Initial Node: -\n')
    ll.showList()
    print ('\n')
    ll.insertNodeBeginning(6)
    print (f'After insertion at beginning: -\n')
    ll.showList()
    print ('\n')
    ll.insertNodeWithin(2,8)
    print (f'After insertion at middle: -\n')
    ll.showList()
    print ('\n')
    ll.insertNodeWithin(10,12)
    print (f'After insertion at middle: -\n')
    ll.showList()
    print ('\n')
    ll.insertNodeEnd(10)
    print (f'After insertion at end: -\n')
    ll.showList()
    print ('\n')
    ll.deleteNodeKey(4)
    print (f'After deletion with key: -\n')
    ll.showList()
    print ('\n')
    ll.deleteNodePos(4)
    print (f'After deletion with position 4: -\n')
    ll.showList()
    print ('\n')
    length = ll.findListLength()
    print (f'Length of the list: {length}\n')
    print ('\n')
    pos = ll.searchElement(10)
    if pos != -1:
        print (f'Position of 10: {pos}\n')
    else:
        print ('\nKey not found in list.\n')
    print ('\n')
    ll.deleteCompleteList()
    print (f'After deletion of complete list: -\n')
    ll.showList()
    print ('\n')
    ll.insertNodeEnd(1)
    ll.insertNodeEnd(2)
    ll.insertNodeEnd(3)
    ll.insertNodeEnd(4)
    ll.insertNodeEnd(5,ll.head.next)
    loop_length,loop = ll.detectLoopAndFindLoopLength()
    if loop_length == -1:
        print ('\nList has no loop.\n')
    else:
        print (f'\nList has loop of length: {loop_length}\n')
        print (f'\nLoop: {[node.data for node in loop+[loop[0]]]}\n')
