# "a" = append - manter o que está escrito e adicionar
# "w" = write - reescreve todo o arquivo
# "r" = read - lê o arquivo (opcional)

# ------------------------------------------------------------------------------------------------------------------

# "with" = abre e fecha automaticamente um arquivo

# name = input("What's your name? ")

# with open("python/file_InputOutput/names.txt", "a") as file:
#     file.write(f"{name}\n")

# ------------------------------------------------------------------------------------------------------------------

# "rstrip" elimina as quebras de linha que foram escritas pelo código acima,
# para eliminar dupla quebra de linha no print

# with open("python/file_InputOutput/names.txt") as file:
#     for line in sorted(file):
#         print("Hello,", line.rstrip())

# ------------------------------------------------------------------------------------------------------------------

names = []

with open("python/file_InputOutput/names.txt") as file:
    for line in sorted(file):
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"Hello, {name}")
