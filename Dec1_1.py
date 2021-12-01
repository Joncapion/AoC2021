
def read_file():
    with open('data/dec1_1.txt') as f:
        lines = list(map(int,f.read().splitlines()))

    return lines

def run():
    lines = read_file()
    counter = 0
    for i in range(0,len(lines)-1):
        if int(lines[i+1]) > int(lines[i]):
            counter+=1
    return print(counter)

if __name__ == '__main__':
    run()

