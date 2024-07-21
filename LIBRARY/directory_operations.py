import os

print(os.getcwd()) # возвращает то, где я запускаю этот файл

print(os.path.exists('classwork.py')) # проверяет существует ли файл

if not os.path.exists('spam'): # проверяет, существует ли директория
    os.mkdir('spam') # создает директорию(папку)


print(os.listdir()) # возвращает списком то, что находится в данной директории

os.chdir(os.getcwd() + '\\' + 'spam') # сменить директорию
print(os.listdir())

if os.path.exists('1.txt'):
    os.rename('1.txt', '2.txt') # переименовывает файл
print(os.listdir())

os.remove('2.txt') # удаляет файл
print(os.listdir())

os.chdir(os.path.dirname(os.path.abspath('spam'))) # возвращает к исполняемому файлу