#Вариативная СР
#4.1. Создание программы с реализацией вручную одного из алгоритмов сортировки (вставки, плавной сортировки).

import numpy as np
import numpy.random 
"""Сортировка простыми вставками"""
def just_sort(lst = np.random.randint(0, 12, 10)): # в качестве аргумента - рандмный список, от 0 до 12, количество элементов 10
    for i in range(len(lst) - 1):
        j = i - 1 
        key = lst[i]
        while lst[j] > key and j >= 0:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

just_sort()
