from Shelter import Shelter

class ShelterBuilder:
    def __init__(self):
        self.shelters = {}
        self.animals = {}

    def create_shelter(self, name, address):
        """Создает новый питомник."""
        if name not in self.shelters:
            self.shelters[name] = Shelter(name, address)
            print(f"Питомник '{name}' создан по адресу: {address}.")
        else:
            print(f"Питомник с названием '{name}' уже существует.")

    def add_animal_to_shelter(self, shelter_name, animal):
        """Добавляет животное в питомник."""
        if shelter_name in self.shelters:
            self.animals.append(animal)
            self.shelters[shelter_name].add_animal(animal)
        else:
            print(f"Питомник с названием '{shelter_name}' не найден.")

    def remove_animal_from_shelter(self, shelter_name, animal_id):
        """Удаляет животное из питомника по его ID."""
        if shelter_name in self.shelters:
            self.shelters[shelter_name].remove_animal(animal_id)
        else:
            print(f"Питомник с названием '{shelter_name}' не найден.")

    def list_all_shelters(self):
        """Выводит список всех питомников."""
        if not self.shelters:
            print("В системе нет зарегистрированных питомников.")
        else:
            print("Список зарегистрированных питомников:")
            for shelter_name in self.shelters:
                print(shelter_name)

    def list_all_animals(self):
        """Выводит список всех питомников."""
        if not self.animals:
            print("В системе нет зарегистрированных питомников.")
        else:
            print("Список зарегистрированных питомников:")
            for animal in self.animals:
                print("ID: " + animal.id + "; name: " + animal.name)

    def get_shelter(self, shelter_name):
        """Возвращает объект питомника по его имени."""
        return self.shelters.get(shelter_name)
