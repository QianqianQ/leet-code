#! /usr/bin/env python3

import timeit
import functools


# bubble sort
# O(N^2)
def bubble_sort(lst: list[float | int]) -> list[float | int]:
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


# selection sort
#  O(n/2 * n) = O(n^2)
# select min value in each iteration, and put in the front
# of the unsorted array
def selection_sort(lst: list[float | int]) -> list[float | int]:
    for i in range(len(lst) - 1):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst


# Insertion sort
#  O(n/2 * n) = O(n^2)
def insertion_sort(lst: list[float | int]) -> list[float | int]:
    # Start from the second element (index 1) and treat the first element as sorted
    for i in range(1, len(lst)):
        j = i - 1
        value = lst[i]

        # Compare the selected element with the previous elements in the sorted portion
        # until an element smaller than it is found
        # For descending order, change value < lst[j] to value > lst[j]
        while j >= 0 and value < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1

        # Place key at after the element just smaller than it.
        lst[j + 1] = value
    return lst


# execution_time = timeit.timeit(lambda: bubble_sort(l), number=1)
# Create a partial function with arguments
l = [10, 9, 8, 3, 4, 5]
partial_func = functools.partial(insertion_sort, l)
execution_time = timeit.timeit(partial_func, number=1)
print(f"Execution time: {execution_time:.6f} seconds")
