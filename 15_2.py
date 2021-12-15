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
        data = [[int(val) for val in row.strip()] for row in fp.readlines()]
        big_data = [[(data[y][x] + (xit + yit)) % 9 or 9 for xit in range(5) for x in range(len(data[0]))] for yit in range(5) for y in range(len(data)) ]
        data = [[Node((x, y), int(val)) for x, val in enumerate(row)] for y, row in enumerate(big_data)]
        nodes = [x for y in data for x in y]
        total = len(nodes)
        x_max = len(data[0]) - 1
        y_max = len(data) - 1
        initial = data[0][0]
        end = data[y_max][x_max]
        initial.distance = 0
        current = initial
        i = 0
        unvisited_with_value = []
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
                    unvisited_with_value.append(n)
            current.visited = True
            unvisited_with_value = [x for x in unvisited_with_value if not x.visited]
            sorted_nodes = sorted([x for x in unvisited_with_value], key=lambda x: x.distance)
            i += 1
            if i % 400 == 100:
                print(len([x for x in nodes if x.visited]) / total)
            current = sorted_nodes[0]


if __name__ == '__main__':
    main()
