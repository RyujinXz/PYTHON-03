class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


    def __str__(self):
        return (
            "\n"
            "==========INFORMAÇÕES==========\n"
            f"🌟 Nome: {self.name}\n"
            f"🎂 Idade: {self.age}\n"
            "==============================="
    )


p1 = Person("John", 36)
p2 = Person("Katarina", 28)
p3 = Person("Richard", 24)
p4 = Person("Matheus", 17)
p5 = Person("Yasmin", 19)
print(p1)
print(p2)
print(p3)
print(p4)
