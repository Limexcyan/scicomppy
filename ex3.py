import math

# Exercise 3.1

word = "Conda"
no_letters = len(word) 

upper = "+" + (no_letters * "---+")

mid_0 = "".join([f"| {letter} " for letter in word])
mid = mid_0 + "|"

print(upper)
print(mid)
print(upper)

# Exercise 3.2

for i in range(1, 41):
    if i == 13:
        continue
    if (i %  5 == 0) and (i % 7 != 0): 
        print(f'{i} is divided by 5')
    elif (i % 7 == 0) and (i % 5 != 0):
        print(f'{i} is divided by 7')
    elif (i % 5 == 0) and (i % 7 == 0):
        print(f'{i} is divided by 5 and 7')
    else:
        print(f'{i} is not important')


x = 1

while x <= 40:
    if x == 13:
        x += 1
        continue
    
    if x % 5 == 0 and x % 7 == 0:
        print(f"{x} is divided by 5 and 7")
    elif x % 5 == 0:
        print(f"{x} is divided by 5")
    elif x % 7 == 0:
        print(f"{x} is divided by 7")
    else:
        print(f"{x} is not important")
    
    x += 1

# Exercise 3.3

n = 2022
x = round(math.pi, 5)
word = "Python"
polish = "książka"

with open("vars.txt", "w", encoding="utf-8") as file:
    file.write(str(n))
    file.write("\n")
    file.write(str(x))
    file.write("\n")
    file.write(word)
    file.write("\n")
    file.write(polish)

with open("vars.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
