from drzewo_bst import BST_Tree


def test_find_true():
    lista = [0, 3, 5, 6, 2, 1, 7, 4]
    tree = BST_Tree(lista[0])
    for num in lista:
        tree.insert(num)
    assert tree.Root_Node.find(3)


def test_find_false():
    lista = [0, 3, 5, 6, 2, 1, 7, 4]
    tree = BST_Tree(lista[0])
    for num in lista:
        tree.insert(num)
    assert not tree.Root_Node.find(55)


def test_delete():
    lista = [0, 3, 5, 6, 2, 1, 7, 4]
    tree = BST_Tree(lista[0])
    for num in lista:
        tree.insert(num)
    assert tree.Root_Node.find(3)
    tree.delete(3)
    assert not tree.Root_Node.find(3)


def test_value():
    lista = [5, 3]
    tree = BST_Tree(lista[0])
    for num in lista:
        tree.insert(num)
    assert tree.Root_Node.value == 5


def test_left():
    lista = [5, 3]
    tree = BST_Tree(lista[0])
    for num in lista:
        tree.insert(num)
    assert tree.Root_Node.left.value == 3


def test_left_right():
    lista = [33, 13, 52, 8, 15, 40, 55]
    tree = BST_Tree(lista[0])
    for num in lista:
        tree.insert(num)
    assert tree.Root_Node.left.right.value == 15


def test_right_right():
    lista = [33, 13, 52, 8, 15, 40, 55]
    tree = BST_Tree(lista[0])
    for num in lista:
        tree.insert(num)
    assert tree.Root_Node.right.right.value == 52


def test_parent():
    lista = [5, 3]
    tree = BST_Tree(lista[0])
    for num in lista:
        tree.insert(num)
    assert tree.Root_Node.left.parent.value == 5
