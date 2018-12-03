#4.2. Создание программы по распределению списка с случайными значениями на два списка 
#по определенному критерию четность/нечетность.

import random
array = []

for i in range(50):
    array.append(int(random.random() * 100))
    
array.sort()

even_num = list(filter(lambda x: not x%2, array))
odd_num = list(filter(lambda x: x%2, array))

print(even_num)
print(odd_num)
