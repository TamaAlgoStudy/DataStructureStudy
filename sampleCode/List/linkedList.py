class ListNode:
    def __init__(self, value, next):
        self.val = value
        self.next = next

class LinkedListBasic:
    def __init__(self):
        self.__head = ListNode('dummy', None)
        self.__numItems = 0

    def __getNode(self, index:int) -> ListNode:
        curr = self.__head # 더미헤드
        for index in range(i+1):
            curr = curr.next
        return curr

    def __findNode(self, x) -> (ListNode, ListNode):
        prev = self.__head
        curr = prev.next
        while curr != None:
            if curr.val == x:
                return (prev, curr)
            else:
                prev = curr
                curr = curr.next

    def insert(self, index, newItem: ListNode):
        # i인덱스 값이 0보다 크고, i의 값이 전체 길이보다 작을경우 처리
        if index >= 0 and index <= self.__numItems:
            prev = self.__getNode(i - 1)
            newNode = ListNode(newItem, prev.next)
            prev.next = newNode
            # 추가가 되었으니 카운트 1
            self.__numItems += 1
        else:
            print(i, " index is Error")

    def append(self, newItem):
        prev = self.__getNode(self.__numItems - 1)
        newNode = ListNode(newItem, prev.next)
        prev.next = newNode
        # 추가가 되었으니 카운트 1
        self.__numItems += 1

    def pop(self, index):
        if (index >= 0 and index <= self.__numItems - 1):
            prev = self.__getNode(index - 1)
            curr = prev.next
            prev.next = curr.next
            retItem = curr.item
            self.__numItems -= 1
            return retItem
        else:
            print(i, " index is Error")

    def remove(self, x):
        (prev, curr) = self.findNode(x)
        if curr != None:
            prev.next = curr.next
            self.__numItems -= 1

    def get(self, index):
        if self.isEmpty():
            return None
        if (index >= 0 and index < self.__numItems - 1):
            return self.__getNode(index).val

    def isEmpty(self) -> bool:
        return self.__numItems == 0

    def size(self) -> int:
        return self.__numItems

    def clear(self):
        self.__head = ListNode("dummy", None)
        self.__numItems = 0

    def index(self, x) -> int:
        curr = self.__head.next
        for index in range(self.__numItems):
            if curr.val == x:
                return index
            else:
                curr = curr.next
        return -1

    def count(self, x) -> int:
        cnt = 0
        curr = self.__head.next
        while curr != None:
            if curr.val == x:
                cnt += 1
            curr = curr.next
        return cnt


linkedList = LinkedListBasic()


for i in range(1, 100):
    node = ListNode(i, None)
    linkedList.append(node)

print('size is : ', linkedList.size())
for i in range(11, 25):
    print(i, 'index value is : ', linkedList.get(i).val)

