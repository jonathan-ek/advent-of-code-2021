def main():
    with open('input/07.txt', 'r') as fp:
        data = [int(x) for x in fp.readlines()[0].split(',')]
        d_min = min(data)
        d_max = max(data)
        distances = {}
        for d in range(d_min, d_max+1):
            tmp = 0
            for c in data:
                tmp += abs(d - c)
            distances[d] = tmp
        print(sorted(distances.items(), key=lambda x: x[1])[0][1])


if __name__ == '__main__':
    main()
