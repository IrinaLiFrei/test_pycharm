# Доработаем задания 5-6.
# Создайте класс-фабрику.
# - Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# - Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
from task_1_parent import Animal, Dog, Fish, Bird


class Factory(Dog, Fish, Bird):
    def __init__(self, class_name, *args, **kwargs):
        self.class_name = class_name
        Dog.__init__(self, *args, **kwargs)
        Fish.__init__(self, *args, **kwargs)
        Bird.__init__(self, *args, **kwargs)

    def create_animal(self):
        if self.class_name == 'Dog':
            return Dog(self.name, self.age, self.color, self.breed)
        if self.class_name == 'Fish':
            return Fish(self.name, self.age, self.color, self.water_type)
        if self.class_name == 'Bird':
            return Bird(self.name, self.age, self.color, self.migratory_behavior)

    def show_animal_info(self):
        if self.class_name == 'Dog':
            return self.show_dog_info()
        elif self.class_name == 'Fish':
            return self.show_fish_info()
        elif self.class_name == 'Bird':
            return self.show_bird_info()

    def show_dog_info(self):
        return f'I am a {self.color} {self.breed} DOG named {self.name}. I am {self.age} years old, and I love humans'

    def show_fish_info(self):
        return f'I am a {self.color} {self.water_type} FISH named {self.name}. I am {self.age} years old, and I love water'

    def show_bird_info(self):
        return f'I am a {self.color} {self.migratory_behavior} BIRD named {self.name}. I am {self.age} years old, and I love freedom'


bird = Factory('Bird', 'Chiki', 2, 'brown', 'canary')
bird.create_animal()
print(bird.show_animal_info())
dog = Factory('Dog', 'Cuper', 5, 'black', 'Spaniel')
dog.create_animal()
print(dog.show_animal_info())
fish = Factory('Fish', 'Nemo', 1, 'gold', 'marine')
fish.create_animal()
print(fish.show_animal_info())

