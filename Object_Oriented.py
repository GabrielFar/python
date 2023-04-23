# def main():
#     student = get_student()
#     print(f"{student[0]} from {student[1]}")


# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return (name, house)
#     # sem ou com parênteses o programa reconhece como uma tupla


# if __name__ == "__main__":
#     main()

# ----------------------------------------------------------------------------------------------------------------

# class Student:
#     def __init__(self, name, house, patronus):
#         if not name:
#             raise ValueError("Missing name")
#         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#             raise ValueError("Invalid house")
#         self.name = name
#         self.house = house
#         self.patronus = patronus

#     def __str__(self):
#         return f"{self.name} from {self.house}"

#     def charm(self):
#         match self.patronus:
#             case "Stag":
#                 return "🦌"
#             case "Otter":
#                 return "🦦"
#             case "Jack Russell Terrier":
#                 return "🐶"
#             case _:
#                 return "No patronus"


# def main():
#     student = get_student()
#     print("Expecto Patronum!", student.charm())


# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     patronus = input("Patronus: ")
#     return Student(name, house, patronus)


# if __name__ == "__main__":
#     main()

# ----------------------------------------------------------------------------------------------------------------
# O código acima pemitia que as propriedades fossem alteradas a qualquer momento,
# burlando a checagem de erro das casas, por exemplo


# O código abaixo ainda tem este erro na variável _house, mas é uma conveção da
# comunidade programadora que se uma variável tem o símbolo "_" quer dizer "Não toque nessa variável"


class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
