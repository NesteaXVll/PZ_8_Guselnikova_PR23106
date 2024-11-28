class RealString:
    def __init__(self, value):
        self.value = value
    
    def __len__(self):
        return len(self.value)
    
    def __eq__(self, other):
        # Сравниваем по длине строк
        if isinstance(other, RealString):
            return len(self) == len(other)
        elif isinstance(other, str):
            return len(self) == len(other)
        return False

# Пример использования:
rs1 = RealString("Apple")
rs2 = RealString("Яблок")
rs3 = "Banana"

print(rs1 == rs2)  # False, т.к. длина "Apple" (5) не равна длине "Яблоко" (6)
print(rs1 == rs3)