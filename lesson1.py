

v_int = 2
v_float = 1.1
#v_string = 'string'
#print(v_int)
#print(v_float)
#print(v_string)
#v_int2 = v_int * 15
#rint(v_int2)
#v_int = '3'
#print(v_int)

v_result = v_int * v_float
#тут неявное преобразование. чтобы оно было явным нужно использовать спец функцию
v_int_fl = float(v_int)
print((v_int_fl))
print(v_result)

#лист это как самый простой ray. Те как коллекция и все с ним связанное
#он может быть объявлен двумя способами.
v_list = list()
v_list2 = [1,2,3,4,5]
print(v_list)
print(v_list2)
#v_list3 = [1.,2.,'3','4',5]
#print(v_list3)
#v_list4 = [1,2,list[3,4]]
#print(v_list4)
#v_list2 = v_list2+v_list3
#print(v_list2)

#добавление нового элемента
v_list2.append('test')
print(v_list2)
#но так будет ошибка
#v_list2 = v_list2 + 'tset'
#print(v_list2)

a = 7
b = 2

# Сложение
print('Sum: ', a + b)
# Вычитание
print('Subtraction: ', a - b)
# Умножение
print('Multiplication: ', a * b)
# Деление
print('Division: ', a / b)
# Целочисленное деление
print('Floor Division: ', a // b)
# Остаток от деления
print('Modulo: ', a % b)
# a в степени b
print('Power: ', a ** b)

# Оператор Равно
print('a == b =', a == b)
# Оператор Не Равно
print('a != b =', a != b)
# Оператор Больше чем
print('a > b =', a > b)
# Оператор Меньше чем
print('a < b =', a < b)
# Оператор Больше или Равно
print('a >= b =', a >= b)
# Оператор Меньше или Равно
print('a <= b =', a <= b)

x1 = 4
y1 = 4
x2 = 'Hello'
y2 = 'Hello'
x3 = [1, 2, 3]
y3 = [1, 2, 3]
print(x1 is not y1)  # выведет False
print(x2 is y2)  # выведет True
print(x3 is y3)  # выведет False потому что списки как бы равны, но не идентичны

x = 'Hello world'
y = {1: 'a', 2: 'b'} #Точно так же 1 — это ключ, а 'a' — это значение в словаре y. Следовательно, 'a' in y возвращает False.
# Проверяем, находится ли 'H' в строке x
print('H' in x)  # выведет True
# Проверяем, находится ли 'hello' в строке x
print('hello' not in x)  # выведет True
# Проверяем, находится ли ключ '1' в словаре y
print(1 in y)  # выведет True
# Проверяем, находится ли ключ 'a' в словаре y
print('a' in y)  # выведет False


print('new changes')


print(2*8)