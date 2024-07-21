import colorama
colorama.init(autoreset=True)

counter_months = 0

print('Привет\nЯ - помощник при рассчете выгоды кредита или ипотеки!')



while True:
    S = input('Введите сумму кредита или ипотеки: ')
    try:
        S = float(S)
        if S < 0:
            print(colorama.Fore.RED + 'Введено некорректное значение! Повторите попытку!')
            continue
        break
    except:
        print(colorama.Fore.RED + 'Введено некорректное значение! Повторите попытку!')
k = S



while True:
    q = input('Введите процентную ставку в месяц: ')
    try:
        q = float(q)
        if q < 0:
            print(colorama.Fore.RED + 'Введено некорректное значение! Повторите попытку!')
            continue
        break
    except:
        print(colorama.Fore.RED + 'Введено некорректное значение! Повторите попытку!')



while True:
    d = input('Введите ежемесечную сумму выплат: ')
    try:
        d = float(d)
        if d < 0:
            print(colorama.Fore.RED + 'Введено некорректное значение! Повторите попытку!')
            continue
        else:
            d = float(d)
            if S * q / 100 < d:
                while S > d:
                    S = S + S * q / 100 - d
                    counter_months += 1
                    print('После ', counter_months, ' месяца вам осталось заплатить ', S, 'рублей')
                break
            else:
                print(colorama.Fore.RED + 'Введено некорректное значение! Повторите попытку!')
    except:
        print(colorama.Fore.RED + 'Введено некорректное значение! Повторите попытку!')





print('Заплатив за ', counter_months + 1, ' месяцев, вы полностью погасите свою задолжность!')
print('Вы будете выплачивать кредит в течение ', counter_months + 1, ' месяцев')
overpayment = counter_months * d + S - k
print('Переплата по кредиту составит ', overpayment, 'рублей')
