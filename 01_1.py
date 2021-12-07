def main():
    with open('input/01.txt', 'r') as fp:
        data = [int(x) for x in fp.readlines()]
        prev = None
        inc_sum = 0
        for x in data:
            if prev is not None and x > prev:
                inc_sum += 1
            prev = x
        print(inc_sum)


if __name__ == '__main__':
    main()
