def main():
    # print_column(3)
    # print_row(4)
    print_rectangle(4, 1)


def print_column(height):
    for _ in range(height):
        print("#")


def print_row(width):
    print("#" * width)


def print_rectangle(height, width):
    for _ in range(height):
        print_row(width)


main()
