def show_hello_message(student_name):
    hello_message = "Welcome to your first Python course"
    hello_with_name = '{}, {}'.format(hello_message, student_name)
    show_message(hello_with_name)
    show_additional_message(hello_with_name)


def show_message(message):
    print(message)


def show_additional_message(message):
    if is_hello_message(message):
        show_message_char_by_char("And welcome to my course!")
    else:
        show_message_char_by_char("Welcome back")


def is_hello_message(message):
    """
    You can verify if a substring is part of a string with the word "in".
    This will return a boolean condition.
    If you want to verify that a word is not part of a string you can use 'not in'
    """
    if "Welcome" in message:
        return True
    return False  # you return a value by return word
    # short form : return "hello" in hello_message


def show_message_char_by_char(hello_message):
    """
     Strings are Arrays. Square brackets can be used to access elements of the string.
     hello_message[0] where hello_message is "ana" will be "a" char
     for syntax will execute every step from 0 to the len of the hello message - 1
     """
    for char in hello_message:
        print(char)


def show_hello_len(hello_message):
    # len will return the length of the string
    # len(ana) will return 3
    print(len(hello_message))


if __name__ == '__main__':
    show_hello_message('Florin')
