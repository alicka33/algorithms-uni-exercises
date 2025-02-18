from copy import copy


def bublesort(table):
    sort_table = copy(table)
    flag = True
    while flag:
        flag = False
        for i in range(len(sort_table)-1):
            if sort_table[i] > sort_table[i+1]:
                sort_table[i], sort_table[i+1] = sort_table[i+1], sort_table[i]
                flag = True
    return sort_table


def selectionsort(table):
    sort_table = copy(table)
    for i in range(len(sort_table)-1):
        min_ind = i
        min_val = sort_table[i]
        for j in range(i+1, len(sort_table)):
            if min_val > sort_table[j]:
                min_val = sort_table[j]
                min_ind = j
        sort_table[i], sort_table[min_ind] = sort_table[min_ind], sort_table[i]
    return sort_table


def merge(table1, table2):
    ind1 = 0
    ind2 = 0
    table = []
    for i in range(len(table1)+len(table2)):
        if ind1 >= len(table1):
            table = table + table2[ind2:]
            break
        elif ind2 >= len(table2):
            table = table + table1[ind1:]
            break
        else:
            if table1[ind1] > table2[ind2]:
                table.append(table2[ind2])
                ind2 += 1
            else:
                table.append(table1[ind1])
                ind1 += 1
    return table


def mergesort(table):
    if len(table) == 1 or len(table) == 0:
        return table

    middle = int(len(table)/2)

    tab1 = table[0:middle]
    tab2 = table[middle:]

    tab1 = mergesort(tab1)
    tab2 = mergesort(tab2)

    return merge(tab1, tab2)


def quicksort_alg(table, left_ind, right_ind):
    i = left_ind
    j = right_ind
    pivot = table[int((i+j)/2)]

    while i <= j:
        while table[i] < pivot:
            i += 1
        while table[j] > pivot:
            j -= 1
        if i <= j:
            table[i], table[j] = table[j], table[i]
            i += 1
            j -= 1

    if left_ind < j:
        quicksort_alg(table, left_ind, j)
    if i < right_ind:
        quicksort_alg(table, i, right_ind)


def quicksort(table):
    if len(table) == 0:
        return table
    sort_table = copy(table)
    quicksort_alg(sort_table, 0, len(sort_table)-1)
    return sort_table


if __name__ == "__main__":

    ta = [2, 4, 6, 7, 3, 5, 1]

    print("Bubblesort:")
    print(bublesort(ta))
    print(ta)
    ta = [2, 4, 6, 7, 3, 5, 1]

    print("Selectionsort:")
    print(selectionsort(ta))
    print(ta)
    ta = [2, 4, 6, 7, 3, 5, 1]

    print("Mergesort:")
    print(mergesort(ta))
    print(ta)
    ta = [2, 4, 6, 7, 3, 5, 1]

    print("Quicksort:")
    print(quicksort(ta))
    print(ta)
    ta = [2, 4, 6, 7, 3, 5, 1]
