def main():
    with open('input/20.txt', 'r') as fp:
        lines = fp.readlines()
        algo = [1 if x == "#" else 0 for x in lines[0].strip()]
        data = [[1 if x == "#" else 0 for x in '..' + line.strip() + '..'] for line in lines[2:]]
        data.insert(0, [0 for _ in range(len(data[0]))])
        data.insert(0, [0 for _ in range(len(data[0]))])
        data.append([0 for _ in range(len(data[0]))])
        data.append([0 for _ in range(len(data[0]))])
        outside = 0
        for i in range(50):
            outside = algo[0] if outside == 0 else algo[len(algo) - 1]
            output = [[outside for _ in range(len(data[0]) + 2)], [outside for _ in range(len(data[0]) + 2)]]
            for y in range(1, len(data) - 1):
                line = [outside, outside]
                for x in range(1, len(data[y]) - 1):
                    number = int(
                        f"{data[y - 1][x - 1]}{data[y - 1][x]}{data[y - 1][x + 1]}"
                        f"{data[y][x - 1]}{data[y][x]}{data[y][x + 1]}"
                        f"{data[y + 1][x - 1]}{data[y + 1][x]}{data[y + 1][x + 1]}",
                        2
                    )
                    line.append(algo[number])
                line.append(outside)
                line.append(outside)
                output.append(line)
            output.append([outside for _ in range(len(data[0]) + 2)])
            output.append([outside for _ in range(len(data[0]) + 2)])
            data = output
        print(sum([i for j in data for i in j]))


if __name__ == '__main__':
    main()
