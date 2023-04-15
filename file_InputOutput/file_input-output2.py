# with open("python/file_InputOutput/hogwarts.csv") as file:
#     for line in file:
#         row = line.rstrip().split(",")
#         print(f"{row[0]} is in {row[1]}")

# ------------------------------------------------------------------------------------------------------------------

# students = []

# with open("python/file_InputOutput/hogwarts_house.csv") as file:
#     for line in sorted(file):
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)

# # lambda é uma função anônima. Pega o parâmetro objeto student e retorna o nome

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is in {student['house']}")

# ------------------------------------------------------------------------------------------------------------------

# import csv

# students = []

# with open("python/file_InputOutput/hogwarts_home.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name": row["name"], "home": row["home"]})

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")

# ------------------------------------------------------------------------------------------------------------------

# import csv

# name = input("What's youyr name? ")
# home = input("Where's your home? ")

# with open("python/file_InputOutput/hogwarts_home2.csv", "a") as file:
#     # fieldnames serve para dizer ao programa em qual coluna os dados devem ir
#     writer = csv.DictWriter(file, fieldnames=["name", "home"])
#     writer.writerow({"name": name, "home": home})
