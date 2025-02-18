class BST_Node:

    def __init__(self, value, parent_node):
        self.left = None
        self.right = None
        self.parent = parent_node
        self.value = value

    def insert(self, next_value):
        if next_value < self.value:
            if self.left is None:
                self.left = BST_Node(next_value, self)
            else:
                self.left.insert(next_value)
        else:
            if self.right is None:
                self.right = BST_Node(next_value, self)
            else:
                self.right.insert(next_value)

    def find_node(self, searching_value):
        if searching_value == self.value:
            return self
        elif searching_value < self.value:
            if self.left is None:
                return None
            else:
                return self.left.find_node(searching_value)
        else:
            if self.right is None:
                return None
            else:
                return self.right.find_node(searching_value)

    def find(self, searching_value):
        if self.find_node(searching_value) is not None:
            return True
        return False

    def min_node(self):
        smallest_node = self
        while smallest_node.left is not None:
            smallest_node = smallest_node.left
        return smallest_node

    def max_node(self):
        biggest_node = self
        while biggest_node.right is not None:
            biggest_node = biggest_node.right
        return biggest_node

    def min(self):
        return self.min_node().value

    def max(self):
        return self.max_node().value

    def swap_value(self, node):
        my_value = self.value

        self.value = node.value

        node.value = my_value

    def delete(self, value):
        node_to_delete = self.find_node(value)
        print(node_to_delete)
        self.delete_node(node_to_delete)

    def delete_node(self, node):
        if node:
            if node.parent is None:
                if not node.has_any_kid():
                    node = None
                elif node.has_one_kid():
                    if node.has_right():
                        node.right.parent = None
                    else:
                        node.left.parent = None
                else:
                    min_right_node = node.right.min_node()
                    node.swap_value(min_right_node)
                    node.delete_node(min_right_node)

            else:
                if not node.has_any_kid():
                    if node.i_am_right():
                        node.parent.right = None
                    else:
                        node.parent.left = None

                    node = None

                elif node.has_one_kid():
                    if node.i_am_right():
                        if node.has_right():
                            node.right.parent = node.parent
                            node.parent.right = node.right
                        else:
                            node.left.parent = node.parent
                            node.parent.right = node.left
                    else:
                        if node.has_right():
                            node.right.parent = node.parent
                            node.parent.left = node.right
                        else:
                            node.left.parent = node.parent
                            node.parent.left = node.left
                    node = None

                else:
                    min_right_node = node.right.min_node()
                    node.swap_value(min_right_node)
                    node.delete_node(min_right_node)

    def has_any_kid(self):
        if (self.left is not None) or (self.right is not None):
            return True
        return False

    def has_two_kid(self):
        if (self.left is not None) and (self.right is not None):
            return True
        return False

    def has_one_kid(self):
        if (self.left is None) ^ (self.right is None):
            return True
        return False

    def has_right(self):
        if (not self.right):
            return False
        return True

    def has_left(self):
        if (not self.left):
            return False
        return True

    def i_am_right(self):
        if self.parent is None:
            return False
        if self.parent.right == self:
            return True
        return False


class BST_Tree:
    def __init__(self, start_value):
        self.Root_Node = BST_Node(start_value, None)
        self.size = 1
        self.list_of_level = []

    def insert(self, next_value):
        self.Root_Node.insert(next_value)
        self.size += 1

    def delete(self, value_to_delete):
        if self.Root_Node:
            self.Root_Node.delete(value_to_delete)

            if self.Root_Node.value == value_to_delete:
                if not self.Root_Node.has_any_kid():
                    self.Root_Node = None
                elif self.Root_Node.has_one_kid():
                    if self.Root_Node.has_right():
                        self.Root_Node = self.Root_Node.right
                    else:
                        self.Root_Node = self.Root_Node.left
                else:
                    min_right_node = self.Root_Node.right.min_node()
                    self.Root_Node = min_right_node

    def levels(self, start_node, level):
        if level >= len(self.list_of_level):
            list = []
            self.list_of_level.append(list)

        if start_node is None:
            self.list_of_level[level].append(None)
            return
        else:
            self.list_of_level[level].append(start_node.value)
            self.levels(start_node.left, level+1)
            self.levels(start_node.right, level+1)

    def refresh_levels(self):
        self.list_of_level = []
        self.levels(self.Root_Node, 0)

    def show(self):
        self.refresh_levels()

        print(self.list_of_level)

        for line in self.list_of_level:
            to_print = ""
            for node_value in line:
                if node_value is None:
                    to_print += "   "
                else:
                    to_print += "%03d" % node_value
                to_print += "   "
            print(to_print)
