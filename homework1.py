numbers = int((input(('ВВедите трехзначное число: '))))
# print(sum(list(map(int, numbers))))

if numbers < 10000 and numbers > 99:
    a=int(numbers/100)
    b=int(numbers/10 - a*10)
    c= numbers%10
    print(c)
    print(f'Сумма цифр числа {numbers} равна: {a+b+c}')
else:
    print('Не верное число')