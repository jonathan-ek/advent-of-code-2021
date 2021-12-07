def main():
    with open('input/01.txt', 'r') as fp:
        data = [int(x) for x in fp.readlines()]
        prev = None
        prev_prev = None
        prev_sum = None
        inc_sum = 0
        for x in data:
            if prev is not None and prev_prev is not None and prev_sum is not None:
                if prev_sum < prev_prev + prev + x:
                    inc_sum += 1
            try:
                prev_sum = prev_prev + prev + x
            except TypeError:
                prev_sum = None
            prev_prev = prev
            prev = x
        print(inc_sum)


if __name__ == '__main__':
    main()
