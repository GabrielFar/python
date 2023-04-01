while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        # print("x isn't an integer")
        pass
    else:
        break

print(f'x is {x}')