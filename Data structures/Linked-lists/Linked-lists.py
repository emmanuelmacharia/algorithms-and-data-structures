# '''
# Create a linked list

# We create a Node object and create another class to use this node object. 
# We pass the appropriate values thorugh the node object to point the to the next data elements. 
# The below program creates the linked list with three data elements
# '''


# class Node:
#     ''''
#     creates the node object; Itll take two prpoperties, 
#     the Link - what stores the element of data; we also call this the node
#     the pointer - we call this Next; it points to the next value of the linked list
#     '''
#     def __init__(self, dataval=None):
#         self.dataval = dataval
#         self.nextval = None
        
# class SLinkedList:
#     '''
#     creates the head value for our linked list;
#     This class is responsible for initializing our linked list's head so that we can actually use the Node class
#     Remember that in a linked list, we need to have an object that starts the whole thing that isnt linked to anythiing prior; thats the head
#     think of this 1 -> 2 -> 3 -> 4 -> 5 -> NULL
#     1 is the head, 5 is the tail; the tail also always points to a NULL value
#     '''
#     def __init__(self):
#         self.headVal = None

#     def listPrint(self):
#         printVal = self.headVal
#         while printVal is not None:
#             print('Our node element ---> ', printVal.dataval)
#             print('Our  node pointer ---> ', printVal.nextval)
#             printVal = printVal.nextval

    

# list1 = SLinkedList()
# # create the headval for your linked list
# list1.headVal = Node('Mon')
# # create some other nodes we can link to from the headval
# day2 = Node('Tue')
# day3 = Node('Wed')
# day4 = Node('Thur')

# # lets link the first node to the second

# list1.headVal.nextval = day2

# # link the second node to the third

# day2.nextval = day3

# # and so on

# day3.nextval = day4


# #TRAVERSING A LINKED LIST
# '''
# To traverse a linked list (singly linked lists), we can only move in the forward direction, ie from the head to the tail.
# For an example, we can try simply prinitng out the value of the next element in our linked list, by assigning the pointer of the next node to the current element
# '''
# list1.listPrint()


# # INSERTING A LINKED LIST


# # REVERSE A LINKED LIST A -> B -> C -> D -> NULL to D -> C -> B -> A -> NULL

# ''' iterative reversal'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.headval = None

    def print_list(self):
        print_val = self.headval
        while print_val:
            print(print_val.data)
            print_val = print_val.next


    def isEmpty(self):
        if self.headval is None:
            return True

    def append(self, data):
        '''adds to the end of the list'''
        new_node = Node(data)

        if self.isEmpty():
            self.headval = new_node
            return
        
        last_node = self.headval
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node


    def prepend(self, data):
        ''' adds to the begiining of the linked list'''
        new_node = Node(data)

        if self.isEmpty():
            self.headval = new_node
            return

        first_node = self.headval
        new_node.next = first_node
        self.headval = new_node

    def insert_in_between(self, prev_node, data):
        '''inserts a node in between two nodes'''

        if not prev_node:
            print('node doesnt exist')
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        




lList = LinkedList()
lList.append('A')
lList.append("B")
lList.append('C')
lList.append("D")
lList.prepend('E')

lList.insert_in_between(lList.headval.next.next, 'F')

lList.print_list()