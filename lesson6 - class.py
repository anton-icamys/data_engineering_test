#класс можно определять как через инит, так и сразу в определении
class Test:
    test: int

    def __init__(self):
        self.test = 2


class Test2:
    test = 2


class Human:
    hands = 2
    foots = 2
    head = 1
    eyes = 2
    age = 30
    sex = 1
    name = str

    def __init__(self, v_name):
        self.name = v_name

    #функция которая работает тольок внутри это класса
    def mob(self):
        if self.sex == 1:
            self.hands = self.hands / 2

    def see_info(self):
        print(f'name = {str(self.name)}')
        print(f'hands = {str(self.hands)}')
        print(f'foots = {str(self.foots)}')
        print(f'head = {str(self.head)}')
        print(f'eyes = {str(self.eyes)}')
        print(f'age = {str(self.age)}')
        print(f'sex = {str(self.sex)}')

    def __str__(self):
        return self.name
#создадим переменную в которой будет лежать экземпляр этого класса

o_petya = Human('Petya')
#o_petya.see_info()

o_vasya = Human('Vasya')
o_vasya.see_info()
o_vasya.mob()

o_vasya.see_info()
o_vasya.hands = 3
o_vasya.see_info()

#если вызвать посто принт, то ничего не будет. Но если в классе оисать def __str__(self): то вернет ответ
print(o_vasya)

class Woman(Human):#наслдеуем от класса Хуман
    def __init__(self, v_name=''):
        super().__init__(v_name)#наследуем все параметры из родительского или переопределяем
        self.sex = 0
        self.circle = 30#динамически объявили переменную

    def see_info(self):
        super().see_info()
        print(f'circle = {str(self.circle)}')


o_masha = Woman("masha")
print('mmm')
o_masha.see_info()

# чем объект отличается от классов?
# объект это конрктеный экземпляр какого то класса

a[j], a[j + 1] = a[j + 1], a[j]