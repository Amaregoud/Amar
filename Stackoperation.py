class Stack:
    def __init__(self):
        self.__stack = []  # Private stack list

    def push(self, data):
        self.__stack.append(data)
        print(f"Pushed {data} into Stack")

    def size(self):
        return len(self.__stack)

    def is_empty(self):
        return len(self.__stack) == 0

    def top(self):
        if len(self.__stack) == 0:
            print("Stack is Empty")
        else:
            return self.__stack[-1]

    def pop(self):
        if len(self.__stack) == 0:
            print("Stack is Empty")
        else:
            popped = self.__stack.pop()
            print(f"Popped {popped} from Stack")
            return popped


# Testing the stack
mystack = Stack()
print("Is empty?", mystack.is_empty())
mystack.push(10)
mystack.push(20)
mystack.push(30)
mystack.push(40)
mystack.push(50)
print("Size:", mystack.size())
mystack.pop()
mystack.pop()
print("Size after popping:", mystack.size())
print("Top element:", mystack.top())
