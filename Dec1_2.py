import math
def read_file():
    with open('data/dec1_1.txt') as f:
        lines = list(map(int, f.read().splitlines()))

    return lines

def run():
    lines = read_file()
    counter = 0
    running_sum = 3
    for i in range(0,len(lines)-running_sum):
        if int(lines[i+running_sum]) > int(lines[i]):
            counter+=1
    return print(counter)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()

#1497
