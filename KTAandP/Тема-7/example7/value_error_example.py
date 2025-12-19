
try:
    ans = int(input('Введіть номер: '))
except ValueError as error:
    print('Введено не коректне значення')
else:
    print(f"{ans = }")


