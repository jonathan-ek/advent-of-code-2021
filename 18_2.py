import json
import math


def post_order(pair, order):
    if type(pair) == int:
        return
    post_order(pair.left, order)
    if pair.left_is_int:
        order.append(pair)
    post_order(pair.right, order)
    if not pair.left_is_int:
        order.append(pair)


class PairIterator:
    def __init__(self, pair):
        self.current = pair
        self.order = []
        post_order(pair, self.order)
        self.index = 0

    def __next__(self):
        self.index += 1
        try:
            return self.order[self.index-1]
        except IndexError:
            raise StopIteration()


class Pair:
    def __init__(self, left=None, right=None, parent=None):
        self.left = left
        self.right = right
        self.parent = parent

    @classmethod
    def parse(cls, data, parent=None):
        pair = cls(parent=parent)
        if type(data[0]) == int:
            pair.left = data[0]
        else:
            pair.left = cls.parse(data[0], parent=pair)
        if type(data[1]) == int:
            pair.right = data[1]
        else:
            pair.right = cls.parse(data[1], parent=pair)
        return pair

    @property
    def left_is_int(self):
        return type(self.left) == int

    @property
    def right_is_int(self):
        return type(self.right) == int

    @property
    def depth(self):
        i = 0
        tmp = self
        while True:
            if tmp.parent is None:
                break
            tmp = tmp.parent
            i += 1
        return i

    @property
    def magnitude(self):
        return (3 * (self.left if self.left_is_int else self.left.magnitude)) + (2 * (self.right if self.right_is_int else self.right.magnitude))

    def find_left(self):
        if self.parent is None:
            return None, None
        if self.parent.right == self:
            if self.parent.left_is_int:
                return self.parent, 'l'
            else:
                tmp = self.parent.left
                while not tmp.right_is_int:
                    tmp = tmp.right
                return tmp, 'r'
        else:
            return self.parent.find_left()

    def find_right(self):
        if self.parent is None:
            return None, None
        if self.parent.left == self:
            if self.parent.right_is_int:
                return self.parent, 'r'
            else:
                tmp = self.parent.right
                while not tmp.left_is_int:
                    tmp = tmp.left
                return tmp, 'l'
        else:
            return self.parent.find_right()

    def explode(self):
        left, left_dir = self.find_left()
        right, right_dir = self.find_right()

        if left:
            if left_dir == 'r':
                left.right += self.left
            else:
                left.left += self.left
        if right:
            if right_dir == 'r':
                right.right += self.right
            else:
                right.left += self.right
        if self.parent.left == self:
            self.parent.left = 0
        if self.parent.right == self:
            self.parent.right = 0

    def split_left(self):
        self.left = Pair(math.floor(self.left/2), math.ceil(self.left/2), self)

    def split_right(self):
        self.right = Pair(math.floor(self.right/2), math.ceil(self.right/2), self)

    def __add__(self, other):
        new_node = Pair(self, other)
        self.parent = new_node
        other.parent = new_node
        return new_node

    def __iter__(self):
        return PairIterator(self)

    def __str__(self):
        return f"[{str(self.left)},{str(self.right)}]"


def simplify(pair):
    has_change = True
    allow_split = False
    while has_change:
        has_change = False
        for c in pair:
            if c.depth == 4:
                c.explode()
                has_change = True
                allow_split = False
                break
            elif allow_split and c.left_is_int and c.left > 9:
                c.split_left()
                has_change = True
                allow_split = False
                break
            elif allow_split and c.right_is_int and c.right > 9:
                c.split_right()
                has_change = True
                allow_split = False
                break

        if not has_change and not allow_split:
            has_change = True
            allow_split = True


def main():
    with open('input/18.txt', 'r') as fp:
        data = [x.strip() for x in fp.readlines()]
        max_mag = 0
        for i, e in enumerate(data):
            for j, f in enumerate(data):
                if i == j:
                    continue
                current = Pair.parse(json.loads(e)) + Pair.parse(json.loads(f))
                simplify(current)
                max_mag = max([max_mag, current.magnitude])
        print(max_mag)


if __name__ == '__main__':
    main()
