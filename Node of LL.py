#create a Node OF LL
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None


first=Node(1)
second=Node(2)
third=Node(3)



first.next=second
second.next=third
head=first
print(first.next)


print(head.data)
print(head.next.data)
print(head.next.next.data)