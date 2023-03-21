from linkedListBasic import *

list = LinkedListBasic()
list.append(30)
list.insert(0, 20)
list.printList()

a = LinkedListBasic()
a.append(4); a.append(3); a.append(3); a.append(2); a.append(1)
a.printList()

list.extend(a)
list.printList()

list.reverse()
list.printList()

list.pop(0) # 0번째 pop
list.printList()

print("3의 개수:", list.count(3))
print("3번 인덱스의 값:", list.get(3))