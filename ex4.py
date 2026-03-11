# Exercise 4.1

points = [(1, 2), (3, 4), (0.1, 0), (0.3, -0.4)]

# (a)

print(list(filter(lambda p: p[0] * p[0] + p[1] * p[1] <= 1, points)))

# (b)

print(list(filter(lambda p: p[0] > 0 and p[1] > 0, points)))

# (c)

print(points.sort(key=lambda p: (-p[1], p[0])))

# (d)

print(points.sort(key=lambda p: abs(p[0]) + abs(p[1])))

# Exercise 4.2

L = [i for i in range(0, 10)]

def reverse_range(L, a, b):
    while a < b:
        L[a], L[b] = L[b], L[a]
        a = a + 1
        b = b - 1

def reverse_two(L, a, b):
    if a >= b:
        return
    L[a], L[b] = L[b], L[a]
    reverse_two(L, a + 1, b - 1)

reverse_range(L, 3, 6)
print(L)

reverse_two(L, 1, 3)
print(L)

# Exercise 4.3

# (a)

def iter_even():
    n = 0
    while 1:
        yield n
        n = n + 2

# (b)

def iter_odd():
    n = 1
    while 1:
        yield n
        n = n + 2

# (c)

def iter_power(k):
    p = 1
    while 1:
        yield p
        p = p * k

rt = iter_even()
iter_even()
print(iter_even())
print(rt)

iter_odd()
iter_odd()
print(iter_odd())

iter_power(1)
iter_power(1)
print(iter_power(1))

iter_power(3)
iter_power(3)
iter_power(3)
iter_power(3)
print(iter_power(3))
