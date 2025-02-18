import time
import gc
import numpy as np
import matplotlib.pyplot as plt

from algorytmy import quicksort, bublesort, mergesort, selectionsort


def time_measurement(sort_function, table):
    gc_old = gc.isenabled()  # pobierz aktualny stan odśmiecania
    gc.disable()  # wyłącz odśmiecanie

    start = time.process_time()

    sort_function(table)

    stop = time.process_time()
    if gc_old:
        gc.enable()  # przywróć pierwotny stan odśmiecania

    return stop - start


def word_file(path, number_of_words):
    with open(path) as file:
        return file.read().split()[:number_of_words]


def measure_times_of_sort(numbers_of_words, path):

    quicksort_times = []
    mergesort_times = []
    selectionsort_times = []
    bublesort_times = []

    for n in numbers_of_words:
        pan_tadeusz = word_file(path, n)
        quicksort_times.append(time_measurement(quicksort, pan_tadeusz))
        mergesort_times.append(time_measurement(mergesort, pan_tadeusz))
        selectionsort_times.append(time_measurement(selectionsort, pan_tadeusz))
        bublesort_times.append(time_measurement(bublesort, pan_tadeusz))

    return quicksort_times, mergesort_times, selectionsort_times, bublesort_times


def make_bar_plot(sort_times, numbers_of_words, name_of_algorith):
    y_pos = np.arange(len(sort_times))

    plt.figure(figsize=(10, 5))

    plt.bar(y_pos, sort_times, color='#7070ff')

    plt.xticks(y_pos, numbers_of_words)

    plt.xlabel('Długość listy', fontsize=12, color='#323232')
    plt.ylabel('Czas sortowania [sekundy]', fontsize=12, color='#323232')
    plt.title(name_of_algorith, fontsize=16, color='#323232')

    plt.savefig(name_of_algorith+'.png')


if __name__ == "__main__":
    path = 'pan-tadeusz-unix.txt'
    numbers_of_words = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

    quicksort_times, mergesort_times, selectionsort_times, bublesort_times = measure_times_of_sort(numbers_of_words, path)

    make_bar_plot(quicksort_times, numbers_of_words, 'Quicksort')
    make_bar_plot(mergesort_times, numbers_of_words, 'Mergesort')
    make_bar_plot(selectionsort_times, numbers_of_words, 'Selectionsort')
    make_bar_plot(bublesort_times, numbers_of_words, 'Bublesort')
