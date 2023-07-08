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


def reverse(str):
    st = ListStack()
    for i in range(len(str)):
        st.push(str[i])
    out = ""
    while not st.isEmpty():
        out += st.pop()

    return out

def main():
    input = "Test Seq 12345"
    output = reverse(input)

    print("input : ", input)
    print("output : ", output)


main()