class BMI_Calculator:
    def __init__(self, weight_kg, height_m):
        self._weight_kg = weight_kg
        self._height_m = height_m

    @property
    def weight(self):
        return self._weight_kg

    @property
    def height(self):
        return self._height_m

    def BMI_Value(self):
        return self._weight_kg / (self._height_m ** 2)


weight = float(input("Weight: "))
height = float(input("Height: "))  

person = BMI_Calculator(weight, height)
print("Weight:", person.weight, "kg")
print("Height:", person.height, "m")
print("BMI:", "{:.2f}".format(person.BMI_Value()))