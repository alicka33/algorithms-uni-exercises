from drzewo_avl import AVL_Tree


def test_find_true():
    root = None
    nums = [33, 13, 52, 9, 21, 61, 8, 11]
    tree = AVL_Tree()
    for num in nums:
        root = tree.insert_node(root, num)
    assert tree.find(root, 13)


def test_find_false():
    root = None
    nums = [33, 13, 52, 9, 21, 61, 8, 11]
    tree = AVL_Tree()
    for num in nums:
        root = tree.insert_node(root, num)
    assert not tree.find(root, 3)


def test_delete():
    root = None
    nums = [33, 13, 52, 9, 21, 61, 8, 11]
    tree = AVL_Tree()
    for num in nums:
        root = tree.insert_node(root, num)
    assert tree.find(root, 13)
    tree.delete_node(root, 13)
    assert not tree.find(root, 13)


def test_value():
    root = None
    nums = [33, 13, 52]
    tree = AVL_Tree()
    for num in nums:
        root = tree.insert_node(root, num)
    assert root.value == 33


def test_left():
    root = None
    nums = [33, 13, 52]
    tree = AVL_Tree()
    for num in nums:
        root = tree.insert_node(root, num)
    assert root.left.value == 13


def test_left_2():
    root = None
    nums = [33, 13, 52, 8, 15, 40, 55]
    tree = AVL_Tree()
    for num in nums:
        root = tree.insert_node(root, num)
    assert root.left.left.value == 8


def test_right():
    root = None
    nums = [33, 13, 52]
    tree = AVL_Tree()
    for num in nums:
        root = tree.insert_node(root, num)
    assert root.right.value == 52


def test_right_left():
    root = None
    nums = [33, 13, 52, 8, 15, 40, 55]
    tree = AVL_Tree()
    for num in nums:
        root = tree.insert_node(root, num)
    assert root.right.left.value == 40


def test_height_root():
    root = None
    nums = [33, 13, 52]
    tree = AVL_Tree()
    for num in nums:
        root = tree.insert_node(root, num)
    assert root.height == 2


def test_height_right():
    root = None
    nums = [33, 13, 52]
    tree = AVL_Tree()
    for num in nums:
        root = tree.insert_node(root, num)
    assert root.right.height == 1
