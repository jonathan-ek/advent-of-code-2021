def main():
    with open('input/09.txt', 'r') as fp:
        data = [[int(y) for y in x.strip()] for x in fp.readlines()]

        def get_value(x, y):
            if x < 0 or y < 0:
                return None
            try:
                return data[y][x]
            except IndexError:
                return None

        low_point = []
        risk = 0
        for y in range(len(data)):
            for x in range(len(data[y])):
                current = get_value(x, y)
                left = get_value(x - 1, y)
                right = get_value(x + 1, y)
                up = get_value(x, y - 1)
                down = get_value(x, y + 1)
                neighbours = [x for x in [left, right, up, down] if x is not None]

                if min(neighbours) <= current:
                    continue
                low_point.append((x, y))
                risk += current + 1

        print(risk)


if __name__ == '__main__':
    main()
