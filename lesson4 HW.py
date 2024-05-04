# for el in [1, 2, 3]:
#     print(el)
#
# l1 = ['ythgj', 'hello!', 'hello', 'yagoda malinka']
# for el in l1:
#     if len(el) > 5:
#         print(el)
#
# l2 = [1, 2, 3]
#
# l3 = [l1]
# print(l3)
# l3.append(l2)
# print(l3)
#
# for el in l3:
#     for el1 in el:
#         print(el1)

d1 = {
    'val1': 1,
    'val2': 2,
    'val3': 3
}
print(d1)

d2 = dict()
d2[1] = 'a'
d2[2] = 'b'
d2[3] = 'c'

print(d2)
# for el in d1:
#     print(el)
# for el in d1.values():
#     print(el)

# i = 1
# while True:
#     print(i)
#     i += 1
#     if i > 10:
#         break

d4 = dict()
a = 0

# while True:
#     d4[a] = d1.values()

print(d4)

dict1 = {'a': 1, 'z': 2, 'c': 3}
dict2 = {'x': 10, 'y': 20, 'z': 30}

merged_dict = {}

# for key in dict2:
#     if key in dict1:
#         merged_dict[key] = dict1[key]
#     merged_dict[key] = dict2[key]
dict3 = {
    1: dict1,
    2: dict2
}

i = 0
while i < len(dict3):
    for el in dict1.values():
        merged_dict[i] = el
        i += 1
    for el in dict2.values():
        merged_dict[i] = el
        i += 1


print("Словарь 1:", dict1)
print("Словарь 2:", dict2)
print("Объединенный словарь:", merged_dict)