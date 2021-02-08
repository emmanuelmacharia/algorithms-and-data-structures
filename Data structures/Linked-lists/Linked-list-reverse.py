'''
Create a linked list

We create a Node object and create another class to use this node object. 
We pass the appropriate values thorugh the node object to point the to the next data elements. 
The below program creates the linked list with three data elements
'''


class Node:
    ''''
    creates the node object; Itll take two prpoperties, 
    the Link - what stores the element of data; we also call this the node
    the pointer - we call this Next; it points to the next value of the linked list
    '''
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
        
class SLinkedList:
    '''
    creates the head value for our linked list;
    This class is responsible for initializing our linked list's head so that we can actually use the Node class
    Remember that in a linked list, we need to have an object that starts the whole thing that isnt linked to anythiing prior; thats the head
    think of this 1 -> 2 -> 3 -> 4 -> 5 -> NULL
    1 is the head, 5 is the tail; the tail also always points to a NULL value
    '''
    def __init__(self):
        self.headVal = None

    def listPrint(self):
        printVal = self.headVal
        while printVal is not None:
            print('Our node element ---> ', printVal.dataval)
            print('Our  node pointer ---> ', printVal.nextval)
            printVal = printVal.nextval

list1 = SLinkedList()
# create the headval for your linked list
list1.headVal = Node('Mon')
# create some other nodes we can link to from the headval
day2 = Node('Tue')
day3 = Node('Wed')
day4 = Node('Thur')

# lets link the first node to the second

list1.headVal.nextval = day2

# link the second node to the third

day2.nextval = day3

# and so on

day3.nextval = day4


#TRAVERSING A LINKED LIST
'''
To traverse a linked list (singly linked lists), we can only move in the forward direction, ie from the head to the tail.
For an example, we can try simply prinitng out the value of the next element in our linked list, by assigning the pointer of the next node to the current element
'''
list1.listPrint()


# INSERTING A LINKED LIST