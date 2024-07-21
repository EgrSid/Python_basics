tpl = ('YoKaLeMeNe', 'YoPeReSeTe', 7)  # картеж - неизменяемая структура
print(tpl[1])
print(tpl[2] * 4)


lst1 = []# пустой список; его можно изменять
lst1 = list()# переводим НИЧЕГО в список

lst1.append(True)# добавляет элемент (True - в данном случае) в конец списка

lst1.extend([45, False, -0.4])# расширить список другим списком (добавляет в конце)
[45, False, -0.4].extend(lst1)# расширяет список другим списком (добавляет в начале)

lst1.insert(2, 'Giga')# вставляет значение в список на нужное место; 2 - место, куда надо вставить

lst1.remove(45)# удаление элемента в списке с данным значением

lst1.pop()# удаление последнего элемента + возвращает удаленный элемент
lst1.pop(1)# удаление элемента с индексом 1 + возвращает удаленный элемент

lst1.clear()# удаление всех элементов в списке с сохранением списка

lst2 = [12, True, 'asdf', -0.999, [1, 2, 3], tpl, True]
print(lst2[5])# выводит 5 элемент
print(lst2[5][1])# выводит 1 элемент у 5 элемента списка

lst2.count(True)# считает количество элементов в списке

lst3 = []
lst3 = lst2.copy()# скопировал список lst2 в список lst3



lst4 = [756, -5, 23, 9, 0]
lst4.sort()# сортирует список от меньшего к большему
lst4.sort(reverse = True)# сортирует список от большего к меньшему

del lst4# удалит полностью из памяти компьютера нужные данные


        # ШИФР ЦЕЗАРЯ "РАСШИФРОВКА"
def encrypt(password, key):
    password_new = ''
    lst1 = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    for i in password:
        if i.isalpha():
            if i.isupper():
                i = i.lower()
                is_kaps = True
            y = lst1[lst1.index(i) + key - 33]
            if is_kaps:
                password_new += y.upper()
                is_kaps = False
            else:
                password_new += y
        else:
            password_new += i
    print(password_new)
encrypt('Привет, я 1 в России!!!', 3)




        # ШИФР ЦЕЗАРЯ "ВЗЛОМ"
def encrypt(password, key = range(32)):
    lst1 = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    if key is int:
        key = [key]
    else:
        key = range(32)
    for k in key:
        password_new = ''
        for j in password:
            if j.isalpha():
                if j.isupper():
                    j = j.lower()
                    is_kaps = True
                y = lst1[lst1.index(j) - k]
                if is_kaps:
                    password_new += y.upper()
                    is_kaps = False
                else:
                    password_new += y
            else:
                password_new += j
        print(password_new)
encrypt('Тулезх, плу, в 1 е Усффллл!!!')