def main():
    with open('input/21.txt', 'r') as fp:
        pos = [int(x.split(': ')[1]) for x in fp.readlines()]
        data = [0, 0]
        current_player = 0
        current_dies = []
        die_rolls = 0
        while True:
            for x in range(100):
                die_rolls += 1
                val = x+1
                current_dies.append(val)
                if len(current_dies) == 3:
                    pos[current_player] += sum(current_dies)
                    pos[current_player] = pos[current_player] % 10
                    if pos[current_player] == 0:
                        pos[current_player] += 10
                    data[current_player] += pos[current_player]
                    if data[current_player] >= 1000:
                        loosing_player = 1 if current_player == 0 else 0
                        print(data[loosing_player] * die_rolls)
                        return

                    current_player = 1 if current_player == 0 else 0
                    current_dies = []


if __name__ == '__main__':
    main()
