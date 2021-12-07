import collections


def main():
    with open('input/05.txt', 'r') as fp:
        data = [[tuple(int(z) for z in y.split(',')) for y in x.split(' -> ')] for x in fp.readlines()]
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
            else:
                x0 = min(start[0], end[0])
                x1 = max(start[0], end[0])
                if start[0] == x0:
                    left = start
                    right = end
                else:
                    left = end
                    right = start

                if left[1] > right[1]:
                    # down right
                    y = left[1]
                    for y_diff, x in enumerate(range(x0, x1 + 1)):
                        touched.append((x, y - y_diff))
                else:
                    # up right
                    y = left[1]
                    for y_diff, x in enumerate(range(x0, x1 + 1)):
                        touched.append((x, y + y_diff))

        res = [coord for coord, count in collections.Counter(touched).items() if count > 1]
        print(len(res))


if __name__ == '__main__':
    main()
