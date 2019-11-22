# 6. Функция сортировки выбором select:
# 3. Функция шейкерной (коктейльной) сортировки shaker - модификации пузырьковой:

from random import randint

def selectsort(a):
    # сортировка Select
    for i in range(len(a)-1):
        m=i
        j = i + 1
        while j < len(a):
                    if a[j] < a[m]:
                        m = j
                    j = j + 1
        a[i], a[m] = a[m], a[i]
def shakersort(a):
    # сортировка Shaker
    def swap(i, j):
        a[i], a[j] = a[j], a[i]
    upper = len(a) - 1
    lower = 0
    no_swap = False
    while not no_swap and upper - lower > 1:
        no_swap = True
        for j in range(lower, upper):
            if a[j + 1] < a[j]:
                swap(j + 1, j)
                no_swap = False
        upper = upper - 1
        for j in range(upper, lower, -1):
            if a[j - 1] > a[j]:
                swap(j - 1, j)
                no_swap = False
        lower = lower + 1

a = []
for i in range(5):
    a.append(randint(1, 99))
print(a)
b = a.copy()
selectsort(b)
print(b)
shakersort(a)
print(a)