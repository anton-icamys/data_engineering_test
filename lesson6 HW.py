class Citizen:    planet: str
    hand: int    leg: int
    age: int    sex: int
    nation: str
    def __init__(self):        self.planet = 'Earth'
        self.hand = 2        self.leg = 2
        self.age = 20        self.sex = 1
        self.nation = 'rus'
    def see_info(self):
        print(f'planet = {str(self.planet)}')        print(f'hand = {self.hand}')
        print(f'leg = {self.leg}')        print(f'age = {self.age}')
        print(f'sex = {self.sex}')        print(f'nation = {self.nation}')
    def change_parametr(self, key: str, new_parametr: any):
        new_key = key        setattr(Citizen, key, new_parametr)

anton = Citizen()
anton.see_info()anton.change_parametr('age', 21)
anton.see_info()anton.age = 22
anton.see_info()
class Child(Citizen):    parent1: str
    parent2: str
    def __init__(self):
        super().__init__()        self.parent1 = 'father'
        self.parent2 = 'mother'
    def see_info(self):
        super().see_info()        print(f'parent1 = {str(self.parent1)}')
        print(f'parent2 = {str(self.parent2)}')
petya = Child()
petya.see_info()