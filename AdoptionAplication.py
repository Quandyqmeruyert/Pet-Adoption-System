class AdoptionApplication:
    def __init__(self, adopter, animal):
        self.adopter = adopter
        self.animal = animal
        self.status = "На рассмотрении"

    def approve(self):
        self.animal.mark_adopted()
        self.status = "Одобрено"
        print(f"Application on adoption of animal with ID {self.animal.id} is approved.")

    def reject(self, reason):
        """Отклоняет заявку на усыновление с указанием причины."""
        self.status = f"Отклонено: {reason}"
        print(f"Application on adoption of animal with ID {self.animal.id} rejected with the reason: {reason}")

    def get_application_info(self):
        """Возвращает информацию о заявке на усыновление."""
        return f"Adopter: {self.adopter.name}, Animal: {self.animal.get_info()}, Status: {self.status}"
