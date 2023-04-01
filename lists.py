# students = ["Harry", "Hermionne", "Ron"]

# for i in range(len(students)):
#     print(students[i])

# ------------------------------------------------------------------------------------------------------------------

# students = {
#     "Harry": "Gryffindor",
#     "Hermionne": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin"
# }

# for student in students:
#     print(student, students[student])

# ------------------------------------------------------------------------------------------------------------------

# students = [
#     {"name": "Harry", "house": "Gryffindor", "patronus": "Otter"},
#     {"name": "Hermione", "house": "Gryffindor", "patronus": "Stag"},
#     {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
#     {"name": "Draco", "house": "Slytherin", "patronus": None},
# ]

# for student in students:
#     print(student["name"], student["house"], student["patronus"], sep=", ")

# ------------------------------------------------------------------------------------------------------------------

names = []

for _ in range(3):
    names.append(input("What's your name? "))

for name in sorted(names):
    print(f"hello, {name}")
