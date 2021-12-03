def main():
    with open('input_03.txt', 'r') as fp:
        data = [x.strip() for x in fp.readlines()]
        count = []
        for d in data:
            for i, c in enumerate(d):
                if len(count) <= i:
                    count.append(0)
                if c == '1':
                    count[i] += 1
        gama_rate_list = []
        epsilon_rate_list = []
        for c in count:
            if c > len(data)/2:
                gama_rate_list.append('1')
                epsilon_rate_list.append('0')
            else:
                gama_rate_list.append('0')
                epsilon_rate_list.append('1')
        gama_rate = int(''.join(gama_rate_list), 2)
        epsilon_rate = int(''.join(epsilon_rate_list), 2)
        print(gama_rate * epsilon_rate)


if __name__ == '__main__':
    main()
