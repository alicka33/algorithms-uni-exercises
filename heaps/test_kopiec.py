from kopiec import Kopiec


def test_table():
    lista = [6, 7, 9, 3, 5, 4, 3, 25, 12, 11, 8, 10]
    kop = Kopiec(lista[0], 2)
    for num in range(1, len(lista)):
        kop.push(lista[num])
    assert kop.table == [25, 12, 10, 9, 11, 7, 3, 3, 6, 5, 8, 4]


def test_num_of_leafs():
    lista = [6, 7, 9, 3, 5, 4, 3, 25, 12, 11, 8, 10]
    kop = Kopiec(lista[0], 2)
    assert kop.numbers_of_leafs == 2


def test_push():
    lista = [6, 7, 9, 3, 5, 4, 3, 25, 12, 11, 8, 10]
    kop = Kopiec(lista[0], 2)
    for num in range(1, len(lista)):
        kop.push(lista[num])
    assert kop.table == [25, 12, 10, 9, 11, 7, 3, 3, 6, 5, 8, 4]
    kop.push(13)
    assert kop.table == [25, 12, 13, 9, 11, 10, 3, 3, 6, 5, 8, 4, 7]


def test_push2():
    lista = [6, 7, 9, 3, 5, 4, 3, 25, 12, 11, 8, 10]
    kop = Kopiec(lista[0], 2)
    for num in range(1, len(lista)):
        kop.push(lista[num])
    assert kop.table == [25, 12, 10, 9, 11, 7, 3, 3, 6, 5, 8, 4]
    kop.push(5)
    assert kop.table == [25, 12, 10, 9, 11, 7, 3, 3, 6, 5, 8, 4, 5]


def test_pop_root():
    lista = [6, 7, 9, 3, 5, 4, 3, 25, 12, 11, 8, 10]
    kop = Kopiec(lista[0], 2)
    for num in range(1, len(lista)):
        kop.push(lista[num])
    assert kop.table == [25, 12, 10, 9, 11, 7, 3, 3, 6, 5, 8, 4]
    kop.pop_root()
    assert kop.table == [12, 11, 10, 9, 8, 7, 3, 3, 6, 5, 4]
