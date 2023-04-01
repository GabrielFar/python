# import random

# print(random.choice(['head', 'tails']))

# print(random.randint(0, 9))

# list = ['A', 'B', 'C']
# random.shuffle(list)
# for _ in list:
#     print(_)

# -----------------------------------------------------------------------------------------------------------------

# import statistics

# print(statistics.mean([100, 90])) -------- média

# -----------------------------------------------------------------------------------------------------------------

# import sys

# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")

# print("hello, my name is", sys.argv[1])

# ----------------------------------------------------------------------------------------------------------------

# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")

# for arg in sys.argv[1:-1]:            #"1:-1" significa do elemento de index 1 até o penúltimo elemento
#     print("Hello, my name is", arg)

# for arg in sys.argv[1:]:              #"1:" significa do elemento de index 1 até o final
#     print("Hello, my name is", arg)

# -----------------------------------------------------------------------------------------------------------------

# import cowsay
# import sys

# if len(sys.argv) == 2:
#     cowsay.trex("Hello, " + sys.argv[1])
#     cowsay.cow("Hello, " + sys.argv[1])

# -----------------------------------------------------------------------------------------------------------------
