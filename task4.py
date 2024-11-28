class Nikola:
    def __init__(self):
        name = input("Введите ваше имя: ")

        if name != "Николай":
            self.__name = "Я не " + name + ", а Николай"
        else:
            self.__name = name

        self.age = int(input("Введите ваш возраст: "))

    @property
    def name(self):
        return self.__name

nikola = Nikola() 
print(nikola.name)  
print(nikola.age)  