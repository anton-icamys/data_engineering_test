
class Human:
    name: str
    __age: int #private
    _password: str

    def __init__(self, v_name = 'Vasya'):
        self.name = v_name
        self.__age = 30
        self._password = '1234'

    def get_age(self):
        return self.__age

    def set_age(self, v_age):
        if type(v_age) == int: # == equal is
            self.__age = v_age


o_vasya = Human('Vasya')
print(o_vasya.name)
#print((o_vasya.__age))
print(o_vasya._password)

print(o_vasya.get_age())

o_vasya.set_age(25)

print(o_vasya.get_age())

#public
#protected _
#private __