import os
os.chdir(os.getcwd() + '\\' + 'spam')
file = open('Snow Queen.txt', 'r', encoding='utf-8') # 2 аргумент - режим открытия

# t = text file, b = binary file

'''2 аргументы:
        'r' - только чтение, курсор сотит в начале файла
        'rb' - только чтение бинарного файла
        'r+' - чтение и запись, курсор стоит в начале файла
        'rb+' - чтение и запись бинарного, курсор в начале файла
        'w' - только для записи.пересоздает файл.добавляет в начало файла
        'wb' - только для записи бинарного файла
        'файл от АДВ' '''

print(file.name)
print(file.mode) # то, как мы файл открыли

# print(file.readline())  считывает строчку

# print(file.readlines()) # вернет список из строчек

print(file.tell()) # показывает положение курсора
file.seek(0) # выставляем положение курсора(0 символов перед ним)


for line in file.readlines(30): # считывает 30 строчек
    print(line)

d = file.read(5) # 5 - количество элементов, которое надо считать

file.close()



import os
          #ПОСЧЕТ КОЛИЧЕСТВА "О" В ФАЙЛЕ
os.chdir(os.getcwd() + '\\' + 'spam')

with open('Snow Queen.txt', 'r', encoding='utf-8') as file:
     a = file.readlines()
     b = 0
     for i in a:
          b += i.lower().count('о')
     print(b)



os.chdir(os.getcwd() + '\\' + 'spam')


os.chdir('spam')
        #ПОИСК СЛОВ В ТЕКСТЕ
from colorama import Fore
with open('Snow Queen.txt', 'r', encoding='utf-8') as file:
    a = file.readlines()
word = input('Введите слово, которое необходимо найти: ').lower().strip()
for i in a:
    try:
        b = i.lower().index(word)
        print(i)
        break
    except:
        continue
else:
    print(Fore.RED + 'Такого слова в тексте нет! \nПопробуйте снова!')

    import os

    # ФОРМАТИРОВАНИЕ ФАЙЛА
def formatting_file(person_file):
    if not os.path.exists('spam'):
        os.mkdir('spam')
    os.chdir('spam')
    file_name = person_file[:person_file.index('.')]
    with open(person_file, 'r', encoding='utf-8') as file:
        if os.path.exists(file_name + '(formatted).txt'):
            os.remove(file_name + '(formatted).txt')
        with open(file_name + '(formatted).txt', 'a', encoding='utf-8') as f:
            for line in file.readlines():
                if line == '\n' or line == '\xa0':
                    continue
                else:
                    f.write('   ' + line)
    os.chdir(os.getcwd()[:os.getcwd().rindex('\\')])
formatting_file('Snow Queen.txt')
formatting_file('1.txt')


        # ЗАПИСЫВАЕТ ИНФОРМАЦИЮ В .TXT ФАЙЛ
def export2file(message, file_name = 'export2file'):
    if not os.path.exists('exports'):
        os.mkdir('exports')
    os.chdir('exports')
    with open(file_name + '.txt', 'a', encoding='utf-8') as file:
        file.write(message)
    os.chdir(os.getcwd()[:os.getcwd().rindex('\\')])
export2file('привет', 'Egor')
export2file('пока', 'Egor')