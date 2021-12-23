states = {}
multiplier = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000,
}
correct_cave = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8,
}


def solve(state, energy=0):
    if state in states and states[state] <= energy:
        return None
    states[state] = energy
    possible_moves = []
    state_map = dict(state)
    for pos, val in state_map.items():
        if val is not None:
            steps = 0
            y = pos[1]
            x = pos[0]
            if y == 0:
                # must move down
                goal_x = correct_cave[val]
                if state_map[(goal_x, 1)] is None and \
                        state_map[(goal_x, 2)] in [None, val] and \
                        state_map[(goal_x, 3)] in [None, val] and \
                        state_map[(goal_x, 4)] in [None, val]:
                    i = 0
                    direction = -1 if goal_x - x < 0 else 1
                    while (x + i) != goal_x:
                        # Add all possible positions left and right.
                        i += (1 * direction)
                        steps += 1
                        if state_map[(x + i, 0)] is not None:
                            break
                    if (x + i) != goal_x:
                        continue
                    if state_map[(goal_x, 4)] is None:
                        possible_moves.append(((pos, None), ((x + i, 4), val), (steps + 4) * multiplier[val]))
                    elif state_map[(goal_x, 3)] is None:
                        possible_moves.append(((pos, None), ((x + i, 3), val), (steps + 3) * multiplier[val]))
                    elif state_map[(goal_x, 2)] is None:
                        possible_moves.append(((pos, None), ((x + i, 2), val), (steps + 2) * multiplier[val]))
                    else:
                        possible_moves.append(((pos, None), ((x + i, 1), val), (steps + 1) * multiplier[val]))
            else:
                # must move up
                if x == correct_cave[val]:
                    # Don't move if in correct cave unless other behind
                    if y == 4 or (
                            y == 3 and state_map[(x, 4)] == val
                    ) or (
                            y == 2 and state_map[(x, 4)] == val and state_map[(x, 3)] == val
                    ) or (
                            y == 1 and state_map[(x, 4)] == val and state_map[(x, 3)] == val and state_map[(x, 2)] == val
                    ):
                        continue
                if state_map[(pos[0], pos[1] - 1)] is None:
                    y -= 1
                    # can move up
                    steps += 1
                    while y != 0:
                        # can move up twice
                        y -= 1
                        steps += 1
                    left = True
                    right = True
                    i = 0
                    while left or right:
                        # Add all possible positions left and right.
                        i += 1
                        if left and x - i >= 0 and state_map[(x - i, 0)] is None:
                            if x - i not in correct_cave.values():
                                possible_moves.append(((pos, None), ((x - i, 0), val), (steps + i) * multiplier[val]))
                        else:
                            left = False
                        if right and x + i <= 10 and state_map[(x + i, 0)] is None:
                            if x + i not in correct_cave.values():
                                possible_moves.append(((pos, None), ((x + i, 0), val), (steps + i) * multiplier[val]))
                        else:
                            right = False

    current_low = None
    for move_from, move_to, move_energy in possible_moves:
        new_state = tuple(
            [((pos, data) if pos != move_from[0] else move_from) if pos != move_to[0] else move_to for pos, data in
             state])
        cave_state = "".join([s for pos, s in new_state[11:] if s])
        if len(cave_state) == 16 and cave_state == "ABCDABCDABCDABCD":
            return energy + move_energy
        else:
            res = solve(new_state, energy + move_energy)
            if res is not None:
                if current_low is None:
                    current_low = res
                else:
                    current_low = min(current_low, res)
    return current_low


def main():
    with open('input/23.txt', 'r') as fp:
        data = [[y for y in x.strip('\n') if y not in [' ', '#']] for x in fp.readlines()[2:4]]
        data = [data[0], 'DCBA', 'DBAC', data[1]]
        state = [
            ((0, 0), None),
            ((1, 0), None),
            ((2, 0), None),
            ((3, 0), None),
            ((4, 0), None),
            ((5, 0), None),
            ((6, 0), None),
            ((7, 0), None),
            ((8, 0), None),
            ((9, 0), None),
            ((10, 0), None),
        ]
        y = 0
        for row in data:
            y += 1
            x = 0
            for a in row:
                x += 2
                state.append(((x, y), a))
        state = tuple(state)
        res = solve(state)
        print(res)


if __name__ == '__main__':
    main()
