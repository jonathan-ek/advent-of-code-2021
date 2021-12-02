def main():
    with open('input_02.txt', 'r') as fp:
        data = [(x.split(' ')[0], int(x.split(' ')[1])) for x in fp.readlines()]
        forward = 0
        depth = 0
        aim = 0
        for ins, d in data:
            if ins == 'forward':
                forward += d
                depth += (aim * d)
            if ins == 'up':
                aim -= d
            if ins == 'down':
                aim += d
        print(forward * depth)


if __name__ == '__main__':
    main()
