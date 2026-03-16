import numpy as np

# Exercise 8.1

a = np.linspace(0.0, 1.0, 11)
b = np.zeros((5, 6), dtype="i1")
c = complex(0, 1) * np.arange(9)

print(f"first: {a}")
print(f"second: {b}")
print(f"third: {c}")

# Exercise 8.2

v1 = np.arange(10, 20)
v2 = v1[1::2]
v3 = v1[::-1]

print(f"first: {v1}")
print(f"second: {v2}")
print(f"third: {v3}")
# Exercise 8.3

m1 = np.arange(20).reshape(4, 5)
m2 = m1[:, ::-1]
m3 = m1[::-1, :]
m4 = m1[1:-1, 1:-1]

print(f"first: {m1}")
print(f"second: {m2}")
print(f"third: {m3}")
print(f"fourth: {m4}")
