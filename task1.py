class Soda:
    def show_my_drink(self, dobavka):
        if dobavka == "":
            print("Обычная газировка")
        else:
            print(f"Газировка и {dobavka}")

drink = Soda()
drink.show_my_drink(input("Введите добавку если хотите: "))