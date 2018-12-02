#Вариативная СР
#4.2. Создание программы по разделению одного словаря на произвольное количество словарей 
#по определенному критерию, задаваемому в виде лямбда функции.

#СДЕЛАТЬ ЛЯМБДА ФУНКЦИЮ!

def main():
    dic = {
    'Name':'ksenia',
    'Age': 20,
    'Surname':'Vehova'}

    dict_num = {}
    dict_str = {}

    for k, v in dic.items():
        if type(v) is int:
            dict_num[k] = v
        if type(v) is str:
            dict_str[k] = v
    print(dict_num)
    print(dict_str)
    
        
if __name__ == '__main__':
    main()
