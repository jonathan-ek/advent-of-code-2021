import collections


def main():
    with open('input_05.txt', 'r') as fp:
        data = [[tuple(int(z) for z in y.split(',')) for y in x.split(' -> ')] for x in fp.readlines()]
        data = [d for d in data if d[0][0] == d[1][0] or d[0][1] == d[1][1]]
        touched = []
        for start, end in data:
            if start[0] == end[0]:
                x = start[0]
                y0 = min(start[1], end[1])
                y1 = max(start[1], end[1])
                for y in range(y0, y1+1):
                    touched.append((x, y))
            elif start[1] == end[1]:
                y = start[1]
                x0 = min(start[0], end[0])
                x1 = max(start[0], end[0])
                for x in range(x0, x1+1):
                    touched.append((x, y))

        res = [coord for coord, count in collections.Counter(touched).items() if count > 1]
        print(len(res))


if __name__ == '__main__':
    main()
