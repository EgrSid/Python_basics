import string
import random


def password(length, numbers=True, letters=True, symbols=True):
    answer1 = ''
    if numbers:
        answer1 += string.digits
    if letters:
        answer1 += string.ascii_letters
    if symbols:
        answer1 += string.punctuation
    answer = ''.join(random.choice(answer1) for i in range(length))
    return answer


print(password(10))