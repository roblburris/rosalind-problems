import sys

def main():
    lines = sys.stdin.readlines()
    data = [lines[i].strip() for i in range(len(lines))]
    print(f'{sum(list(map(lambda x: 1 if data[0][x] != data[1][x] else 0, [i for i in range(len(data[0]))])))}')

if __name__ == '__main__':
    main()
