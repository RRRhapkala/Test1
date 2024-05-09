class Human:
    def __init__(self, name: str, surname: str, age: int, sex: str, is_gay: bool, nuzda: int):
        self.name = name
        self.surname = surname
        self.age = age
        self.sex = sex
        self.is_gay = is_gay
        self.nuzda = nuzda        

    def pokakaj(self):
        if self.nuzda >= 50:
            print("Я пошел срать")
        else:
            print("Не хочу срать")

    def get_info(self):
        gender = "straight" if not self.is_gay else "gay"
        print(f"My name is: {self.name}\nMy surname is: {self.surname}\nI am {self.age} years old\n"
              f"My gender is {self.sex}\nI am {gender}")


Human_1 = Human('Ryhor', 'Hapkala', 20, 'Male', False, 44)
Human_1.get_info()
print('------------------------------')
Human_1.pokakaj()

# Определяем функцию ride_a_car только для Human_1
def ride_a_car(human_instance, car_type: str):
    print(f"{human_instance.name} is riding a {car_type} car")

# Присваиваем ride_a_car только Human_1
Human_1.ride_a_car = ride_a_car

# Используем ride_a_car только для Human_1
print('------------------------------')
Human_1.ride_a_car(Human_1, 'Audi')


def spacja():
    pass