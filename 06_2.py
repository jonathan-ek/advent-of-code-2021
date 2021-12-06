def main():
    with open('input_06.txt', 'r') as fp:
        state = [int(x) for x in fp.readlines()[0].split(',')]
        pop = {
            0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0,
        }
        for f in state:
            pop[f] += 1

        for r in range(256):
            new_pop = dict()
            new_pop[8] = pop[0]
            new_pop[7] = pop[8]
            new_pop[6] = pop[7] + pop[0]
            new_pop[5] = pop[6]
            new_pop[4] = pop[5]
            new_pop[3] = pop[4]
            new_pop[2] = pop[3]
            new_pop[1] = pop[2]
            new_pop[0] = pop[1]
            pop = new_pop
        print(sum(pop.values()))


if __name__ == '__main__':
    main()
