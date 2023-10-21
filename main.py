# задание 1
with open('input.txt', 'r') as file:
    n = list(map(int, file.read().split()))

s = 1
for i in n:
    s *= i

with open('output.txt', 'w') as file:
    file.write(str(s))

# задание 2
with open('input1.txt', 'r') as file:
    n = list(map(int, file.read().split()))

def insertionSort(n):
    a = len(n)
    for i in range(1, a):
        for j in range(i, 0, -1):
            if n[j] < n[j - 1]:
                n[j], n[j - 1] = n[j - 1], n[j]
            else:
                break

insertionSort(n)
with open('output1.txt', 'w') as file:
    for i in range(len(n)):
        file.write(str(n[i]) + '\n')

# задание 3
lastNameYoungest = ""
firstNameYoungest = ""
minAge = float("inf")

lastNameOldest = ""
firstNameOldest = ""
maxAge = float("-inf")

with open("children.txt", "r") as file:
    for line in file:
        lastName, firstName, age = line.strip().split()
        age = int(age)

        if age < minAge:
            minAge = age
            lastNameYoungest = lastName
            firstNameYoungest = firstName

        if age > maxAge:
            maxAge = age
            lastNameOldest = lastName
            firstNameOldest = firstName

with open("youngest.txt", "w") as file:
    file.write(f"Младший ребенок: {lastNameYoungest} {firstNameYoungest} {minAge}")

with open("oldest.txt", "w") as file:
    file.write(f"Старший ребенок: {lastNameOldest} {firstNameOldest} {maxAge}")

