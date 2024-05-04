#функции. обялвяется через def. может как иметь параметры, так и не иметь.


def func1():
    print('a')
    print('b')


func1()


# for one in [1, 2, 3]:
#     func1()


def func2(local_element):
    print(local_element, local_element * 2)


for element in [1, 2, 3]:
    func2(element)
for element in [1, 2, 3]:
    func2(local_element=element)


#функция должна что-то возвращать.
#В начале строки f нужно, чтобы подцеплять переменные!!!


def func3(firstname, lastname='Сидоров'):
    print(f'FirstName = {str(firstname)}, LastName = {str(lastname)}')


func3('Петя', 'Петров')
func3('Петя')


def sum2(a, b):
    result = a + b
    return result


print((sum2(3, 5)))

c = sum2(3, 8)
print(c)


def any_function(a, b):
    resul1 = a + b
    result2 = a - b
    return resul1, result2


print(any_function(1, 1))

var1, var2 = any_function(10, 8)
print(var1, var2)

var3 = any_function(1, 5)
print(var3)

l1 = [1, 2]
print(l1)


def func4(a: int):
    return a * 2


print(func4(5))
print(func4('privet'))


def loop1():
    for element1 in [1, 2, 3, 4, 5, 6, 7, 8]:
        print(element1)
        if element1 > 3:
            return None


loop1()