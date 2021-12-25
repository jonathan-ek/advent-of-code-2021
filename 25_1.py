def main():
    with open('input/25.txt', 'r') as fp:
        data = [[y for y in x.strip()] for x in fp.readlines()]
        i = 0
        while True:
            moves = []
            has_moved = False
            for y in range(len(data)):
                for x in range(len(data[y])):
                    if data[y][x] == '.' and data[y][x-1] == '>':
                        moves.append(((x, y), (x-1, y)))
                        has_moved = True

            for (x_from, y_from), (x_to, y_to) in moves:
                tmp = data[y_from][x_from]
                data[y_from][x_from] = data[y_to][x_to]
                data[y_to][x_to] = tmp

            moves = []
            for y in range(len(data)):
                for x in range(len(data[y])):
                    if data[y][x] == '.' and data[y-1][x] == 'v':
                        moves.append(((x, y), (x, y-1)))
                        has_moved = True

            for (x_from, y_from), (x_to, y_to) in moves:
                tmp = data[y_from][x_from]
                data[y_from][x_from] = data[y_to][x_to]
                data[y_to][x_to] = tmp
            i += 1
            if not has_moved:
                break
        print(i)


if __name__ == '__main__':
    main()
