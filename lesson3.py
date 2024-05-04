#True False
if True:
    print(1)

#В оператор а записываем результат сравнения 1 и 2
a = 1==2
print(a)

#но в любом случае выводится первая истина
a = 5
if (a > 2) and type(a)==int:
    print('a>2')
    print('ghte')
elif a == 2:
    print('a = 2')
else:
    print('a<2')
print(type(a))