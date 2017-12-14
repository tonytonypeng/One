# 单链表，数据+下一个节点的地址

import time


class Node(object):
    """创建节点类"""
    def __init__(self,item):
        """next用于存储下一节点信息，item用于存储数据"""
        self._next = None
        self.item = item


class Singlelist(object):
    """创建单链表类"""
    def __init__(self):
        """head为链表头"""
        self.head = None
        self.list = []  # 用来计算链表的长度

    def add(self,node):
        """正常添加节点"""
        if self.head is None:
            """刚添加节点，头部还没有存储节点信息"""
            self.head = node
            self.list.append(1)
        else:
            node._next = self.head
            self.head = node
            self.list.append(1)

    def length(self):
        """遍历链表节点并打印"""
        cur = self.head
        while cur is not None:
            """头部不为空时"""
            print(cur.item,end=' ')
            time.sleep(0.1)
            cur = cur._next
            if cur._next is None:
                """当遍历到最后一个节点时"""
                print(cur.item,end=' ')
                break
        print()

    def append(self,node):
        """尾部添加节点"""
        if self.head is None:
            self.list.append(1)
            self.head = node
            return

        elif self.head._next is None:

            self.head._next = node

        else:
            self.list.append(1)
            cur = ''
            cur = self.head
            while cur._next is not None:
                cur = cur._next
            cur._next = node

    def insert(self,addr,node):
        """按指定位置插入节点"""
        if addr <= 0:  # 当指定位置小于等于0时，默认从头部添加
            self.list.append(1)
            if self.head is not None:
                node._next = self.head
                self.head = node
                return
            self.head = node

        elif addr >= len(self.list):   # 当指定位置大于等于链表长度时，默认从尾部添加
            self.list.append(1)
            cur = ''
            cur = self.head
            while cur._next is not None:
                cur = cur._next
            cur._next = node

        else:  # 正常情况下
            self.list.append(1)
            cur = ''
            n = 0
            pre = ''
            cur = self.head
            while n < addr:
                pre = cur
                cur = cur._next
                n += 1
            node._next = cur
            pre._next = node

    def remove(self,addr):
        """指定位置删除节点"""
        if addr <= 0:  # 当指定位置小于等于0时，默认将头部删除
            self.head = self.head._next
            self.list.pop()

        elif addr >= len(self.list):   # 当指定位置大于等于链表长度时，默认将尾部删除
            pass

        else:  # 正常情况下
            pass


sll = Singlelist()
node = Node(2)
sll.add(node)
node = Node(3)
sll.add(node)
node = Node(4)
sll.add(node)
node = Node(1)
sll.append(node)
node = Node(6)
sll.add(node)
node = Node(7)
sll.add(node)
sll.length()

node = Node(5)
sll.insert(2,node)
sll.length()

sll.remove(0)
sll.length()










