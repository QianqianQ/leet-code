#! /usr/bin/env python3

import timeit
import functools


# bubble sort
# O(N^2)
def bubble_sort(l: list) -> list:
    for i in range(len(l) - 1):
        for j in range(len(l) - 1 - i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    print(l)
    return l


# selection sort
#  O(n/2 * n) = O(n^2)
# select min value in each iteration, and put in the front
# of the unsorted array
def selection_sort(l: list) -> list:
    for i in range(len(l) - 1):
        min_index = i
        for j in range(i + 1, len(l)):
            if l[j] < l[min_index]:
                min_index = j
        l[i], l[min_index] = l[min_index], l[i]
    print(l)


# Insertion sort
#  O(n/2 * n) = O(n^2)
def insertion_sort(l: list) -> list:
    for i in range(1, len(l)):
        insert_index = i
        current_value = l[i]
        for j in range(i - 1, -1, -1):
            if l[j] > current_value:
                insert_index = j
                l[j + 1] = l[j] 
            else:
                break
        l[insert_index] = current_value
    print(l)


# execution_time = timeit.timeit(lambda: bubble_sort(l), number=1)
# Create a partial function with arguments
l = [10, 9, 8, 3, 4, 5]
partial_func = functools.partial(insertion_sort, l)
execution_time = timeit.timeit(partial_func, number=1)
print(f"Execution time: {execution_time:.6f} seconds")
