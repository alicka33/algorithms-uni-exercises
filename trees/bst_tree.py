class BST_Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # def Inorder( node, Root ):
    #     if( Root is None ):
    #         return
    #     node.Inorder(Root.left)
    #     print(Root.value,end = ' ')
    #     node.Inorder(Root.right)

    def insert(self, value):
        if self is None:
            self = BST_Tree(value)
        elif value < self.value:
            if self.left is None:
                self.left = BST_Tree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST_Tree(value)
            else:
                self.right.insert(value)

    def find_node(self, searched_value):
        if self.value == searched_value:
            return self
        elif searched_value < self.value:
            if not self.left:
                return None
            return self.left.find_node(searched_value)
        else:
            if not self.right:
                return None
            return self.right.find_node(searched_value)

    def find(self, searched_value):
        if self.find_node(searched_value):
            return True
        return False

    def delete(self, buffor, value):
        if value < self.value:
            buffor = self
            self.left.delete(buffor, value)
        elif value > self.value:
            buffor = self
            self.right.delete(buffor, value)

        else:
            if self.left is None and self.right is None:
                if buffor.left == self:
                    buffor.left = None
                else:
                    buffor.right = None
                self = None

            elif self.right is None:
                if buffor.left == self:
                    buffor.left = self.left
                else:
                    buffor.right = self.left
                self = None

            elif self.left is None:
                if buffor.left == self:
                    buffor.left = self.right
                else:
                    buffor.right = self.right
                self = None

            else:
                buffor = self.right
                while buffor.left is not None:
                    buffor = buffor.left
                self.value = buffor.value
                self.right.delete(buffor, buffor.value)


# nums = [33, 13, 52, 9, 21, 61, 8, 11]

from random import randint

def generate_random_num():
    num_list = []
    for number in range(0, 10000):
        num_list.append(randint(1, 30000))
    return num_list

num_list = generate_random_num()
bst_tree = BST_Tree(num_list[0])
for num in num_list:
    bst_tree.insert(num)


# bst_tree = BST_Tree(nums[0])
# for num in nums:
#     bst_tree.insert(num)

print(bst_tree.find(30))
if bst_tree.find(30):
    bst_tree.delete(bst_tree, 30)
    print(bst_tree.find(30))
