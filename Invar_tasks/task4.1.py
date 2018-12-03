#Инвариантная СР
#4.1. Создание программы по заполнению массивов случайными значениями. 
#Сортировка значений в списке методом вставки, плавной сортировки, с помощью встроенных функций языка.

#NumPy — это библиотека языка Python, добавляющая поддержку больших 
#многомерных массивов и матриц, вместе с большой библиотекой 
#высокоуровневых (и очень быстрых) математических функций 
#для операций с этими массивами.

#Для создания массивов со случайными элементами служит модуль numpy.random

"""Создаем массив со случайными эелементами"""
import numpy as np
import numpy.random 

"""создание массива со случайными целыми и дробными числами"""
float_array = np.random.sample(10)
array = np.random.randint(0, 12, 10)
a = np.arange(10)

"""Реализация различных сортировок:
      1) сортировка по возрастанию/убыванию;
      2) случайная выборка из массива, с помощью функции choice;
      3) функция permutation позволяет перемешать и возвратить полученный массив.
"""
sort_array = sorted(array)
reverse_array = sorted(array, reverse = True)

two_array = np.random.choice(a, 20, replace = True)
new_array = np.random.permutation(array)

#print(float_array)
#print(array)
#print(new_array)
#print(two_array)
#print(sort_array)
#print(reverse_array)

"""Сортировка простыми вставками"""
def just_sort(lst = np.random.randint(0, 12, 10)):
    for i in range(len(lst) - 1):
        j = i - 1 
        key = lst[i]
        while lst[j] > key and j >= 0:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

just_sort()

"""Быстрая сортировка"""
import random
def quick_sort(nums):
   if len(nums) <= 1:
       return nums
   else:
       elem = random.choice(nums)
   one_nums = [n for n in nums if n < elem]
 
   two_nums = [elem] * nums.count(elem)
   three_nums = [n for n in nums if n > elem]
   return quicksort(one_nums) + two_nums + quick_sort(three_nums)

quick_sort([5,8,1,0,4,9])
