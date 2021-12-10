def main():
    with open('input/10.txt', 'r') as fp:
        data = [list(x.strip()) for x in fp.readlines()]
        matching = {
            ')': '(',
            ']': '[',
            '}': '{',
            '>': '<',
        }
        value_lookup = {
            '(': 1,
            '[': 2,
            '{': 3,
            '<': 4,
        }
        scores = []
        for row in data:
            open_blocks = []
            discard = False
            for character in row:
                if character in "([{<":
                    open_blocks.append(character)
                else:
                    mc = matching[character]
                    expected = open_blocks.pop(-1)
                    if mc != expected:
                        discard = True
            if not discard:
                line_sum = 0
                for character in reversed(open_blocks):
                    line_sum *= 5
                    line_sum += value_lookup[character]
                scores.append(line_sum)

        print(sorted(scores)[int((len(scores)-1)/2)])


if __name__ == '__main__':
    main()
