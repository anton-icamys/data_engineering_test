import random


def func0():
    result = random.random()
    return result
#
#
# print(func0())
#
#
# def func1(a):
#     print(a)
#
#
# func1(5)
# func1('privet')
#
#
# def func2(a: int, b: int, c: int):
#     result = (a + b) * c
#     return result
#
#
# def funct3(a: int, b: int, c: int = 1):
#     result = (a + b) * c
#     return result


# for element in [1, 2, 5]:
#     if element <= 4:
#         func1(element)
#     elif element > 4:
#         func1(int(func0() * 100))

l1 = [int(func0() * 100), int(func0() * 100), int(func0() * 100), int(func0() * 100), int(func0() * 100)]
print(l1)


def func4(lilt1: list):
    result = 0
    for new_element in lilt1:
        result += new_element
    return result


# print(func4(l1))
# print('bubble function')


def bubble(list1: list):
    i = 0
    l = len(list1) - 1
    for element1 in list1:
        print(element1)

def bubble_sort(list1: list):
    i = 0
    q = len(list1) - 1
    ex = 0
    while True:
        #ex = 0
        if list1[i] > list1[i + 1]:
            stage = list1[i+1]
            list1[i + 1] = list1[i]
            list1[i] = stage
            ex = 1
        i += 1
        #print(list1, i, ex)
        if i == q and ex == 1:
            i = 0
            ex = 0
        if i == q and ex == 0:
            return list1

print(bubble_sort(l1))




