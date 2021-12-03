def get_one_count(data):
    count = []
    for d in data:
        for i, c in enumerate(d):
            if len(count) <= i:
                count.append(0)
            if c == '1':
                count[i] += 1
    return count


def main():
    with open('input_03.txt', 'r') as fp:
        original_data = [x.strip() for x in fp.readlines()]
        data = [*original_data]
        word_length = len(data[0])
        ogr = 0
        csr = 0
        for i in range(word_length):
            count = get_one_count(data)
            if count[i] >= len(data)/2:
                data = [d for d in data if d[i] == '1']
            else:
                data = [d for d in data if d[i] == '0']
            if len(data) == 1:
                ogr = int(data[0], 2)
                break
        data = [*original_data]
        for i in range(word_length):
            count = get_one_count(data)
            if count[i] >= len(data)/2:
                data = [d for d in data if d[i] == '0']
            else:
                data = [d for d in data if d[i] == '1']
            if len(data) == 1:
                csr = int(data[0], 2)
                break

        print(ogr * csr)


if __name__ == '__main__':
    main()
