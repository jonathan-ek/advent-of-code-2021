

def main():
    with open('input/08.txt', 'r') as fp:
        data = [[[sorted([v for v in z.strip()]) for z in y.split(' ')] for y in x.split(' | ')] for x in fp.readlines()]
        count = 0
        for key, value in data:
            numbers = [*key, *value]
            numbers = [x for x in set([''.join(n) for n in numbers])]

            one = [n for n in numbers if len(n) == 2][0]
            seven = [n for n in numbers if len(n) == 3][0]
            four = [n for n in numbers if len(n) == 4][0]
            eight = [n for n in numbers if len(n) == 7][0]
            three = [n for n in numbers if len(n) == 5 and len(set(list(n)).difference(set(list(seven)))) == 2][0]
            numbers = [x for x in set(numbers).difference({one, seven, four, eight, three})]
            five = [n for n in numbers if len(n) == 5 and len(set(list(n)).difference(set(list(four)))) == 2][0]
            numbers = [x for x in set(numbers).difference({five})]
            two = [n for n in numbers if len(n) == 5][0]
            numbers = [x for x in set(numbers).difference({two})]
            nine = [n for n in numbers if len(n) == 6 and len(set(n).difference(three)) == 1][0]
            numbers = [x for x in set(numbers).difference({nine})]
            zero = [n for n in numbers if len(set(n).difference(five)) == 2][0]
            numbers = [x for x in set(numbers).difference({zero})]
            six = numbers[0]

            nr = {
                ''.join(sorted(zero)): '0',
                ''.join(sorted(one)): '1',
                ''.join(sorted(two)): '2',
                ''.join(sorted(three)): '3',
                ''.join(sorted(four)): '4',
                ''.join(sorted(five)): '5',
                ''.join(sorted(six)): '6',
                ''.join(sorted(seven)): '7',
                ''.join(sorted(eight)): '8',
                ''.join(sorted(nine)): '9',
            }
            nr_value = int(''.join([nr[''.join(sorted(v))] for v in value]), 10)
            print(nr_value)
            count += nr_value

        print(count)

if __name__ == '__main__':
    main()
