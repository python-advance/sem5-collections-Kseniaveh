#Инвариантная СР
#4.2. Создание программы по распределению списка с случайными значениями на два списка 
#по определенному критерию положительные/отрицательные.

import random
array = []

for i in range(10):
    array.append(int(random.random() * 10) - 5)

negative_num = []
positive_num = []

for i in array:
    if i < 0:
        negative_num.append(i)
    elif i > 0:
        positive_num.append(i)
        
print(array)
print(negative_num)
print(positive_num)

