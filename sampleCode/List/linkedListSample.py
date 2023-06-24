class ListNode:
    def __init__(self, value, next):
        self.val = value
        self.next = next

head = ListNode(0, None) # { val: 0, next: None}
current = head # 메모리 주소를 참조.

for i in range(1, 11):
    new_node = ListNode(i, None) # { val: i, next: None}
    current.next = new_node # { val: 0, next: { val: i, next: None}}
    current = new_node

current = head

# current = { val: 0, next: { val: 1, next: { val: 20, next: None}}}

while current is not None:
    print(current.val)
    current = current.next
    # { val: 0, next: { val: 1, next: { val: 20, next: None}}}
    # { val: 1, next: { val: 2, next: None}}
    # { val: 2, next: None}
