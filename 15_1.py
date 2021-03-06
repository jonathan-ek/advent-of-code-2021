class Node:
    def __init__(self, pos, value):
        self.pos = pos
        self.value = value
        self.distance = None
        self.visited = False

    def __str__(self):
        return f"{str(self.pos)} {str(self.value)} {str(self.distance)}"


def main():
    with open('input/15.txt', 'r') as fp:
        data = [[Node((x, y), int(val)) for x, val in enumerate(row.strip())] for y, row in enumerate(fp.readlines())]
        nodes = [x for y in data for x in y]
        x_max = len(data[0]) - 1
        y_max = len(data) - 1
        initial = data[0][0]
        end = data[y_max][x_max]
        initial.distance = 0
        current = initial
        while True:
            if current == end:
                print(current.distance)
                break
            neighbours = [data[y][x] for x, y in [
                (current.pos[0], current.pos[1] - 1),
                (current.pos[0], current.pos[1] + 1),
                (current.pos[0] - 1, current.pos[1]),
                (current.pos[0] + 1, current.pos[1]),
            ] if 0 <= x <= x_max and 0 <= y <= y_max and not data[y][x].visited]
            for n in neighbours:
                if n.distance is None or n.distance > (current.distance + n.value):
                    n.distance = current.distance + n.value
            current.visited = True
            sorted_nodes = sorted([x for x in nodes if not x.visited and x.distance is not None], key=lambda x: x.distance)
            current = sorted_nodes[0]


if __name__ == '__main__':
    main()
