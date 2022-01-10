import sys, itertools

def main():
    lines = sys.stdin.readlines()
    data = [lines[i].strip() for i in range(1, len(lines), 2)]
    counts = [[0 for i in range(len(data[0]))] for j in range(4)]
    for d in data:
        for i, j in enumerate(d):
            counts[(lambda x: 0 if x == 'A' else (1 if x == 'C' else (2 if x == 'G' else 3)))(j)][i] += 1

    get_nucleotide = lambda x: 'A' if x == 0 else ('C' if x == 1 else ('G' if x == 2 else 'T'))
    print(''.join([get_nucleotide(i.index(max(i)))
                   for i in zip(*counts)]))
    print('\n'.join([f'{get_nucleotide(j)}: {" ".join([str(j) for j in counts[i]])}' for i in range(4)]))


    

if __name__ == '__main__':
    main()
