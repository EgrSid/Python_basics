        #то же, что и конструкция elif('case _:' = 'else:')
def get_number_explanation(number):
    match number:
        case 666: #if number == 666
            return 'devil number'
        case 42: #elif number == 42
            return 'answer for everything'
        case 7: #elif number == 7
            return 'prime number'
        case _: #else:
            return 'just a number'