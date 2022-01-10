def main():
    print(f"{''.join(list(map(lambda x: 'A' if x == 'T' else ('T' if x == 'A' else ('C' if x == 'G' else 'G')), input()))[::-1])}")

if __name__ == '__main__':
    main()
