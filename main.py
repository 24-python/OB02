class Bird():
    def __init__(self, name, voice, color):
        self.name = name
        self.voice = voice
        self.color = color
        self.name = name

    def fly(self):
        print(f'{self.name} летает')

    def eat (self):
        print(f'{self.name} ест')
    def sing(self):
        print(f'{self.name} поет чирик чирик')

    def info(self):
        print(f'{self.name} имя')
        print(f'{self.voice} голос')
        print(f'{self.color} цвет')



class Pigeon(Bird):
    def __init__(self, name, voice, color, favorite_food):
        super().__init__(name, voice, color)
        self.favorite_food = favorite_food

    def walk(self):
        print(f'{self.name} бродит')

    def sing(self):
        print(f'{self.name} поет курлык курлык')



bird1 = Pigeon("Гоша", "Кря-кря", "Красный", "Курица" )

bird2 = Bird("Вася", "курлык", "Серый")


bird1.sing()
bird1.info()
bird1.walk()