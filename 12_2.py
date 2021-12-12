class Node:
    def __init__(self, id):
        self.id = id
        self.paths = []
        self.small = False
        if id.lower() == id:
            self.small = True
        
    def add_path(self, node):
        self.paths.append(node)
        
        
def get_paths(history, current, prevent_dual=False):
    paths = []
    for n in current.paths:
        used_dual = prevent_dual
        if n in history and n.small:
            used_dual = True
            if prevent_dual or n.id == 'start':
                continue
        if n.id == 'end':
            paths.append([*history, current, n])
            continue
        paths += get_paths([*history, current], n, used_dual)
    return paths

def main():
    with open('input/12.txt', 'r') as fp:
        data = [x.strip().split('-') for x in fp.readlines()]
        lo = dict()
        nodes = set([d for x in data for d in x])
        for node in nodes:
            lo[node] = Node(node)
        for path in data:
            a, b = path
            n0 = lo[a]
            n1= lo[b]
            n0.add_path(n1)
            n1.add_path(n0)
            
        start = lo['start']
        end = lo['end']
        paths = []
        for s in start.paths:
            paths.append(get_paths([start], s))
        paths = [p for ps in paths for p in ps]
        print(len(paths))


if __name__ == '__main__':
    main()