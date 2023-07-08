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

