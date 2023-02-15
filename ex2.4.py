import sys

sys.setrecursionlimit(20000)

def choose_pivot(array, low, high):
    mid = low + (high - low) // 2
    pivot = high
    if array[low] < array[mid]:
        if array[mid] < array[high]:
            pivot = mid
    elif array[low] < array[high]:
        pivot = low
    return pivot

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    pivot_index = choose_pivot(array, start, end)
    array[start], array[pivot_index] = array[pivot_index], array[start]
    pivot = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1
        while low <= high and array[low] <= pivot:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high