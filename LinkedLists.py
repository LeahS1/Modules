# -*- coding: utf-8 -*-
"""
Linked list modules
"""
class Node:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.nextval = None

class SLinkedlist:
    def __init__(self):
        self.headval = None
    
    def listprint(self):
        #Print the head node value
        printval = self.headval
        #while the node value isn't None, print the value in the datapoint
        while printval is not None:
            print (printval.dataval)
            #then reassign the printval as the next value
            printval = printval.nextval
            
    def newfrontnode(self, new_point):
        #Make a node with the new point value
        new_node = Node(new_point)
        #set the linkedlist headvalue to the new node's next value
        new_node.nextval = self.headval
        #set the head value as the new node
        self.headval = new_node
        
    def new_mid_node(self,prev_node,new_point):
        #check that the node value is in the list
        if prev_node is None:
            print ("Previous node doesn't exist in linked list")
            return
        #create a new node with the new value
        new_node =  Node(new_point)
        #set the previous nodes next value as the new nodes next value
        new_node.nextval = prev_node.nextval
        #then reverse it and set the previous nodes next value as the new node
        prev_node.nextval = new_node
        
    def append(self, new_point):
        #create a new node
        new_node = Node(new_point)
        #Check if Linkedlist is empty. If so, make the value the head value
        if self.headval is None:
            self.headval = new_node
            return
        #traverse through the linked list to the last value and 
        last = self.headval
        while (last.nextval):
            last = last.nextval 
        last.nextval = new_node 
    
    def count_nodes(self):
        counter = 0
        last = self.headval
        while (last):
            counter += 1
            last = last.nextval
        return counter
#%%
#Doubly linked lists module
class dNode:
    def __init__(self, dataval = None, prev = None):
        self.dataval = dataval
        self.nextval = None
        self.prev = prev

class dLinklist:
    def __init__(self):
        self.headval = None
    
    #Add a node at the front of the linkedlist
    def addfront(self, new_data):
        #Initiate a new node
        new_node = dNode(dataval = new_data)
        #Set the headval to the new node's next val
        new_node.nextval = self.headval
        #Set the new node's prev val to none
        new_node.prev = None
        if self.headval is not None:
        #Set the 
            self.headval.prev = new_node
        self.headval = new_node
        
    def dprintlist(self):
        #Print the head node value
        printval = self.headval
        #while the node value isn't None, print the value in the datapoint
        while printval is not None:
            print (printval.dataval)
            #then reassign the printval as the next value
            printval = printval.nextval
    
    #Add values after a given value
    def addafter(self, prev, new_data):
        #check that the previous value given isn't none
        if prev is None:
            print ("The previous node doesn't exist in this list")
            return
        #create a new node
        new_node = dNode(dataval = new_data)
        #Set the previous value's next value as the new nodes next value
        new_node.nextval = prev.nextval
        #Set the previous nodes next value as the new node
        prev.nextval = new_node
        #Set the new nodes previous value as the previous value
        new_node.prev = prev
        #Set the new node's next value's previous value as the new node
        if new_node.nextval is not None:
            new_node.nextval.prev = new_node
        
    def addlast(self, new_data):
        #Create a new node
        new_node = dNode(dataval = new_data)
        #Start at the headval
        last = self.headval
        
        #Check that the list isn't empty. If it is, then add the new_node as head
        if self.headval is None:
            new_node.prev = None
            self.head = new_node
            return
        
        #While there's a next value, iterate through the list replacing with next value
        while (last.nextval):
            last = last.nextval
        #Set the last value to have a next value of the new point
        last.nextval = new_node
        #Didn't need to set to None, but did 
        new_node.nextval = None
        #Set the new node's prev node as the last node
        new_node.prev = last
    
    def travforward(self, node):
        print ("Traversing forward through list \n")
        while (node is not None):
            print("%d" %(node.dataval))
            node = node.nextval
            last = node
        print ("Traversing backwards through list \n")
        while (last is not None):
            print ("%d" %(last.dataval))
            last = last.prev
    
    #Reverse a linkedlist
    def reverselink(self):
        #create a temporary holder variable
        temp = None
        current = self.headval
        while current is not None:
            #Set the current previous as a temp value
            temp = current.prev
            #Set the current next as the previous value
            current.prev = current.nextval
            #Set the temp as the current next value
            current.nextval = temp
            #Set the current previous value as the current value and iterate again
            current = current.prev
        if temp is not None:
            self.headval = temp.prev
            
    
#%% 
#Testing 
list1 = SLinkedlist()
list1.headval = Node(4)
e2 = Node(2)
e3 = Node(3)

list1.headval.nextval = e2
e2.nextval = e3

list1.newfrontnode(5)

list1.new_mid_node(list1.headval.nextval.nextval,1)

list1.append(8)
list1.append(4)

list1.listprint()
print( list1.count_nodes())

list2 = dLinklist()
list2.addfront(5)
list2.addfront(6)
list2.addafter(list2.headval,2)
list2.addlast(9)
list2.dprintlist()
list2.travforward(list2.headval)
list2.addlast(7)
list2.reverselink()
list2.dprintlist()




    
