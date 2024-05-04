#циклы
l1 = [1, 2, 3, 'hello']
#one_element по сути переменная в которую читаем элементы из коллекции
for one_element in l1:
    print(one_element)
    #или для каждого элемента будет выполнять 2 действия
    print(one_element * 2)

d1 = {
    'one': 123,
    'two': 456
}

for key_elemnet in d1.keys():
    print(key_elemnet)

a = 1
d2 = dict()

for element in l1:
    d2[a] = element
    a = a + 1

print((d2))

i = 0
while True:
    print(i)
    i += 1
    if i == 5:
        break