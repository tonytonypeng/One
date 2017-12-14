class Node(object):
    def __init__(self,item):
        self.item = item
        self.lchild = None  # 左分支
        self.rchild = None  # 右分支


class Tree(object):
    def __init__(self):
        self.root = None  # 根

    def add(self,item):
        """添加节点"""
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = []  # 队列用来存取节点信息
        queue.append(self.root)
        while queue:
            """继续循环将左右分支下的左右分支数据取出来"""
            tmp = queue.pop(0)  # 每次都取出最左的数据
            if tmp.lchild is None:  # 首先判断左分支有没有数据
                tmp.lchild = node
                return
            elif tmp.rchild is None: # 若左分支有数据了，然后判断右分支有没有数据
                tmp.rchild = node
                return
            else:
                queue.append(tmp.lchild)  # 若左右分支都有数据了，则将左右分支添加了队列
                queue.append(tmp.rchild)

    def breath_travel(self):
        """广度遍历：从树的根节点开始，从上到下从从左到右遍历整个树的节点"""
        if self.root is None:
            return '没有数据'
        queue = []
        queue.append(self.root)
        while queue:
            tmp = queue.pop(0)
            print(tmp.item,end=' ')  # 先根
            if tmp.lchild is not None:  # 左分支
                queue.append(tmp.lchild)
            if tmp.rchild is not None:  # 右分支
                queue.append(tmp.rchild) #
        print()

    # 深度遍历：先序，中序，后序
    def pretravel(self,node):
        """先序遍历：根节点->左子树->右子树"""
        if node is None:
            return
        print(node.item,end=' ')  # 先根
        self.pretravel(node.lchild) # 再左分支
        self.pretravel(node.rchild) # 再右分支

    def intravel(self,node):
        """中序遍历：左子树->根节点->右子树"""
        if node is None:
            return
        self.intravel(node.lchild)
        print(node.item,end=' ')
        self.intravel(node.rchild)

    def posttravel(self,node):
        """后序遍历：左子树->右子树->根节点"""
        if node is None:
            return
        self.posttravel(node.lchild)
        self.posttravel(node.rchild)
        print(node.item,end=' ')

    def depth_travel(self):
        """调用深度遍历"""
        self.pretravel(self.root)
        print()
        self.intravel(self.root)
        print()
        self.posttravel(self.root)

tree = Tree()
tree.add(0)
tree.add(1)
tree.add(2)
tree.add(3)
tree.add(4)
tree.add(5)
tree.add(6)
tree.add(7)
tree.add(8)
tree.add(9)
tree.breath_travel()
tree.depth_travel()



















































