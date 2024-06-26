#1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты
# (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.

#2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`,
# которые наследуют от класса `Animal`.
# Добавьте специфические атрибуты и переопределите методы, если требуется
# (например, различный звук для `make_sound()`).

#3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()` для каждого животного.

#4. Используйте композицию для создания класса `Zoo`, который будет содержать
# информацию о животных и сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.

#5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`,
# которые могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper` и
# `heal_animal()` для `Veterinarian`).



#Попробуйте добавить дополнительные функции в вашу программу, такие как сохранение
# информации о зоопарке в файл и возможность её загрузки, чтобы у вашего зоопарка было "постоянное состояние"
# между запусками программы.


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age



    def make_sound(self):
        pass

    def eat(self):
        pass

class Bird(Animal):
    def __init__(self, name, age, flying_speed):
        super().__init__(name, age)
        self.flying_speed = flying_speed
    def make_sound(self):
        print("чик-чирик")

class Mammal(Animal):
    def __init__(self, name, age, running_speed):
        super().__init__(name, age)
        self.running_speed = running_speed
    def make_sound(self):
        print("гав-гав")

class Reptile(Animal):
    def __init__(self, name, age, crawling_speed):
        super().__init__(name, age)
        self.crawling_speed = crawling_speed
    def make_sound(self):
        print("клац-клац")

animals = [Bird("Воробей", 3, 10),
           Mammal("Собака", 2, 5),
           Reptile("Крокодил", 1, 3)]
for animal in animals:
    animal.make_sound()

class Zoo:
    def __init__(self):
        self.animals = []
        self.zookeepers = []
        self.veterinarians = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"животное {animal.name} добавлено в зоопарк")

    def add_zookeeper(self, zookeeper):
        self.zookeepers.append(zookeeper)

    def add_veterinarian(self, veterinarian):
        self.veterinarians.append(veterinarian)


class ZooKeeper:
    def feed_animal(self, animal, food):

        print(f"Животное {animal.name} покормлено")

class Veterinarian:
    def heal_animal(self, animal):
        print(f"Лечим животное {animal.name}")


# Создание объектов животных
bird = Bird("Воробей", 3, 10)
mammal = Mammal("Собака", 2, 5)
reptile = Reptile("Крокодил", 1, 3)


# Создание сотрудников зоопарка
keeper = ZooKeeper()
veterinarian = Veterinarian()

# Создание зоопарка и добавление в него животных и сотрудников
zoo = Zoo()
keeper = ZooKeeper()
veterinarian = Veterinarian()
zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)
keeper.feed_animal(bird, "мясо")





