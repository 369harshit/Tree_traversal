class Tree:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def create_node(self, value):
        if self.value is None:
            self.value = value
        else:
            if value < self.value:
                if self.left is None:
                    self.left = Tree(value)
                else:
                    self.left.create_node(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Tree(value)
                else:
                    self.right.create_node(value)

    def find_height(self, Root):
        if Root is None:
            return 0
        else:
            l_subtree = self.find_height(Root.left)
            r_subtree = self.find_height(Root.right)
            return max(l_subtree, r_subtree) + 1

    def level_order(self, Root):

        height = self.find_height(Root)
        for i in range(0, height):
            self.traversal(Root, i)

    def traversal(self, Root, level):
        if Root is None:
            return
        elif level == 0:
            print(Root.value, end=' ')
        elif level > 0:
            self.traversal(Root.left, level - 1)
            self.traversal(Root.right, level - 1)


Root = Tree(5)
Root.create_node(7)
Root.create_node(2)
Root.create_node(3)
Root.create_node(6)
Root.create_node(1)
Root.create_node(8)
print('Level order traversal :', end='')
Root.level_order(Root)


# DFS in tree traversal can be of three types:
# [1] In-order traversal.

# [2] Pre-order traversal.

# [3] Post-order traversal.
