import uuid
from datetime import datetime

class Adopter:
    def __init__(self, name, contact_info, address):
        self.id = str(uuid.uuid4())  # Генерация уникального ID
        self.name = name
        self.contact_info = contact_info
        self.address = address

    def submit_application(self, application):
        """Добавляет новую заявку на усыновление в список заявок усыновителя."""
        self.applications.append(application)
        print(f"{self.name} подал(а) заявку на усыновление животного с ID {application.animal.id}.")

    def list_applications(self):
        """Выводит список всех заявок на усыновление, поданных усыновителем."""
        if not self.applications:
            print(f"{self.name} пока не подал(а) ни одной заявки на усыновление.")
        else:
            print(f"Заявки на усыновление от {self.name}:")
            for app in self.applications:
                print(f"Животное с ID {app.animal.id}, Статус: {app.status}")
