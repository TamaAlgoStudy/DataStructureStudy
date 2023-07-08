class ListQueue:
    def __init__(self):
        self.__queue = []

    def enqueue(self, x): # 큐의 끝에 원소 x 를삽입.
        self.__queue.append(x)

    def dequeue(self): # 큐의 맨 앞에 있는 원소를 알려주고 삭제
        return self.__queue.pop(0)

    def front(self): # 큐의 맨 앞의 원소를 알려줌
        if self.isEmpty():
            return None
        return self.__queue[0]

    def isEmpty(self) -> bool: # 빈배열 확인
        return (len(self.__queue) == 0)

    def dequeueAll(self): # 초기화
        self.__queue.clear()

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

def isPalindrome(A) -> bool:
    # 거꾸로 해도 같은 문자인지 체크.

    # 형일 코드
    # s = ListStack()
    # q = ListQueue()

    # for i in range(len(A)):
    #     s.push(A[i])
    #     q.enqueue(A[i])
    
    # while (not q.isEmpty()) and s.pop() == q.dequeue():
    #     {}
    # if q.isEmpty():
    #     return True
    # return False

    # 정한님 코드.
    queue = ListQueue()
    stack = ListStack()

    for i in range:
        queue.enqueue(s[i])
        stack.push(s[i])

    while not q.isEmpty():
        if queue.dequeue() != stack.pop():
            return false

    return true

def main():
    print("Palindrome Check")
    str = 'lioninoil'
    t = isPalindrome(str)
    print(str, " is Palindrome?: ", t)

main()