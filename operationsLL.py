class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Correct: Each node has data and a pointer to the next node

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp_next=new_node
    def insert_at_position(self,pos,value):
        if pos==0:
            self.insert_at_beginning(value)
            return
        new_node=Node(value)
        temp=self.head
        for i in range(pos-1):
            if temp is None:
                print("Position is out of range")
                return
            temp=temp.next
        new_node.next=temp.next
        temp.next=new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ---> ")
            temp = temp.next
        print("None")
        
    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty")
            return
        self.head=self.head.next
    def delete_at_end(self):
        if self.head is None:
            print("List is Empty")
            return 
        if self.head.next is None:
            self.head=None
            return
        temp=self.head
        while temp.next.next:
            temp=temp.next
        temp.next=None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next

    def delete_at_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def delete_at_position(self, pos):
        if self.head is None:
            print("List is empty")
            return
        if pos == 0:
            self.head = self.head.next
            return
        temp = self.head
        for i in range(pos - 1):
            if temp is None or temp.next is None:
                print("Position out of range")
                return
            temp = temp.next
        if temp.next is None:
            print("Position out of range")
            return
        temp.next = temp.next.next

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ---> ")
            temp = temp.next
        print("None")

            
            
        
# Create Linked List and test
ll = LinkedList()
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.insert_at_end(40)
ll.print_list()

ll.delete_at_beginning()
ll.print_list()

ll.delete_at_end()
ll.print_list()

ll.delete_at_position(1)
ll.print_list()

 