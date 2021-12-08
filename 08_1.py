def main():
    with open('input/08.txt', 'r') as fp:
        data = [[[z.strip() for z in y.split(' ')] for y in x.split(' | ')] for x in fp.readlines()]
        count = 0
        for key, value in data:
            for v in value:
                if len(v) in [2,3,4,7]:
                    count += 1


        print(count)

if __name__ == '__main__':
    main()
