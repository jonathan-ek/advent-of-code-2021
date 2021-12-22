def parse(state, cuboid):
    return state, [[int(y) for y in (x.split('=')[1]).split('..')] for x in cuboid.split(',')]


def main():
    with open('input/22.txt', 'r') as fp:
        lines = fp.readlines()
        data = [parse(*x.split(' ')) for x in lines]
        active = set()
        for state, pos in data:
            if max([pos[0][1], pos[1][1], pos[2][1]]) > 50:
                continue
            if min([pos[0][0], pos[1][0], pos[2][0]]) < -50:
                continue
            for x in range(pos[0][0], pos[0][1]+1):
                for y in range(pos[1][0], pos[1][1]+1):
                    for z in range(pos[2][0], pos[2][1]+1):
                        if state == 'on':
                            active.add((x, y, z))
                        else:
                            try:
                                active.remove((x, y, z))
                            except KeyError:
                                pass
        print(len(active))


if __name__ == '__main__':
    main()
