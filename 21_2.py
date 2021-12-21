# 3  111
# 4  112 121 211
# 5  113 131 311 122 212 221
# 6  123 132 213 231 222 312 321
# 7  133 232 223 322 331 313
# 8  233 323 332
# 9  333
outcomes = {
    3: 1,
    4: 3,
    5: 6,
    6: 7,
    7: 6,
    8: 3,
    9: 1,
}


def game(pos, score, wins, multiplier, player):
    for val, count in outcomes.items():
        new_pos = [*pos]
        new_score = [*score]
        new_pos[player] += val
        new_pos[player] = new_pos[player] % 10
        if new_pos[player] == 0:
            new_pos[player] += 10
        new_score[player] += new_pos[player]
        if new_score[player] >= 21:
            wins[player] += multiplier * count
        else:
            game(new_pos, new_score, wins, multiplier * count, 1 if player == 0 else 0)


def main():
    with open('input/21.txt', 'r') as fp:
        pos = [int(x.split(': ')[1]) for x in fp.readlines()]
        wins = [0, 0]
        game(pos, [0, 0], wins, multiplier=1, player=0)
        print(wins)


if __name__ == '__main__':
    main()
