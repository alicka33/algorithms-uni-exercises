class AVL_Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVL_Tree():
    def insert_node(self, root, value):
        if not root:
            return AVL_Node(value)
        elif value < root.value:
            root.left = self.insert_node(root.left, value)
        else:
            root.right = self.insert_node(root.right, value)

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balanceFactor = self.getBalance(root)
        if balanceFactor > 1:
            if value < root.left.value:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if balanceFactor < -1:
            if value > root.right.value:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root

    def find_node(self, root, searched_value):
        if root.value == searched_value:
            return root
        elif searched_value < root.value:
            if not root.left:
                return None
            return self.find_node(root.left, searched_value)
        else:
            if not root.right:
                return None
            return self.find_node(root.right, searched_value)

    def find(self, root, searched_value):
        if self.find_node(root, searched_value):
            return True
        return False

    def delete_node(self, root, value):
        if not root:
            return root
        elif value < root.value:
            root.left = self.delete_node(root.left, value)
        elif value > root.value:
            root.right = self.delete_node(root.right, value)
        else:
            if root.left is None:
                buffor = root.right
                root = None
                return buffor
            elif root.right is None:
                buffor = root.left
                root = None
                return buffor
            buffor = self.getMinValueNode(root.right)
            root.value = buffor.value
            root.right = self.delete_node(root.right,
                                          buffor.value)
        if root is None:
            return root

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balanceFactor = self.getBalance(root)

        if balanceFactor > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root

    def leftRotate(self, root):
        buffor1 = root.right
        buffor2 = buffor1.left
        buffor1.left = root
        root.right = buffor2
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))
        buffor1.height = 1 + max(self.getHeight(buffor1.left),
                                 self.getHeight(buffor1.right))
        return buffor1

    def rightRotate(self, root):
        buffor1 = root.left
        buffor2 = buffor1.right
        buffor1.right = root
        root.left = buffor2
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))
        buffor1.height = 1 + max(self.getHeight(buffor1.left),
                                 self.getHeight(buffor1.right))
        return buffor1

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

#############################################
#     def get_begining_root_file(self, root):
#         return root.height

#     def show(self, root, begining_root_height):
#         how_many_num = 2 ** (begining_root_height - root.height)
#         steps = [root.left, root.parent, root.right, root.]
#         for num in range(how_many_num):
#             for step in range(5):
#                 to_print = ""
#                 if root is None:
#                     to_print += '   '
#                 else:
#                     to_print += "%03d" % root.value

#         print(to_print)


# root = None
# nums = [33, 13, 52, 8, 15, 40, 55]
# tree = AVL_Tree()
# for num in nums:
#     root = tree.insert_node(root, num)
# begining_root_height = tree.get_begining_root_file(root)
# tree.show(root, begining_root_height)
