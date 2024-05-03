import uuid

class Animal:
    def __init__(self, species, breed, age, health_records):
        self.id = str(uuid.uuid4())  # Генерация уникального ID
        self.species = species
        self.breed = breed
        self.age = age
        self.health_records = health_records
        self.adopted = False

    @property
    def adopted(self):
        return self._adopted

    @adopted.setter
    def adopted(self, value):
        if isinstance(value, bool):
            self._adopted = value
        else:
            raise ValueError("Adopted status must be a boolean")

    def get_info(self):
        return f"ID: {self.id}, Вид: {self.species}, Порода: {self.breed}, Возраст: {self.age}, Здоровье: {self.health_records}"

    def mark_adopted(self):
        self.adopted = True
        return f"Животное с ID {self.id} теперь усыновлено!"


class Dog(Animal):
    def __init__(self, name, age, breed, health_records):
        # Обратите внимание, что класс Animal не принимает параметр name напрямую.
        super().__init__('Собака', breed, age, health_records)
        self.name = name

class Cat(Animal):
    def __init__(self, name, age, breed, health_records):
        # Обратите внимание, что класс Animal не принимает параметр name напрямую.
        super().__init__('Кот', breed, age, health_records)
        self.name = name
