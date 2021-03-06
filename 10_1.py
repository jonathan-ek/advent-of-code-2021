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
            '(': 3,
            '[': 57,
            '{': 1197,
            '<': 25137,
        }
        sum = 0
        for row in data:
            open_blocks = []
            for character in row:
                if character in "([{<":
                    open_blocks.append(character)
                else:
                    mc = matching[character]
                    expected = open_blocks.pop(-1)
                    if mc != expected:
                        sum += value_lookup[mc]
                        continue
        print(sum)

if __name__ == '__main__':
    main()
