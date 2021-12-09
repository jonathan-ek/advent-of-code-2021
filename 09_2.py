
def add_neighbours(matrix, point, points):
    def get_value(a, b):
        if a < 0 or b < 0:
            return None
        try:
            return matrix[b][a]
        except IndexError:
            return None
    if point in points:
        return
    points.append(point)
    x, y = point
    left = get_value(x - 1, y)
    right = get_value(x + 1, y)
    up = get_value(x, y - 1)
    down = get_value(x, y + 1)
    if left is not None and left != 9:
        add_neighbours(matrix, (x - 1, y), points)
    if right is not None and right != 9:
        add_neighbours(matrix, (x + 1, y), points)
    if up is not None and up != 9:
        add_neighbours(matrix, (x, y - 1), points)
    if down is not None and down != 9:
        add_neighbours(matrix, (x, y + 1), points)


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
        areas = dict()
        for point in low_point:
            tmp = []
            add_neighbours(data, point, tmp)
            areas[point] = len(tmp)
        larges_areas = sorted(areas.values(), reverse=True)[:3]
        prod = 1
        for l in larges_areas:
            prod *= l
        print(prod)


if __name__ == '__main__':
    main()
