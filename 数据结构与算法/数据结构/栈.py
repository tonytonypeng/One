# 后进先出，只能在一端操作


class Stack(object):
    def __init__(self):
        self.item = None
        self.list = []

    def push(self,item):
        """添加数据"""
        return self.list.append(item)

    def pop(self):
        """栈顶取出数据(删除)"""
        return self.list.pop()

    def peek(self):
        """栈顶取出数据"""
        return self.list[-1]

    def is_empty(self):
        """判断栈是否为空"""
        return len(self.list) is 0

    def size(self):
        """计算栈内数据个数"""
        return len(self.list)

stack = Stack()
print(stack.is_empty())
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
print(stack.is_empty())
print(stack.size())
print(stack.pop())
print(stack.peek())


