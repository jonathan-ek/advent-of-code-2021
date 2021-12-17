def main():
    with open('input/17.txt', 'r') as fp:
        data = [x.strip() for x in fp.readlines()][0].strip('target area: ').split(', ')
        target = [[int(y) for y in x[2:].split('..')] for x in data]
        x_range = []
        for x in range(target[0][1]):
            x_pos = 0
            cur_acc = x
            while cur_acc != 0:
                x_pos += cur_acc
                cur_acc -= 1
                if target[0][0] <= x_pos <= target[0][1]:
                    x_range.append(x)
                    break
                if x_pos > target[0][1]:
                    break

        y_max = abs(target[1][0] + 1)
        successful = []
        for x in range(target[0][0], target[0][1] + 1):
            for y in range(target[1][0], target[1][1] + 1):
                successful.append((x, y))

        for x in x_range:
            for y in range(target[1][0], y_max+1):
                if (x, y) in successful:
                    continue
                x_v = x
                y_v = y
                x_pos = 0
                y_pos = 0
                while True:
                    x_pos += x_v
                    x_v -= 1 if x_v > 0 else 0
                    y_pos += y_v
                    y_v -= 1
                    if target[0][0] <= x_pos <= target[0][1] and target[1][0] <= y_pos <= target[1][1]:
                        successful.append((x, y))
                        break
                    if x_pos > target[0][1] or y_pos < target[1][0]:
                        break
        print(len(successful))


if __name__ == '__main__':
    main()
