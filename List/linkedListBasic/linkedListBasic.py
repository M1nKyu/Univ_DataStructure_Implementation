'''
Node Class
'''
class ListNode :
    def __init__(self, newItem, nextNode):
        self.Item = newItem
        self.next = nextNode
        

'''
Linked List Implementation
'''
class LinkedListBasic:
    # Constructer #
    def __init__(self):
        # head의 초기값은 더미 노드이며, next는 없는 상태
        self.__head = ListNode('dummy', None)
        # 노드의 수(__numItems)
        self.__numItems = 0

    # 해당 인덱스의 노드 찾기 #
    def __getNode(self, i:int) -> ListNode : # ListNode 타입을 리턴함
        curr = self.__head # 더미 헤드
        for index in range(i+1): # 더미 헤드를 제외해야하기 때문에 i+1 만큼 반복
            curr = curr.next
        return curr
    
    # 데이터값으로 노드찾기 튜플 자료형으로 리턴
    def __findNode(self, x) :
        prev = self.__head # 더미헤드
        curr = prev.next # 0번 노드
        while curr != None:
            if curr.Item == x:
                return (prev, curr)
            else:
                prev = curr; curr = curr.next
            return (None, None) 

    # 리스트가 비어있는지 확인 #
    def isEmpty(self):
        return self.__numItems == 0


    '''
    리스트에 원소 삽입
    '''
    # Insertion #
    def insert(self, i, newItem):
        # 삽입하려는 인덱스가 존재하는 인덱스일 때
        if i >= 0 and i <= self.__numItems:
            # i번째에 노드를 삽입하기 때문에 i-1번의 next를 newNode로 지정
            prev = self.__getNode(i-1) 
            # 위치 : (prev) (new) (prev.next)
            newNode = ListNode(newItem, prev.next)
            prev.next = newNode
            self.__numItems += 1
        else :
            print("index", i, "-> out of bound in insert()")

    # Append #
    def append(self, newItem):
        prev = self.__getNode(self.__numItems -1) # index 만약 3까지 있으면, 사이즈는 4다. 그래서 -1
        newNode = ListNode(newItem, prev.next)
        prev.next = newNode
        self.__numItems += 1

    '''
    리스트의 원소 삭제
    ''' 
    # pop 인덱스를 찾아 삭제 #
    def pop(self, i:int):
        if(i >= 0 and i <= self.__numItems-1):
            prev = self.__getNode(i-1) # 삭제하려는 노드(i번째노드)의 이전노드 찾음
            curr = prev.next # 삭제할 노드를 prev.next로 두고
            prev.next = curr.next # prev.next를 curr.next로 두면서, prev와 curr의 연결을 끊는다
            self.__numItems -= 1
            return curr.Item
        else: 
            return None

    # remove 값을 찾아 삭제 #
    def remove(self, x):
        (prev, curr) = self.__findNode
        if curr != None:
            prev.next = curr.next
            self.__numItems -= 1
            return x
        else:
            return None
        
    '''
    검색 메소드
    '''
    # i번 원소 알려주기 #     
    def get(self, i:int):
        if self.isEmpty():
            return None
        if (i >= 0 and i <= self.__numItems - 1):
            return self.__getNode(i).Item
        else :
            return None 
        
    # 값을 통해 index 찾기 #
    def index(self, x):
        curr = self.__head.next # 0번 노드 : 더미 헤드 다음 노드
        for i in range(self.__numItems):
            if curr.Item == x:
                return i
            else:
                curr = curr.next
        return -2 # 안쓰는 인덱스
    
    '''
    기타 메소드
    '''
    # 리스트 크기 리턴 #
    def size(self):
        return self.__numItems
    
    # 리스트 비우기, 리스트 초기화 #
    def clear(self):
        self.__head = ListNode('dummy', None)
        self.__numItems = 0

    # 리스트에 x가 몇번나오는지 카운트(리스트에 중복이 있나?..) #
    def count(self, x):
        count = 0
        curr = self.__head.next
        while curr != None:
            if curr.Item == x:
                count += 1
            curr = curr.next
        return count
    
    # 또 다른 리스트 붙여서 확장 #
    def extend(self, a): # a는 self와 같은 타입의 리스트
        for i in range(a.size()):
            self.append(a.get(i))
            
    # 리스트 복사 #
    def copy(self):
        a = LinkedListBasic()
        for i in range(self.__numItems):
            a.append(self.get(i))
        return a
    
    # 리스트 반대로 배열 #
    def reverse(self):
        a = LinkedListBasic()
        for i in range(self.__numItems):
            a.insert(0, self.get(i))
        self.clear()
        for i in range(a.__numItems):
            self.append(a.get(i))

    # sort #
    def sort(self):
        a = []
        for i in range(self.__numItems):
            a.append(self.__get(i))
        a.sort()
        self.clear()
        for i in range(len(a)):
            self.append(a[i])

    # 리스트 print # 
    def printList(self):
        curr = self.__head.next # 더미 헤드 다음 노드
        while curr != None:
            print(curr.Item, end =' ')
            curr = curr.next
        print();print()



    