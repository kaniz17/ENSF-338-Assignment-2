def func(n, memory={}):
    if n in memory:
        return memory[n]
        
    elif n == 0 or n == 1:
        return n

    memory[n] = func(n-1, memory) + func(n-2, memory)
    return memory[n]