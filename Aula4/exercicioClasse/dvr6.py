class Temperatura:
    def __init__(self, celsius: float):
        self.celsius = celsius 

    def convertorFahrenheit(self):
        return (self.celsius * 1.8) + 32
    
    def convertorKelvin(self):
        return self.celsius + 273
    
    def __str__(self):
        return (
            "\n"
            "========== INFORMAÇÕES DE TEMPERATURA ==========\n"
            f"Temperatura em Celsius: {self.celsius:.2f}°C\n"
            f"Temperatura em Fahrenheit: {self.convertorFahrenheit():.2f}°F\n"
            f"Temperatura em Kelvin: {self.convertorKelvin():.2f}°K\n"
            "================================================\n"
        )

t1 = Temperatura(25)
print(t1)