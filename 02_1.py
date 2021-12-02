def main():
    with open('input_02.txt', 'r') as fp:
        data = [(x.split(' ')[0], int(x.split(' ')[1])) for x in fp.readlines()]
        forward = 0
        depth = 0
        for ins, d in data:
            if ins == 'forward':
                forward += d
            if ins == 'up':
                depth -= d
            if ins == 'down':
                depth += d
        print(forward * depth)


if __name__ == '__main__':
    main()
