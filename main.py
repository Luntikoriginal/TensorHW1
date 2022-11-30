import random

listNum = [random.randint(1, 10) for i in range(10)]
print(listNum)
listNum.sort()
print("Sorted massive:")
print(listNum)
average = sum(listNum) / len(listNum)
print("Average:")
print(average)
