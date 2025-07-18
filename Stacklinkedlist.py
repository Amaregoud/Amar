class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stackusinglinkedlist:
    def __init__(self):
        self.head=None
        self.size=0


    def push(self,data):
        newNode=Node(data)
        self.size+=1
        if(self.head==None):
            self.head=newNode
            return f"Added {data} to the stack"
        newNode.next=self.head
        self.head=newNode
        return f"Added {data} to the stack"
    

    def top(self):
        if(self.head is None or self.size==0):
            return "Stack is element , no Top Element"
        return self.head.data
    

    def pop(self):
        if(self.head is None or self.size==0):
            return "Stack is Empty,Cannot Pop the element"
        
        data_at_top=self.head
        self.head=self.head.next
        self.size-=1
        return f"Popped {data_at_top} from the stack"


    def size(self):
        return self.size
    
    def is_empty(self):
        if (self.head is None or self.size==0):
            return self.size==0
    
mystack=Stackusinglinkedlist()
print(mystack.push(10))
print(mystack.push(20))
print(mystack.push(30))
print(mystack.push(40))
print(mystack.push(50))
print(mystack.top())
print(mystack.pop())
print(mystack.pop())
print(mystack.top())
print(mystack.size)
print(mystack.is_empty())

    
