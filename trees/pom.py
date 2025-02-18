import time
import gc
from random import randint
import numpy as np
import matplotlib.pyplot as plt

from bst_tree import BST_Tree
from drzewo_avl import AVL_Tree


def generate_random_num():
    num_list = []
    for number in range(0, 100):
        num_list.append(randint(1, 30000))
    return num_list


def get_avl_time_insert(numbers):
    gc_old = gc.isenabled()
    gc.disable()
    start = time.process_time()

    avl_tree = AVL_Tree()
    root = None
    for num in numbers:
        root = avl_tree.insert_node(root, num)

    stop = time.process_time()
    if gc_old:
        gc.enable()
    return stop - start


def get_bst_time_insert(numbers):
    gc_old = gc.isenabled()
    gc.disable()
    start = time.process_time()

    bst_tree = BST_Tree(numbers[0])
    for num in numbers:
        bst_tree.insert(num)

    stop = time.process_time()
    if gc_old:
        gc.enable()
    return stop - start


def get_avl_time_delete(numbers, how_many):
    avl_tree = AVL_Tree()
    root = None
    for num in numbers:
        root = avl_tree.insert_node(root, num)

    gc_old = gc.isenabled()
    gc.disable()
    start = time.process_time()

    for i in range(0, how_many):
        avl_tree.delete_node(root, numbers[i])

    stop = time.process_time()
    if gc_old:
        gc.enable()
    return stop - start


def get_bst_time_delete(numbers, how_many):
    bst_tree = BST_Tree(numbers[0])
    for num in numbers:
        bst_tree.insert(num)

    gc_old = gc.isenabled()
    gc.disable()
    start = time.process_time()

    for i in range(0, how_many):
        bst_tree.delete(bst_tree, numbers[i])

    stop = time.process_time()
    if gc_old:
        gc.enable()
    return stop - start


def get_bst_time_find(numbers, how_many):
    bst_tree = BST_Tree(numbers[0])
    for num in numbers:
        bst_tree.insert(num)

    gc_old = gc.isenabled()
    gc.disable()
    start = time.process_time()

    for i in range(0, how_many):
        bst_tree.find(numbers[i])

    stop = time.process_time()
    if gc_old:
        gc.enable()
    return stop - start


def get_avl_time_find(numbers, how_many):
    avl_tree = AVL_Tree()
    root = None
    for num in numbers:
        root = avl_tree.insert_node(root, num)

    gc_old = gc.isenabled()
    gc.disable()
    start = time.process_time()

    for i in range(0, how_many):
        avl_tree.find(root, numbers[i])

    stop = time.process_time()
    if gc_old:
        gc.enable()
    return stop - start


def measure_times_of_inserting(numbers, ranges):
    bst_time_insert = []
    avl_time_insert = []
    for num in ranges:
        bst_time_insert.append(get_bst_time_insert(numbers))
        avl_time_insert.append(get_avl_time_insert(numbers))
    return bst_time_insert, avl_time_insert


def measure_times_of_deleting(numbers, ranges):
    bst_time_delete = []
    avl_time_delete = []
    for num in ranges:
        bst_time_delete.append(get_bst_time_delete(numbers, num))
        avl_time_delete.append(get_avl_time_delete(numbers, num))
    return bst_time_delete, avl_time_delete


def measure_times_of_finding(numbers, ranges):
    bst_time_find = []
    avl_time_find = []
    for num in ranges:
        bst_time_find.append(get_bst_time_find(numbers, num))
        avl_time_find.append(get_avl_time_find(numbers, num))
    return bst_time_find, avl_time_find


def make_bar_plot(bst_data, avl_data, ranges, name_of_algorith):
    X_axis = np.arange(len(ranges))
    plt.bar(X_axis - 0.2, bst_data, 0.4, label='BST_Tree')
    plt.bar(X_axis + 0.2, avl_data, 0.4, label='AVL_Tree')
    plt.xticks(X_axis, ranges)
    plt.xlabel("Number of elements")
    plt.ylabel("Time")
    plt.title(name_of_algorith)
    plt.legend()
    plt.show()
    # plt.savefig(name_of_algorith+'.png')


if __name__ == "__main__":
    # ranges = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    ranges = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    numbers = generate_random_num()
    # ranges = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # numbers = [0, 3, 5, 6, 2, 1, 7, 4, 8, 9]
    bst_time_insert, avl_time_insert = measure_times_of_inserting(numbers,
                                                                  ranges)
    bst_time_delete, avl_time_delete = measure_times_of_deleting(numbers,
                                                                 ranges)
    bst_time_find, avl_time_find = measure_times_of_finding(numbers, ranges)
    # print(bst_time_insert, avl_time_insert)
    # print(bst_time_delete, avl_time_delete)
    # print(bst_time_find, avl_time_find)
    make_bar_plot(bst_time_insert, avl_time_insert, ranges, "Insertion time")
    make_bar_plot(bst_time_delete, avl_time_delete, ranges, "Deleting time")
    make_bar_plot(bst_time_find, avl_time_find, ranges, "Finding time")
