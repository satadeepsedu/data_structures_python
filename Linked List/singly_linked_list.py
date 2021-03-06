class Node:
    """
    A Node class represents a single node of a linked list.
    
    Attributes
    ----------
    data : any type
        Information stored by the node.
    next: class
        Address of the next node of the Linked List.
    """
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class LinkedList:
    """
    A LinkedList represents a chain of Nodes.

    Attributes
    ----------

    Method
    ------
    __init__():
        initializes the head of the list.
    showList():
        display the linked list.
    insertNodeBeginning(data):
        inserts a node at the beginning of the list. The argument "data" is the value of the node being inserted.
    insertNodeWithin(prev_data,current_data):
        inserts a node at a position in the list where value held by the previous node is "prev_data". The argument "data" is the value of the node being inserted.
    insertNodeEnd(data):
        inserts a node at the end of the list. The argument "data" is the value of the node being inserted.
    deleteNodeKey(key):
        deletes a node whose value is equal to "key".
    deleteNodePos(position):
        deletes a node from the nth position of the list where n = "position".
    deleteCompleteList():
        deletes the complete list.
    findListLength():
        returns the length of the linked list.
    searchElement(key):
        searches the list for the node having the value = "key" and returns its position.
    detectLoopAndFindLoopLength():
        finds any loop present in the list. If present, returns the loop elements.
    """
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
    
    def findMiddleNode(self):
        if self.head is None:
            return (-1)
        else:
            pointer1 = self.head
            pointer2 = self.head
            middle_pos = 1
            while pointer2 is not None and pointer2.next is not None:
                pointer2 = pointer2.next.next
                pointer1 = pointer1.next
                middle_pos += 1
            return (middle_pos, pointer1.data)

    def isListPalindrome(self):
        if self.head is None:
            return (-1)
        else:
            propagation_stack = []
            pointer = self.head
            while pointer is not None:
                propagation_stack.append(pointer.data)
                pointer = pointer.next
            pointer = self.head
            while pointer is not None:
                last_ele = propagation_stack.pop()
                if last_ele != pointer.data:
                    return (False)
                pointer = pointer.next
            return (True)

    def removeDuplicates(self):
        if self.head is None:
            print (f'\nList already empty.\n')
            return ()
        else:
            traversed_values = []
            pointer1 = self.head
            pointer2 = self.head.next
            traversed_values.append(pointer1.data)
            if pointer2 is None:
                print (f'\nOnly one node in list.\n')
            else:
                while pointer2 is not None:
                    if pointer2.data not in traversed_values:
                        traversed_values.append(pointer2.data)
                        pointer1 = pointer1.next
                        pointer2 = pointer2.next
                    else:
                        pointer1.next = pointer2.next
                        del pointer2
                        pointer2 = pointer1.next
            print (f'\nList de-duplicated.\n')

    def mergeSortList(self):
        pass

    def quickSortList(self):
        pass

    def separateEvenOddNodes(self):
        if self.head is None:
            return ()
        else:
            pointer1 = self.head
            pointer2 = self.head
            odd_nodes_data = []
            while pointer2 is not None:
                if pointer2.data%2==0:
                    if pointer2 != self.head:
                        pointer1 = pointer1.next
                    pointer2 = pointer2.next
                else:
                    odd_nodes_data.append(pointer2.data)
                    if pointer2 == self.head:
                        self.head = self.head.next
                        del pointer2
                        pointer1 = self.head
                        pointer2 = self.head
                    else:
                        pointer1.next = pointer2.next
                        del pointer2
                        pointer2 = pointer1.next
            for node_val in odd_nodes_data:
                new_node = Node(node_val,None)
                pointer1.next = new_node
                pointer1 = new_node
            return ()
    
    def reverseLinkedList(self):
        if self.head is None:
            return ()
        else:
            pointer1 = self.head
            pointer2 = pointer1.next
            if pointer2 is None:
                print ('\nOne one list in node.\n')
                return()
            pointer1.next = None
            pointer3 = pointer2.next
            while pointer3 is not None:
                pointer2.next = pointer1
                pointer1 = pointer2
                pointer2 = pointer3
                pointer3 = pointer3.next
            pointer2.next = pointer1
            self.head = pointer2
        return()
            
            
                        



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
    middle_pos,middle_element = ll.findMiddleNode()
    print (f'Middle position: {middle_pos}, Middle Element: {middle_element}\n')
    print (f'\nIs list palindrome: {ll.isListPalindrome()}\n')
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
    print (f'\nInserting elements into the list.\n')
    ll.insertNodeEnd(1)
    ll.insertNodeEnd(2)
    ll.insertNodeEnd(2)
    ll.insertNodeEnd(1)
    ll.showList()
    print ('\n')
    print (f'\nIs list palindrome: {ll.isListPalindrome()}\n')
    ll.removeDuplicates()
    ll.showList()
    print ('\n')
    ll.deleteCompleteList()
    print (f'List deleted\n')
    ll.insertNodeEnd(1)
    ll.insertNodeEnd(2)
    ll.insertNodeEnd(3)
    ll.insertNodeEnd(4)
    ll.insertNodeEnd(5,ll.head.next)
    print (f'\nList: 1,2,3,4,5,2\n')
    loop_length,loop = ll.detectLoopAndFindLoopLength()
    if loop_length == -1:
        print ('\nList has no loop.\n')
    else:
        print (f'\nList has loop of length: {loop_length}\n')
        print (f'\nLoop: {[node.data for node in loop+[loop[0]]]}\n')
    del ll
    ll = LinkedList()
    ll.insertNodeEnd(17)
    ll.insertNodeEnd(15)
    ll.insertNodeEnd(8)
    ll.insertNodeEnd(12)
    ll.insertNodeEnd(9)
    ll.insertNodeEnd(10)
    ll.insertNodeEnd(1)
    print (f'\nList before odd even separation:-')
    ll.showList()
    print ('\n')
    ll.separateEvenOddNodes()
    print (f'\nList after odd even separation:-')
    ll.showList()
    print ('\n')
    print ('\nList before reversal:-')
    ll.showList()
    print ('\n')
    print ('\nList after reversal:-')
    ll.reverseLinkedList()
    ll.showList()
    print ('\n')
