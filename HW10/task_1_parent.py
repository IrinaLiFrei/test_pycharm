
class Animal:
    def __init__(self, name: str, age: int, color: str):
        self.name = name
        self.age = age
        self.color = color or 'unknown'

    def show_animal_info(self):
        return f'Hi! I am {self.name}, and I dont know who I am'


class Dog(Animal):
    def __init__(self, name: str, age: int, color: str, breed: str = None):
        super().__init__(name, age, color)
        self.breed = breed or 'unknown'

    def show_animal_info(self):
        return f'I am a {self.color} {self.breed} dog named {self.name}. I am {self.age} years old, and I love humans'


class Fish(Animal):
    def __init__(self, name: str, age: int, color: str, water_type: str = None):
        super().__init__(name, age, color)
        self.water_type = water_type or 'unknown'

    def show_animal_info(self):
        return f'I am a {self.color} {self.water_type} fish named {self.name}. I am {self.age} years old, and I love water'


class Bird(Animal):
    def __init__(self, name: str, age: int, color: str, migratory_behavior: str = None):
        super().__init__(name, age, color)
        self.migratory_behavior = migratory_behavior or 'unknown'

    def show_animal_info(self):
        return f'I am a {self.color} {self.migratory_behavior} bird named {self.name}. I am {self.age} years old, and I love freedom'

