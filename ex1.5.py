import time
import matplotlib.pyplot as plt

def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)

def memoized_func(n, memo={}):
    if n in memo:
        return memo[n]
    elif n == 0 or n == 1:
        memo[n] = n
        return n
    else:
        memo[n] = memoized_func(n-1, memo) + memoized_func(n-2, memo)
        return memo[n]

results = []
memoized_results = []
for n in range(36):
    start_time = time.time()
    result = func(n)
    elapsed_time = time.time() - start_time
    results.append(elapsed_time)

    start_time = time.time()
    memoized_result = memoized_func(n)
    elapsed_time = time.time() - start_time
    memoized_results.append(elapsed_time)

plt.plot(range(36), results, label='original')
plt.plot(range(36), memoized_results, label='memoized')
plt.legend()
plt.xlabel('n')
plt.ylabel('time (s)')
plt.show()
