import collections


def main():
    with open('input/14.txt', 'r') as fp:
        lines = fp.readlines()
        data = dict([x.strip().split(' -> ') for x in lines[2:]])
        code = lines[0].strip()
        for _ in range(10):
            new_code = []
            for i, c in enumerate(code):
                new_code += c
                if len(code) > i + 1:
                    tmp = f"{c}{code[i+1]}"
                    if tmp in data:
                        new_code += data[tmp]
            code = new_code
        values = sorted(collections.Counter(code).values(), reverse=True)
        print(values[0] - values[-1])


if __name__ == '__main__':
    main()
