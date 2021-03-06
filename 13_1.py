def main():
    with open('input/13.txt', 'r') as fp:
        lines = fp.readlines()
        dots = [tuple([int(y) for y in x.strip().split(',')]) for x in lines if x.strip() != '' and 'fold along' not in x]
        folds = [[y for y in x[11:].strip().split('=')] for x in lines if 'fold along' in x]
        folds = [(x[0], int(x[1])) for x in folds]
        for axis, index in folds:
            if axis == 'y':
                dots = list(set([(x[0], x[1] if x[1] < index else 2*index - x[1]) for x in dots]))
            if axis == 'x':
                dots = list(set([(x[0] if x[0] < index else 2*index - x[0], x[1]) for x in dots]))
                break
        print(len(dots))



if __name__ == '__main__':
    main()
