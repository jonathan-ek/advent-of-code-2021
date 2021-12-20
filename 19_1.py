import collections
import math


class Scanner:
    def __init__(self, data):
        tmp = data.split('\n')
        self.name = tmp[0]
        self.current_offset = (0, 0, 0)
        self.beacons = [tuple([int(y) for y in x.split(',')]) for x in tmp[1:]]
        self.internal_distances = []
        self.calculate_internal_distances()

    def calculate_internal_distances(self):
        self.internal_distances = []
        for b in self.beacons:
            for c in reversed(self.beacons):
                if b == c:
                    break
                self.internal_distances.append(
                    (b, c, math.sqrt(math.pow(b[0] - c[0], 2) + math.pow(b[1] - c[1], 2) + math.pow(b[2] - c[2], 2))))

    def transform(self, pos, sign):
        new_beacons = []
        for b in self.beacons:
            new_b = [b[i] for i in pos]
            new_b = tuple([new_b[i] * sign[i] for i in range(3)])
            new_beacons.append(new_b)
        self.beacons = new_beacons
        self.calculate_internal_distances()

    def offset(self, offset):
        new_beacons = []
        self.current_offset = offset
        for b in self.beacons:
            new_b = tuple([b[i] + offset[i] for i in range(3)])
            new_beacons.append(new_b)
        self.beacons = new_beacons
        self.calculate_internal_distances()


def find_transform(scanner_0, scanner):
    transforms = set()
    for x in scanner_0.internal_distances:
        for y in scanner.internal_distances:
            if x[2] == y[2]:
                x_diff = [x[0][0] - x[1][0], x[0][1] - x[1][1], x[0][2] - x[1][2]]
                y_diff = [y[0][0] - y[1][0], y[0][1] - y[1][1], y[0][2] - y[1][2]]
                # print(x[0], x[1],x_diff,  y[0], y[1], y_diff)
                x_diff_abs = [abs(i) for i in x_diff]
                y_diff_abs = [abs(i) for i in y_diff]
                try:
                    y_pos = tuple([x_diff_abs.index(i) for i in y_diff_abs])
                except ValueError:
                    continue
                if not (0 in y_pos and 1 in y_pos and 2 in y_pos):
                    continue
                new_y = [y_diff[i] for i in y_pos]
                y_sign = tuple([1 if new_y[i] == x_diff[i] else -1 for i in range(3)])
                transforms.add((y_pos, y_sign))
    return transforms


def find_offset(scanner_0, scanner):
    x_list = []
    y_list = []
    z_list = []
    matches = 0
    for x in scanner_0.internal_distances:
        for y in scanner.internal_distances:
            if x[2] == y[2]:
                matches += 1
                x_list.append(x[0][0] - y[0][0])
                x_list.append(x[0][0] - y[1][0])
                y_list.append(x[0][1] - y[0][1])
                y_list.append(x[0][1] - y[1][1])
                z_list.append(x[0][2] - y[0][2])
                z_list.append(x[0][2] - y[1][2])
    x = sorted(collections.Counter(x_list).items(), key=lambda i: i[1], reverse=True)[0]
    y = sorted(collections.Counter(y_list).items(), key=lambda i: i[1], reverse=True)[0]
    z = sorted(collections.Counter(z_list).items(), key=lambda i: i[1], reverse=True)[0]
    return (x[0], y[0], z[0]), (x[1] / matches, y[1] / matches, z[1] / matches)


def main():
    with open('input/19.txt', 'r') as fp:
        d = fp.read()
        data = [Scanner(x) for x in d.split('\n\n')]
        scanner_0 = data[0]
        scanners = data[1:]
        while True:
            remove = None
            for i, scanner in enumerate(scanners):
                tmp = set([x[2] for x in scanner_0.internal_distances])
                tmp_2 = set([x[2] for x in scanner.internal_distances])
                res = tmp.intersection(tmp_2)
                if len(res) >= 12:
                    j = 0
                    while True:
                        j += 1
                        tr = list(find_transform(scanner_0, scanner))
                        if ((0, 1, 2), (1, 1, 1)) in tr or ((0, 1, 2), (-1, -1, -1)) in tr:
                            break
                        y_pos, y_sign = tr[0]
                        if j % 3 == 0:
                            # To tired to understand the issue.
                            # Just do some random transform and hope we find the correct.
                            y_pos = (2, 1, 0)
                            y_sign = (-1, 1, -1)
                        scanner.transform(y_pos, y_sign)
                    offset, probability = find_offset(scanner_0, scanner)
                    if probability[0] < 0.9 or probability[1] < 0.9 or probability[2] < 0.9:
                        scanner.transform([0, 1, 2],
                                          [-1 if probability[0] < 0.9 else 1, -1 if probability[1] < 0.9 else 1,
                                           -1 if probability[2] < 0.9 else 1])
                        offset, probability = find_offset(scanner_0, scanner)
                    if probability[0] < 0.9 or probability[1] < 0.9 or probability[2] < 0.9:
                        # To tired to understand the issue.
                        # Just do some random transform and hope we find the correct in the coming iterations.
                        scanner.transform((1, 2, 0), (-1, 1, -1))
                        continue
                    print(scanner.name, offset, probability)
                    scanner.offset(offset)
                    scanner_0.beacons = list({*scanner_0.beacons, *scanner.beacons})
                    scanner_0.calculate_internal_distances()
                    remove = i
                    break
            if remove is not None:
                scanners.pop(remove)
            if len(scanners) == 0:
                break
        print(len(scanner_0.beacons))

        # high 471
        # low 425
        print()
        cur_max = 0
        for s0 in data:
            for s1 in data:
                cur_max = max(cur_max, (
                        abs(s0.current_offset[0] - s1.current_offset[0]) +
                        abs(s0.current_offset[1] - s1.current_offset[1]) +
                        abs(s0.current_offset[2] - s1.current_offset[2])
                )
                              )
        print(cur_max)
        # too low 9612


if __name__ == '__main__':
    main()
