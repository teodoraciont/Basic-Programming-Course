def print_undefined_variable():
    print(x)


def print_undefined_variable_simple():
    try:
        print(x)
    except:
        print("An exception occurred")


def print_undefined_variable_more_info():
    try:
        print(x)
    except Exception as exception:
        print("An exception occurred. The exception is: {}".format(exception))
        print("The exception type is {}".format(type(exception).__name__))


def print_undefined_specific_exception():
    try:
        print(x)
    except NameError:
        print("An NameError exception occurred, so the variable it is not defined!")


def divide_10_with_number(number):
    try:
        result = 10 / number
    except ZeroDivisionError as e:
        print("Cannot divide with 0")
        print(type(e).__name__)
    else:
        print("The division result is {}".format(result))


def transform_string_to_int(string):
    result = 0
    try:
        result = int(string)
    except ValueError:
        print("Cannot transform this string {} in int".format(string))
    finally:
        print("The conversion result is {}".format(result))
        return result


def get_user_feedback():
    while True:
        try:
            x = int(input("Please enter a number: "))
            print("10/{} is... {}".format(x, 10 / int(x)))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
        except ZeroDivisionError:
            print("Cannot divide this number with 0 dude! Do the math!!!")


def raise_an_exception():
    x = "hello"
    if not type(x) is int:
        raise TypeError("Only integers are allowed")


if __name__ == '__main__':
    print_undefined_variable()
    print_undefined_variable_simple()
    print_undefined_variable_more_info()
    print_undefined_specific_exception()
    divide_10_with_number(2)
    divide_10_with_number(0)
    transform_string_to_int("2")
    transform_string_to_int("bla bal bak")
    get_user_feedback()
    raise_an_exception()
