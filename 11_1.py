def flash(point, data, visited):
    visited.append(point)
    count = 1
    def get_value(a, b):
        if a < 0 or b < 0:
            return None
        try:
            return data[b][a]
        except IndexError:
            return None
    x, y = point
    neighbours = [
        (x - 1, y), 
        (x + 1, y),
        (x - 1, y - 1),
        (x, y - 1),
        (x + 1, y - 1),
        (x - 1, y + 1),
        (x, y + 1),
        (x + 1, y + 1),
    ]
    for n in neighbours:
        val = get_value(n[0], n[1])
        if val is not None and val != 0:
            if val == 9:
                data[n[1]][n[0]] = 0
                count += flash(n, data, visited)
            else:
                data[n[1]][n[0]] += 1

    return count


def main():
    with open('input/11.txt', 'r') as fp:
        data = [[int(y) for y in list(x.strip())] for x in fp.readlines()]
        count = 0
        for step in range(100):
            data = [[d+1if d < 9 else 0 for d in row] for row in data]
            visited = []
            for y in range(len(data)):
                for x in range(len(data[y])):
                    if data[y][x] == 0 and (x, y) not in visited:
                        count += flash((x, y), data, visited)
            if step == 1:
                for d in data:
                    print("".join([str(x) for x in d]))
                
        print(count)


if __name__ == '__main__':
    main()
