class KgToPounds:
    def __init__(self):
        self.__kg = float(input("Введите количество килограммов: "))

    @property
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            raise ValueError('Килограммы задаются только числами')

    def to_pounds(self):
        return self.__kg * 2.205

weight = KgToPounds() 
print(f"Килограммы: {weight.kg}") 
print(f"В фунтах: {weight.to_pounds()}")