class Plan:
    def __init__(self, rows):
        self.rows = [[int(y) for y in x.strip().replace('  ', ' ').split(' ')] for x in rows]
        self.columns = [[self.rows[x][y] for x in range(5)] for y in range(5)]

    def has_bingo(self, numbers):
        for row in self.rows:
            if all(nr in numbers for nr in row):
                return True
        for col in self.columns:
            if all(nr in numbers for nr in col):
                return True
        return False


def main():
    with open('input_04.txt', 'r') as fp:
        lines = fp.readlines()
        numbers = [int(x) for x in lines[0].split(',')]
        lines = lines[1:]
        plans = []
        for p in range(int(len(lines)/6)):
            plans.append(Plan(lines[(p*6) + 1:(p+1)*6]))

        for n in range(5, len(numbers)+1):
            for p in plans:
                if p.has_bingo(numbers[:n]):
                    plan_numbers = [p for row in p.rows for p in row]
                    unmarked_plan_numbers = [p for p in plan_numbers if p not in numbers[:n]]
                    print(sum(unmarked_plan_numbers) * numbers[n-1])
                    return



if __name__ == '__main__':
    main()
