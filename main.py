from Administrator import Administrator
from Adopter import Adopter
from AdoptionAplication import AdoptionApplication
from AdoptionManager import AdoptionManager
from Animal import Dog, Cat

from ShelterBuilder import ShelterBuilder


def administrator_mode(shelter_manager):
    print("\nAdministrator mode")
    print("Choose the number:")
    print("1. Create shelter")
    print("2. Add animal to the shelter")
    print("3. Delete animl from the shelter")
    print("4. Exit")

    while True:
        choice = input("Choose the number: ")

        if choice == '1':
            name = input("Name: ")
            address = input("Address: ")
            shelter_manager.create_shelter(name, address)
        elif choice == '2':
            shelter_name = input("Shelter name: ")
            animal_type = input("Animal type (dog/cat): ").lower()
            if animal_type == 'dog':
                name = input("Name: ")
                age = int(input("Age: "))
                breed = input("Bread: ")
                health_records = input("Health records: ")
                animal = Dog(name, age, breed, health_records)
            elif animal_type == 'кот':
                name = input("Name: ")
                age = int(input("Age: "))
                breed = input("Bread: ")
                health_records = input("Health records: ")
                animal = Cat(name, age, breed, health_records)
            else:
                print("Error.")
                continue
            shelter_manager.add_animal_to_shelter(shelter_name, animal)
        elif choice == '3':
            shelter_name = input("Shelter name: ")
            animal_id = int(input("Enter nimal ID: "))
            shelter_manager.remove_animal_from_shelter(shelter_name, animal_id)
        elif choice == '4':
            print("Exit from admin mode.")
            break
        else:
            print("Error.")


def client_mode(shelter_builder):
    while True:
        print("\nWelcome to client mode!")
        print("Choose the number:")
        print("1. List the shelters")
        print("2. List aviable animals")
        print("3. Exit")

        choice = input("Choose the number: ")

        if choice == '1':
            shelter_builder.list_all_shelters()
        elif choice == '2':
            shelter_builder.list_all_animals()
            animal_id = input("Enter ID of animal you want to adopt or enter exit to exit: ")
            if choice != "exit":
                print("Registering the adopter")
                name = input("Name: ")
                contact_info = input("Contact-info: ")
                address = input("Address: ")
                adopter = Adopter(name, contact_info, address)
                manager = AdoptionManager()
                manager.submit_application(adopter, shelter_builder.animals[animal_id])
                break
        elif choice == '3':
            print("Exit.")
            break
        else:
            print("Error.")


def main():
    shelter_builder = ShelterBuilder()
    admin = Administrator();

    while True:
        print("\nWelcome!")
        print("Choose the number:")
        print("1. Administrator mode")
        print("2. Client mode")
        print("3. Exit")

        mode = input("Enter the number: ")

        if mode == '1':
            username = input("login: ")
            password = input("password: ")

            if username == "a" and password == "123":
                administrator_mode(shelter_builder)
            else:
                continue
        elif mode == '2':
            client_mode(shelter_builder)
        elif mode == '3':
            print("Exiting.")
            break
        else:
            print("Error.")

if __name__ == "__main__":
    main()