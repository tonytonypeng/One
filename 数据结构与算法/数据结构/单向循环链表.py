import time


class Node(object):
    def __init__(self,item):
        self.item = item
        self.next = None


class Singlexunhuanlist(object):
    def __init__(self):
        self.head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self.head is None

    def length(self):
        """计算链表长度"""
        if self.is_empty():
            print(0)
            return

        cur = self.head
        count = 1
        while cur.next is not self.head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        if self.is_empty():
            print('空链表')
            return

        cur = self.head
        while cur.next is not self.head:
            print(cur.item,end=' ')
            cur = cur.next
        print(cur.item)
        print()

    def add(self,item):
        """从头部添加节点"""
        node = Node(item)
        if self.is_empty():
            self.head = node
            node.next = self.head
            return

        cur = self.head
        while cur.next is not self.head:
            cur = cur.next

        node.next = self.head
        self.head = node
        cur.next = self.head

    def append(self,item):
        """从尾部添加节点"""
        node = Node(item)
        if self.is_empty():
            self.head = node
            node.next = self.head
            return

        cur = self.head
        while cur.next is not self.head:
            cur = cur.next
        node.next = self.head
        cur.next = node

    def insert(self,addr,item):
        """任意位置插入节点"""
        node = Node(item)
        if self.is_empty():
            self.head = node
            node.next = self.head
            return

        if addr <= 0:
            """默认从头部插入"""
            cur = self.head
            while cur.next is not self.head:
                cur = cur.next

            node.next = self.head
            self.head = node
            cur.next = self.head

        elif addr >= self.length():
            """默认从尾部插入"""
            cur = self.head
            while cur.next is not self.head:
                cur = cur.next
            node.next = self.head
            cur.next = node

        else:
            cur = self.head
            count = 0
            while count < (addr-1):
                cur = cur.next
                count += 1
            node.next = cur.next
            cur.next = node

    def remove(self,item):
        if self.is_empty():
            print('空链表不能删除')
            return

        cur = self.head
        while cur.next is not self.head:
            if cur.item == item:  # 当要删除的节点正好是头部节点时
                pre = cur
                while cur.next is not self.head:
                    cur = cur.next
                cur.next = pre.next
                pre.next = None
                self.head = cur.next
                return

            self.pre = cur
            cur = cur.next
            if cur.item == item:   # 链表中间节点
                self.pre.next = cur.next
                cur.next = None
                return

        if cur.item == item:   # 当要删除的节点正好是尾部节点时
            self.pre.next = cur.next
            cur.next = None
            return

        print('没找到你要删除的节点')

    def search(self,item):
        if self.is_empty():
            print('空链表')
            return

        cur = self.head
        while cur.next is not self.head:
            if cur.item == item:  # 有可能要查找的正好是头节点
                print(cur.item)
                return
            cur = cur.next

        if cur.item == item: # 要查找的正好为尾节点
            print(cur.item)
            return

        print('没找到你要找的节点')


sxl = Singlexunhuanlist()
sxl.add(1)
sxl.add(2)
sxl.add(3)
sxl.add(4)
sxl.append(5)
sxl.travel()
sxl.insert(2,6)
sxl.travel()
sxl.search(5)























