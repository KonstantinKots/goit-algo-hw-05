
def genner(n):
    for i in range(n):
        yield i

def sumprof(num, func):
    return sum(func(num))

print(sumprof(10, genner))

