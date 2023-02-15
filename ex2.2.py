import matplotlib.pyplot as plt, json, time, sys

sys.setrecursionlimit(20000)
def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)
def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high


if __name__ == '__main__':
    with open("ex2.json", "r") as read:
        data = json.load(read)
    x = [i for i in range(len(data))]
    y = []
    for i, test_inputs in enumerate(data):
        arr = test_inputs
        start = time.time()
        func1(arr, 0, len(arr) - 1)
        end = time.time()
        y.append(end - start)

    plt.plot(x, y)
    plt.xlabel('Test Input numbers (in 1000s)')
    plt.ylabel('Time taken (seconds)')
    plt.title('QuickSort Timing Results')
    plt.show()