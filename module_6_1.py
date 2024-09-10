class Animal:
    def __init__(self, alive=True, fed=False, name=None):
        self.alive = alive
        self.fed = fed
        self.name = name


class Plant:
    def __init__(self, edible=False, name=None):
        self.edible = edible
        self.name = name


class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name=name)

    def eat(self, food):
        self.fed = False if self.fed else True
        self.fed = True if food.edible else False
        self.alive = True if self.fed else False
        print(f'{self.name} съел {food.name}')


class Predator(Animal):
    def __init__(self, name):
        super().__init__(name=name)

    def eat(self, food):
        self.fed = True if self.fed else False
        self.fed = False if food.edible else True
        self.alive = True if self.fed else False
        print(f'{self.name} не стал есть {food.name}')


class Flower(Plant):
    def __init__(self, name):
        super().__init__(edible=True, name=name)


class Fruit(Plant):
    def __init__(self, name):
        super().__init__(edible=True, name=name)


if __name__ == '__main__':
    a1 = Predator('Волк с Уолл-Стрит')
    a2 = Mammal('Хатико')
    p1 = Flower('Цветик семицветик')
    p2 = Fruit('Заводной апельсин')

    print(a1.name)
    print(p1.name)

    print(a1.alive)
    print(a2.fed)
    a1.eat(p1)
    a2.eat(p2)
    print(a1.alive)
    print(a2.fed)

    # Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.
