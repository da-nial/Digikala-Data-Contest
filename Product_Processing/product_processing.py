try:
    n = int(input())  # number of terminals

    source_ids = []
    process_ids = []
    terminal_ids = []

    id_types = input().split()

    for i in range(len(id_types)):
        unit_type = int(id_types[i])
        if unit_type == 0:
            process_ids.append(i)
        elif unit_type == 1:
            source_ids.append(i)
        else:
            terminal_ids.append(i)

    units = [[0 for x in range(n)] for y in range(n)]

    e = int(input())  # number of straps

    for i in range(e):
        strap = input().split()

        start_pt = int(strap[0]) - 1
        end_pt = int(strap[1]) - 1
        capacity = int(strap[2])

        units[start_pt][end_pt] = capacity


    def column(matrix, i):
        return [row[i] for row in matrix]


    def argmax(column):
        index, max_val = -1, -1
        for i in range(len(column)):
            if column[i] > max_val:
                index, max_val = i, column[i]
        return index, max_val


    def find_next(current_unit):
        next_index, max_val = argmax(column(units, current_unit))
        return next_index, max_val


    def find_terminal():
        selected_terminal, next_index, max_val = -1, -1, -1

        for terminal_id in terminal_ids:
            indexi, max_vali = argmax(column(units, terminal_id))
            if max_vali > max_val:
                selected_terminal, next_index, max_val = terminal_id, indexi, max_vali

        return selected_terminal, next_index, max_val


    sum_weight = 0

    paths = []
    selected_terminal, current_index, min_weight = find_terminal()
    paths.append((selected_terminal, current_index))

    sum_weight = 0

    paths = []
    selected_terminal, current_index, min_weight = find_terminal()
    paths.append((selected_terminal, current_index))

    while min_weight > 0:
        while not (current_index in source_ids):
            next_index, max_val = find_next(current_index)
            paths.append((current_index, next_index))
            if max_val < min_weight:
                min_weight = max_val

            current_index = next_index
        if min_weight <= 0:
            break

        # print(paths)

        for path in paths:
            current_index, next_index = path
            units[next_index][current_index] = units[next_index][current_index] - min_weight

        sum_weight += min_weight

        paths = []
        selected_terminal, current_index, min_weight = find_terminal()
        paths.append((selected_terminal, current_index))
        if min_weight <= 0:
            break

    print(sum_weight)

except:
    print(0)
