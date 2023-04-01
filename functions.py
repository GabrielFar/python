def main():
    hello()
    name = input("What's your name? ")
    hello(name)

#name="world" serve para caso a função seja chamada sem parâmetro
def hello(name="world"):
    print("Hello", name)

main()