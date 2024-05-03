
class Shelter:
    def __init__(self, name, address):
            self.name = name
            self.address = address
            self.animals = {}
            self.shelters = {}  # Словарь для хранения информации о питомниках

    def add_animal(self, animal):
        """Добавляет животное в приют по уникальному ID."""
        if animal.id not in self.animals:
            self.animals[animal.id] = animal
            print(f"Животное с ID {animal.id} добавлено в приют {self.name}.")
        else:
            print(f"Животное с ID {animal.id} уже находится в приюте {self.name}.")

    def remove_animal(self, animal_id):
        """Удаляет животное из приюта по ID."""
        if animal_id in self.animals:
            del self.animals[animal_id]
            print(f"Животное с ID {animal_id} удалено из приюта {self.name}.")
        else:
            print(f"Животное с ID {animal_id} не найдено в приюте {self.name}.")

    def list_animals(self):
        """Выводит список всех животных в приюте."""
        if not self.animals:
            print("В приюте пока нет животных.")
        else:
            print(f"Животные в приюте {self.name}:")
            for animal in self.animals.values():
                print(animal.get_info())
