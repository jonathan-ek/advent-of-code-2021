def main():
    with open('input_06.txt', 'r') as fp:
        state = [int(x) for x in fp.readlines()[0].split(',')]
        print(state)
        for r in range(80):
            new_state = []
            for d in state:
                if d == 0:
                    new_state.append(6)
                    new_state.append(8)
                else:
                    new_state.append(d-1)
            state = new_state
        print(len(state))


if __name__ == '__main__':
    main()
