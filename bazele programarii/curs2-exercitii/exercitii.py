
def pattern():
    i = 1
    while i <= 5:
        j = 1
        char = ""
        while j <= i:
            char = char + "*"
            j = j + 1
        print(char)
        print("\n")
        i = i + 1


if __name__ == '__main__':
    pattern()