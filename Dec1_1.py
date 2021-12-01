# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def read_file():
    with open('data/dec1_1.txt') as f:
        lines = f.readlines()

    print(lines)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read_file()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
