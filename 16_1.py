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


def read_package(data):
    version = int(data[0:3], 2)
    type_id = int(data[3:6], 2)
    rest = data[6:]
    total_length = None
    nr_of_subpackages = None
    value = None
    if type_id == 4:
        pkgs = []
        while True:
            eop = int(rest[0], 2) == 0
            pkg = rest[1:5]
            pkgs.append(pkg)
            rest = rest[5:]
            if eop:
                break
        value = int("".join(pkgs), 2)
    else:
        length = int(rest[0], 2)
        rest = rest[1:]
        if length == 0:
            total_length = int(rest[:15], 2)
            rest = rest[15:]
        else:
            nr_of_subpackages = int(rest[:11], 2)
            rest = rest[11:]
    return rest, {
        'version': version,
        'type_id': type_id,
        'total_length': total_length,
        'nr_of_subpackages': nr_of_subpackages,
        'value': value,
    }


def main():
    with open('input/16.txt', 'r') as fp:
        hex_data = fp.readlines()[0].strip()
        bin_data = "".join([to_binary[d] for d in hex_data])
        rest = bin_data
        version_sum = 0
        while len(rest) > 8:
            rest, result = read_package(rest)
            version_sum += result['version']
        print(version_sum)


if __name__ == '__main__':
    main()
