# 3. Создать классы: человек, рота, полк. В роте могут содержаться несколько человек, в полку - несколько рот.
# Написать методы:
# - добавления человека в роту, добавления роты в полк.
# - удаления человека из роты или из полка (в этом случае, человек удалиться из роты). Метод на вход должен получать list с несколькими переменными типа Human - как я с автобусом делал.
# - выводить информацию об одном человеке: имя, возраст.
# - выводить информацию об всех людях в роте.
# - выводить информацию об всех людях в полку.

# list1 = list()
# list1 = [1, 0, 2]
#
# for element in list1:
#     result: int
#     try:
#         result = 1 / element
#     except Exception as e:
#         print(e)
#     except ZeroDivisionError:
#         print('Именно на это исключение будет такая ошибка, если ее не прокинули раньше')
#     finally:
#         print('Это действие выполняется всегда после Эксепшена', result)


class Human:
    name: str
    age: int
    size: str
    rang: str

    def __init__(self, name: str, age: int, size: str, rang: str):
        self.name = str.upper(name)
        self.age = int(age)
        self.size = str.upper(size)
        self.rang = str.upper(rang)

    def get_info(self):
        result = 'Сведения о солдате: '
        for element in [self.name, self.age, self.size, self.rang]:
            result = result + str(element) + ', '
        return result[:-2]

    def set_parameter(self, param: str, value):
        setattr(self, param, value)

    def get_parameters(self):
        print(vars(self))


o_petya = Human('petya', 30, 'm', 'sergant')
print(o_petya.get_info())
o_petya.get_parameters()
o_petya.set_parameter('age', 39)
print(o_petya.get_info())

o_vasya = Human('vasya', 18, 's', 'sergant')
o_sasha = Human('sasha', 21, 'L', 'sergant')


class Rota:
    sostav: list()
    name: str

    def __init__(self, name: str, sostav: list()):
        self.sostav = sostav
        self.name = name

    def see_info(self):
        print(f'Название {self.name}')
        sostav1 = 'Состав: '
        for ele in self.sostav:
            sostav1 = sostav1 + str(ele.name) + ', '
        print(sostav1[:-2])

    def add_member(self, list_members: list):
        for member in list_members:
            self.sostav.append(member)

    def delete_member(self, list_members: list):
        for member in list_members:
            if member in self.sostav:
                self.sostav.remove(member)


rota1 = Rota('1', [o_sasha, o_vasya])

rota1.see_info()

rota1.add_member([o_petya])

rota1.see_info()

rota1.delete_member([o_sasha, o_vasya])

rota1.see_info()


class Polk(Rota):

    def __init__(self):
        super().__init__()

    def see_info(self):
        super().see_info()