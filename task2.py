class TriangleChecker:
    def is_triangle(self, a, b, c):
        if not all(isinstance(side, (int, float)) and side > 0 for side in [a, b, c]):
            return print("Введите корректные значения!!!")
        elif (a<(b+c)) and (b<(a+c)) and (c<(a+b)):
            print("Ура, можно построить треугольник!")
        elif (a<=0) or (b<=0) or (c<=0):
            print("С отрицательными числами ничего не выйдет!")
        else:
            print("Жаль, но из этого треугольник не сделать.")

triangle = TriangleChecker()
try:
    a = int(input())
    b = int(input())
    c = int(input())
    triangle.is_triangle(a, b, c)
except ValueError:
    print("Не числа")
