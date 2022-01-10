import sys, functools

def main():
    line = list(input())
    print(f"{functools.reduce(lambda a,b: a + (1 if b == 'A' else 0), line, 0)} {functools.reduce(lambda a,b: a + (1 if b == 'C' else 0), line, 0)} {functools.reduce(lambda a,b: a + (1 if b == 'G' else 0), line, 0)} {functools.reduce(lambda a,b: a + (1 if b == 'T' else 0), line, 0)}")
    

if __name__ == '__main__':
    main()
