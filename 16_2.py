to_binary = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}


def product(args):
    prod = 1
    for p in args:
        prod *= p
    return prod


def gt(args):
    assert len(args) == 2, len(args)
    return 1 if args[0] > args[1] else 0


def lt(args):
    assert len(args) == 2, len(args)
    return 1 if args[0] < args[1] else 0


def eq(args):
    assert len(args) == 2, len(args)
    return 1 if args[0] == args[1] else 0


function = {
    0: sum,
    1: product,
    2: min,
    3: max,
    5: gt,
    6: lt,
    7: eq,
}


def read_package(data, soft_max=None):
    if soft_max == 0:
        return data, None
    version = int(data[0:3], 2)
    type_id = int(data[3:6], 2)
    rest = data[6:]
    c = 6
    total_length = None
    nr_of_subpackages = None
    value = None
    if type_id == 4:
        pkgs = []
        while True:
            if soft_max is not None and c >= soft_max:
                break
            eop = int(rest[0], 2) == 0
            pkg = rest[1:5]
            pkgs.append(pkg)
            rest = rest[5:]
            c += 5
            if eop:
                break
        value = int("".join(pkgs), 2)
    else:
        length = int(rest[0], 2)
        rest = rest[1:]
        c += 1
        if length == 0:
            total_length = int(rest[:15], 2)
            rest = rest[15:]
            c += 15
        else:
            nr_of_subpackages = int(rest[:11], 2)
            rest = rest[11:]
            c += 11
    return rest, Instruction({
        'length': c,
        'version': version,
        'type_id': type_id,
        'total_length': total_length,
        'nr_of_subpackages': nr_of_subpackages,
        'value': value,
        'rest': len(rest),
    })


class Instruction:
    def __init__(self, data):
        self.ins_length = data['length']
        self.total_length = data['total_length']
        self.nr_of_subpackages = data['nr_of_subpackages']
        self.rest = data['rest']
        self.version = data['version']
        self.type_id = data['type_id']
        self.value = data['value']
        self.subs = []

    def add_sub(self, ins):
        self.subs.append(ins)

    @property
    def length(self):
        return sum([x.length + x.ins_length for x in self.subs])

    def calculate(self):
        if self.type_id != 4:
            for sub in self.subs:
                if sub.value is None:
                    sub.calculate()
            self.value = function[self.type_id]([sub.value for sub in self.subs])


def main():
    with open('input/16.txt', 'r') as fp:
        hex_data = fp.readlines()[0].strip()
        bin_data = "".join([to_binary[d] for d in hex_data])
        rest = bin_data
        queue = []
        first_instruction = None
        current = None
        while len(rest) > 8:
            if len(queue):
                current = queue[-1]
            rest, instruction = read_package(rest, (
                        current.total_length - current.length) if current and current.total_length else None)
            if len(queue) == 0:
                first_instruction = instruction
                queue = [first_instruction]
                continue
            if instruction is not None:
                current.add_sub(instruction)

            if (
                    (current.total_length is not None and (current.total_length - current.length) == 0) or
                    (current.nr_of_subpackages is not None and len(current.subs) == current.nr_of_subpackages)
            ):
                queue.pop(-1)
            if instruction is not None and (
                    instruction.total_length is not None or instruction.nr_of_subpackages is not None):
                queue.append(instruction)
            current = queue[-1]

        first_instruction.calculate()
        print(first_instruction.value)


if __name__ == '__main__':
    main()
