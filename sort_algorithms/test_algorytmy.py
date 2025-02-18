from algorytmy import bublesort, selectionsort
from algorytmy import mergesort, quicksort


def test_bubblesort():
    table = [1, -9, 78, 14, 5]
    assert bublesort(table) == [-9, 1, 5, 14, 78]


def test_bubblesort_2():
    table = [1, -9, 78, 14, 0, -9.8]
    assert bublesort(table) == [-9.8, -9, 0, 1, 14, 78]


def test_bubblesort_3():
    table = []
    assert bublesort(table) == []


def test_bubblesort_4():
    table = [1, -3, 5, -3]
    assert bublesort(table) == [-3, -3, 1, 5]


def test_bubblesort_5():
    table = ['ma', 'ala', 'kota', 'a', 'abb', 'ab']
    assert bublesort(table) == ['a', 'ab', 'abb', 'ala', 'kota', 'ma']


def test_selectionsort():
    table = [1, -9, 78, 14, 5]
    assert selectionsort(table) == [-9, 1, 5, 14, 78]


def test_selectionsort_2():
    table = [1, -9, 78, 14, 0, -9.8]
    assert selectionsort(table) == [-9.8, -9, 0, 1, 14, 78]


def test_selectionsort_3():
    table = []
    assert selectionsort(table) == []


def test_selectionsort_4():
    table = [1, -3, 5, -3]
    assert selectionsort(table) == [-3, -3, 1, 5]


def test_selectionsort_5():
    table = ['ma', 'ala', 'kota', 'a', 'abb', 'ab']
    assert selectionsort(table) == ['a', 'ab', 'abb', 'ala', 'kota', 'ma']


def test_mergesort():
    table = [1, -9, 78, 14, 5]
    assert mergesort(table) == [-9, 1, 5, 14, 78]


def test_mergesort_2():
    table = [1, -9, 78, 14, 0, -9.8]
    assert mergesort(table) == [-9.8, -9, 0, 1, 14, 78]


def test_mergesort_3():
    table = []
    assert mergesort(table) == []


def test_mergesort_4():
    table = [1, -3, 5, -3]
    assert mergesort(table) == [-3, -3, 1, 5]


def test_mergesort_5():
    table = ['ma', 'ala', 'kota', 'a', 'abb', 'ab']
    assert mergesort(table) == ['a', 'ab', 'abb', 'ala', 'kota', 'ma']


def test_quicksort():
    table = [1, -9, 78, 14, 5]
    assert quicksort(table) == [-9, 1, 5, 14, 78]


def test_quicksort_2():
    table = [1, -9, 78, 14, 0, -9.8]
    assert quicksort(table) == [-9.8, -9, 0, 1, 14, 78]


def test_quicksort_3():
    table = []
    assert quicksort(table) == []


def test_quicksort_4():
    table = [1, -3, 5, -3]
    assert quicksort(table) == [-3, -3, 1, 5]


def test_quicksort_5():
    table = ['ma', 'ala', 'kota', 'a', 'abb', 'ab']
    assert quicksort(table) == ['a', 'ab', 'abb', 'ala', 'kota', 'ma']
