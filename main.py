import random


def average(number):
    ave_num = sum(number)/len(number)
    total = 0.0
    for numer in number:
            total += numer
    return ave_num

randomlist=[]

for i in range(0,5):
    n = random.randint(1,1500)
    randomlist.append(n)


print(average([1230, 500 ,280, 1615]))
print(average(randomlist))

