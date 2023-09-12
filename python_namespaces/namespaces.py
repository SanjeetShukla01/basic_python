
my_string = "This is a global string variable"


def print_string():
    print("string_variable")
    string_variable = "this is a string to be printed"
    print(locals())


if __name__ == "__main__":
    # print(dir(__builtins__))
    # print(globals())
    print_string()