class Node:  
    def __init__(self,data):  
        self.data = data;  
        self.next = None;  
   
class CircularList:  
    #Here we a are declaring head and tail pointer as null.  
    def __init__(self):  
        self.count = 0;  
        self.tail = Node(None);
        self.head = Node(None);  
        self.head.next = self.tail;  
        self.tail.next = self.head;  
      
    #function to add new node at the end of the list.  
    def addnode(self,data):  
        newNode = Node(data);  
        #statemet that Checks if the list is empty.  
        if self.head.data is None:  
            #If empty, head and tail would point to new node.  
            self.head = newNode;  
            self.tail = newNode;  
            newNode.next = self.head;  
        else:  
            #tail will point to new node.  
            self.tail.next = newNode;  
            # the New node will become new tail.  
            self.tail = newNode;  
            #it is circular linkedlist so tail will point to head.  
            self.tail.next = self.head;  
              
    #This is a function to count the nodes of list  
    def NodeCount(self):  
        ThisNode = self.head;  
        self.count=self.count+1;  
        while(ThisNode.next != self.head):  
            self.count=self.count+1;  
            ThisNode  = ThisNode.next;  
        print("number of nodes in this circular linked list is: "),  
        print(self.count);  
      
   
class SinglyLinkedCircularList:  
    A = CircularList();  
    #Add data 
    A.addnode(9);  
    A.addnode(0);  
    A.addnode(48);  
    A.addnode(2);  
    A.addnode(38);  
    #Displays all the nodes found in the list  
    A.NodeCount();  