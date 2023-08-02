import sys

def div(num1, num2):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        print('Hiba! Osztás nullával!')
        sys.exit(1)

num1 = int(input('Szám1: '))
num2 = int(input('szám2: '))
print(f'Eredmény: {div(num1, num2)}')
