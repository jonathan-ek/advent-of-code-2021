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
                if target[0][0] <= x_pos <= target[0][1] and cur_acc == 0:
                    x_range.append(x)
                    break
                if x_pos > target[0][1]:
                    break
        y_max = abs(target[1][0]+1)
        x_v = x_range[0]
        y_v = y_max
        x_pos = 0
        y_pos = 0
        while True:
            x_pos += x_v
            x_v -= 1 if x_v > 0 else 0
            y_pos += y_v
            y_v -= 1
            y_max = max([y_max, y_pos])
            if target[0][0] <= x_pos <= target[0][1] and target[1][0] <= y_pos <= target[1][1]:
                print('success')
            if x_pos > target[0][1] or y_pos < target[1][0]:
                break
        print(y_max)





if __name__ == '__main__':
    main()
