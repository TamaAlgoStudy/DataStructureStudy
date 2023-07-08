class ListStack:
    def __init__(self):
        self.__stack = []

    def push(self, x):
        self.__stack.append(x)

    def pop(self):
        return self.__stack.pop()

    def top(self):
        if self.isEmpty():
            return None
        return self.__stack[-1]

    def isEmpty(self):
        return not bool(self.__stack)

    def popAll(self):
        self.__stack = []

    def printStack(self):
        print("Stack :", end = ' ')
        for i in range(len(self.__stack)-1, -1, -1):
            print(self.__stack[i], end = ' ')
        print()

liStack = ListStack()
print(liStack.top())

liStack.push(5)
liStack.push(10)
print("top : ", liStack.top())
liStack.pop()
liStack.push('test')

liStack.printStack()