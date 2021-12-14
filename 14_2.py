import collections


def main():
    with open('input/14.txt', 'r') as fp:
        lines = fp.readlines()
        data = dict([x.strip().split(' -> ') for x in lines[2:]])
        code = lines[0].strip()
        code_pairs = dict(collections.Counter([(code[i], code[i+1]) for i in range(len(code) - 1)]))
        for _ in range(40):
            new_code = dict()
            for pair, count in code_pairs.items():
                tmp = f"{pair[0]}{pair[1]}"
                if tmp in data:
                    new_char = data[tmp]
                    if (pair[0], new_char) not in new_code:
                        new_code[(pair[0], new_char)] = 0
                    if (new_char, pair[1]) not in new_code:
                        new_code[(new_char, pair[1])] = 0
                    new_code[(pair[0], new_char)] += count
                    new_code[(new_char, pair[1])] += count
            code_pairs = new_code
        char_count = dict()
        for pair, count in code_pairs.items():
            if pair[0] not in char_count:
                char_count[pair[0]] = 0
            char_count[pair[0]] += count
        char_count[code[-1]] += 1
        values = sorted(char_count.values(), reverse=True)
        print(values[0] - values[-1])


if __name__ == '__main__':
    main()
