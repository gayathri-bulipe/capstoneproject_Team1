def demo():
    yield 'A'
    yield 'B'
    yield 'C'
    yield 'D'
x=demo()
print(next(x))
print(next(x))
print(next(x))


num=[x*x for x in range(1000)]
print(num)