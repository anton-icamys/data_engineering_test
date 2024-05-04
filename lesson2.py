list1 = [1, 2, 'privet']
print(list1)
print(list1[2])
#словарь в котором можно обратить к элементу по названию
#по сути одномерный массив, но по названию
#так словарь объявляется
d1 = dict()
print(d1)
d2 = {
    "val1": 1, "val2": 2, 1: 123
}
print(d2)
#выводит только ключи
print(d2.keys())
#выводит только значения
print(d2.values())
d1["first"] = 1
print(d1)
d1["secd"] = 123456
d1["first"] = 22

print(d1)
#достаем конкретное значение из словаря(потому что у него есть имя)
print(d1.get("secd"))
print(d1["secd"])
print(list1[2])
#print(list1.get(2)) - так будет ошибка

#set - очень похож на лист, но содержит только уникальные значения
list2 = [1, 1, 2, 2, 3, 4]
print(list2)
list2 = list(set(list2))
print(list2)

#В словарь можно запихнуть другой словарь и достать как все значения, так и конкретное

d3 = dict()
d3["new"] = d2
d3["old"] = None
#тк в словаре Д2 нет ключа new - выводится None
print(d3.get("new").get("new"))
print(d3.get("new").get("val2"))

list3 = list(d3.keys())
print(list3)
print(type(list3))
print(type(d3))