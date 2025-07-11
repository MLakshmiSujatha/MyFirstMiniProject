class Person:
    def __init__(self, name, height_cm, weight_kg):
        self.name = name
        self.height_m = height_cm / 100
        self.weight = weight_kg

    def calculate_bmi(self):
        bmi = self.weight / (self.height_m ** 2)
        return round(bmi, 2)

    def category(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal weight"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obese"

# Example usage
if __name__ == "__main__":
    name = input("Enter your name: ")
    height = float(input("Enter height in cm: "))
    weight = float(input("Enter weight in kg: "))

    user = Person(name, height, weight)
    print(f"{user.name}, your BMI is {user.calculate_bmi()} ({user.category()})")
