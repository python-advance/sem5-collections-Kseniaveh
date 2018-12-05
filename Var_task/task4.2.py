#Вариативная СР
#4.2. Создание программы по разделению одного словаря на произвольное количество словарей 
#по определенному критерию, задаваемому в виде лямбда функции.

#при запуске программмы, в main_func мы дергаем break_dict, 
#передавая ему два аргумента: словарь и лямбда-функцию с условием, 
#далее мы бежим в break_dict по данному словарю и идет проверка на условие 
#больше 15 очков (через лямбда-функцию), если True, то добавляем в 1 словарь, 
#если False, то добавляем во 2 словарь. 
#В итоге, функция break_dict отдает мне два словаря, складывая их в переменные one и two.

def break_dict(dictionary: dict, func_lambda): #функция с входными аргументами: словарь и лямбда-функция
    one_dict = {}
    two_dict = {}

    for el in dictionary.items(): # бежит по словарю и проверяет условие в лябда-функции, то есть тут вызывается лямбда
        print('Условие лямбда-функции, больше 15 - ',func_lambda(el)) 
        if func_lambda(el):
            one_dict.update({el[0]: el[1]})
            print(str(el) + " добавление в 1")
        else:
            two_dict.update({el[0]: el[1]})
            print(str(el) + " добавление во 2")

    return one_dict, two_dict


def main_func():
    dic = {
        "Student1": {"name": "Ksenia", "score": 10},
        "Student2": {"name": "Ksusha", "score": 20},
    }

    one, two = break_dict(dic, lambda el: el[1]['score'] > 15) 

    print("Словарь 1:")
    print(one)
    print("Словарь 2:")
    print(two)


if __name__ == '__main__':
    main_func()
