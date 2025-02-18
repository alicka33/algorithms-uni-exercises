import random

from funkcje_szukajace import find_N, find_KMP, find_KR


def test_find_N():
    assert [4] == find_N("ma", "Ala ma kota")


def test_find_N_empty():
    assert [] == find_N("", "Ala ma kota")


def test_find_N_not_in():
    assert [] == find_N("kasia", "Ala ma kota")


def test_find_N_same_lenght():
    assert [0] == find_N("Ala ma kota", "Ala ma kota")


def test_find_N_string_smaller():
    assert [] == find_N("Ala ma kota", "ma")


def test_find_KMP():
    assert [4] == find_KMP("ma", "Ala ma kota")


def test_find_KMP_empty():
    assert [] == find_KMP("", "Ala ma kota")


def test_find_KMP_not_in():
    assert [] == find_KMP("kasia", "Ala ma kota")


def test_find_KMP_same_lenght():
    assert [0] == find_KMP("Ala ma kota", "Ala ma kota")


def test_find_KMP_string_smaller():
    assert [] == find_KMP("Ala ma kota", "ma")


def test_find_KR():
    assert [4] == find_KR("ma", "Ala ma kota")


def test_find_KR_empty():
    assert [] == find_KR("", "Ala ma kota")


def test_find_KR_not_in():
    assert [] == find_KR("kasia", "Ala ma kota")


def test_find_KR_same_lenght():
    assert [0] == find_KR("Ala ma kota", "Ala ma kota")


def test_find_KR_string_smaller():
    assert [] == find_KR("Ala ma kota", "ma")


def test_same_results_in_KR_KMP_N():

    alfabet = ['a', 'b']
    for i in range(10):
        text = ''.join(random.choices(alfabet, k=10))
        string = ''.join(random.choices(alfabet, k=2))
        KMP_result = find_KMP(string, text)
        KR_result = find_KR(string, text)
        N_result = find_N(string, text)
        assert N_result == KMP_result and N_result == KR_result


if __name__ == "__main__":
    test_find_N()

    test_find_N_empty()

    test_find_N_not_in()

    test_find_N_same_lenght()

    test_find_N_string_smaller()

    test_find_KMP()
    
    test_find_KMP_empty()

    test_find_KMP_not_in()

    test_find_KMP_same_lenght()

    test_find_KMP_string_smaller()

    test_find_KR()

    test_find_KR_empty()

    test_find_KR_not_in()

    test_find_KR_same_lenght()

    test_find_KR_string_smaller()

    test_same_results_in_KR_KMP_N()

    print("WSZYSTKIE TESTY PRZESZŁY")
