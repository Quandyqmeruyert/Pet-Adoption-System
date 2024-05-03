from Animal import Animal
from Shelter import Shelter


class Administrator:

    def __init__(self):
        self.shelter = None

    def login_as_administrator():
        # Здесь можно реализовать логику аутентификации администратора
        username = input("Введите имя пользователя (администратора): ")
        password = input("Введите пароль: ")
        # Проверка логина и пароля администратора
        return username == "admin" and password == "admin123"

    def add_shelter(self):
        name = input("Введите название нового питомника: ")
        address = input("Введите адрес нового питомника: ")
        self.shelter = Shelter(name, address)
        print(f"Питомник '{name}' успешно добавлен.")

    def add_animal(self):
        shelter_name = input("Введите название питомника, в который хотите добавить животное: ")
        if self.shelter:
            name = input("Введите имя животного: ")
            age = int(input("Введите возраст животного: "))
            breed = input("Введите породу животного: ")
            health_records = input("Введите медицинские записи животного: ")
            animal = Animal(name, age, breed, health_records)
            self.shelter.add_animal(animal)
            print(f"Животное '{name}' успешно добавлено в питомник '{shelter_name}'.")
        else:
            print(f"Питомник с названием '{shelter_name}' не найден.")
