from AdoptionAplication import AdoptionApplication


class AdoptionManager:
    def __init__(self):
        self.applications = []  # Список всех заявок на усыновление

    def submit_application(self, adopter, animal):
        application = AdoptionApplication(adopter, animal)
        self.applications.append(application)
        print(f"Заявка на усыновление животного {animal.id} подана усыновителем {adopter.name}.")
        self.auto_process_application(application)  # Обработка заявки

    def auto_process_application(self, application):
        print("To assess your readiness for pet adoption, please answer the following questions:")
        print("1. How many hours per day can you dedicate to caring for a pet?")
        time_for_care = float(input())

        print("2. Do you have experience in owning and caring for pets? (yes/no)")
        experience = input().lower()

        print("3. What future plans do you have that may affect your ability to care for a pet?")
        future_plans = input()

        print("4. Are you willing to allocate a budget for medical services and pet care? (yes/no)")
        budget = input().lower()

        print("5. How would you rate your skills in training and raising a pet? (excellent/good/average/poor)")
        training_skills = input().lower()

        print(
            "6. Do you currently have pets at home? If yes, how do you plan to integrate a new member into your family? (share your experience)")
        current_pets = input()

        print(
            "7. Are you ready to undergo the process of adaptation and acclimatization for the pet to your home and lifestyle? (yes/no)")
        adaptation = input().lower()

        # Оценка готовности клиента
        eligibility_score = 0

        # Оценка времени на уход за животным
        if time_for_care >= 2:
            eligibility_score += 1

        # Оценка опыта
        if experience == "yes":
            eligibility_score += 1

        # Оценка готовности выделить бюджет
        if budget == "yes":
            eligibility_score += 1

        # Оценка навыков в обучении и воспитании
        if training_skills in ["excellent", "good"]:
            eligibility_score += 1

        # Оценка готовности к адаптации
        if adaptation == "yes":
            eligibility_score += 1

        # Проверка наличия текущих домашних животных
        if current_pets:
            eligibility_score += 1

        # Вывод результатов оценки
        if eligibility_score >= 4:
            application.approve()
        else:
            application.reject("Unfortunately, you are not yet ready to adopt a pet. Consider preparing and training.")
            print()

    def list_all_applications(self):
        if not self.applications:
            print("Заявок на усыновление пока нет.")
        else:
            for app in self.applications:
                print(app.get_application_info())
