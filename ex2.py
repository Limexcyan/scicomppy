from random import randint

# Exervise 2.1

a = str(randint(0,10000000000))

no_zeros = 0
for letter in a:
    if letter=='0':
        no_zeros = no_zeros + 1


print(f"There is {no_zeros} zeros in {a}")

# Exercise 2.2

# Explain the results.

# Assigning 5 to variable x
x = 5

# true and (logically) 11  => 11
# return second evaluated value, as first is true
x == 5 and 3 + 8   # 11

# false and (logically) 11 => false
# code is read line by line from left to the right so
# false at the beggining always should lead to false
x == 4 and 3 + 8   # False

# 11 and (logically) true
# return second evaluated value as in first example
3 + 8 and x == 5   # True

# 11 and (logically) false => false
# return second evaluated value as above
3 + 8 and x == 4   # False

# True is 1, so True is an integer
# bool is a child class of int
isinstance(True, int)    # True

# True is boolean
# bool is an instance of class bool
isinstance(True, bool)   # True

# Exercise 2.3

print(sum([i * i for i in range(1, 2028)]))

# Exercise 2.4

# (a)

imie = 'Łukasz'
print([ord(letter) for letter in imie])

# (b)

# List of the first ten elements: (No, Name, Symbol, Weight)
pt = [
    (1, "Hydrogen", "H", 1),
    (2, "Helium", "He", 4),
    (3, "Lithium", "Li", 7),
    (4, "Beryllium", "Be", 9),
    (5, "Boron", "B", 11),
    (6, "Carbon", "C", 12),
    (7, "Nitrogen", "N", 14),
    (8, "Oxygen", "O", 16),
    (9, "Fluorine", "F", 19),
    (10, "Neon", "Ne", 20)
]

# Define the decorative borders
header_border = "+---+--------------------+------+----------+"
header_text   = "|No.|Name (en)           |Symbol|Weight (u)|"

print(header_border)
print(header_text)
print(header_border)

for (n, name, symbol, weight) in pt:
    # >3: right 3, <20: left 20, ^6: center 6, >10: right 10
    print(f"|{n:>3}|{name:<20}|{symbol:^6}|{weight:>10}|")

print(header_border)

# Exercise 2.5

S = """ssdfdsvfv dfv dscsdfsd fsd cdsvsvxvfx
vdfvfvcv vxvfxbxfbxfbd dfednrnreyny bsbsrbsbr
svtrbryy dbsgbs gbe bdfbe b t vd fb stdb vdfsbt"""

black_chars_count = sum(1 for char in S if not char.isspace())

words = S.split()
word_count = len(words)
longest_word = max(words, key=len)
lex_sorted = sorted(words)
length_sorted = sorted(words, key=len)

# Exercise 2.6

t = (2, 4)
# print([t[2]]) <- t[0] = 2, t[1] = 4, t[2] - out of range
# t.append(6) <- tuples are immutable
a,b = t # class unpacking without creating temporary variables
print(a, b)

# Exercise 2.7

# Version 1

roman_to_arabic = {
    "I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, 
    "XL": 40, "L": 50, "XC": 90, "C": 100, 
    "CD": 400, "D": 500, "CM": 900, "M": 1000
}

print(roman_to_arabic)

# Version 2

roman_to_arabic = dict(M = 1000, D = 500, C = 100, L = 50, X = 10, V = 5, I = 1)
print(roman_to_arabic)

