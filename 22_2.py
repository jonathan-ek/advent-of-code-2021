class Box:
    def __init__(self, x_range, y_range, z_range):
        self.min_point = (x_range[0], y_range[0], z_range[0])
        self.max_point = (x_range[1], y_range[1], z_range[1])

    def __str__(self):
        return f"({self.min_point[0]}, {self.min_point[1]}, {self.min_point[2]}), ({self.max_point[0]}, {self.max_point[1]}, {self.max_point[2]})"

    @property
    def size(self):
        return ((self.max_point[0] - self.min_point[0]) + 1) * ((self.max_point[1] - self.min_point[1]) + 1) * (
                (self.max_point[2] - self.min_point[2]) + 1)

    def overlap(self, other_box):
        min_x = min(other_box.max_point[0], self.max_point[0])
        max_x = max(other_box.min_point[0], self.min_point[0])
        min_y = min(other_box.max_point[1], self.max_point[1])
        max_y = max(other_box.min_point[1], self.min_point[1])
        min_z = min(other_box.max_point[2], self.max_point[2])
        max_z = max(other_box.min_point[2], self.min_point[2])
        x_diff = max(min_x - max_x, -1) + 1
        y_diff = max(min_y - max_y, -1) + 1
        z_diff = max(min_z - max_z, -1) + 1
        if (x_diff * y_diff * z_diff) > 0:
            return Box(
                x_range=[max_x, min_x],
                y_range=[max_y, min_y],
                z_range=[max_z, min_z],
            )
        else:
            return None


def parse(state, cuboid):
    return state, Box(*[[int(y) for y in (x.split('=')[1]).split('..')] for x in cuboid.split(',')])


def main():
    with open('input/22.txt', 'r') as fp:
        lines = fp.readlines()
        data = [parse(*x.split(' ')) for x in lines]
        res = []
        for state, box in data:
            diffs = []
            if state == 'on':
                diffs.append((state, box))
            for res_state, res_box in res:
                overlap = box.overlap(res_box)
                if overlap and res_state == 'on':
                    diffs.append(('off', overlap))
                elif overlap and res_state == 'off':
                    diffs.append(('on', overlap))
            for diff in diffs:
                res.append(diff)
        print(sum([-1 * b.size if c == 'off' else b.size for c, b in res]))


if __name__ == '__main__':
    main()
