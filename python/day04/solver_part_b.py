from copy import deepcopy

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]


def printf(floor_map):
    for row in floor_map:
        print(row)


def mark_row_index_with_x(map_row, y, character="X"):
    if y == 0:
        return character + map_row[y + 1 :]
    elif y == len(map_row) - 1:
        return map_row[:y] + character
    else:
        return map_row[:y] + character + map_row[y + 1 :]


def get_neighbour_rolls(x: int, y: int, rows: int, columns: int, floor_map: list[str]):
    total_roll_count = 0

    for dx, dy in dirs:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < rows and 0 <= ny < columns:
            if floor_map[nx][ny] in ("X", "@"):
                total_roll_count += 1

    return total_roll_count


def get_total_removals(floor_map):
    rows = len(floor_map)
    columns = len(floor_map[0])

    total_rolls_with_max = 0
    for row in range(rows):
        for column in range(columns):
            if floor_map[row][column] == ".":
                continue
            total_neighrs = get_neighbour_rolls(row, column, rows, columns, floor_map)
            if total_neighrs < 4:
                total_rolls_with_max += 1
                # Update @ with X
                out = mark_row_index_with_x(floor_map[row][:], column)
                floor_map[row] = out
    print("\n---\n")
    print(f"Total removals: {total_rolls_with_max=}")
    return total_rolls_with_max, floor_map


def cleanup_floor(floor_map):
    return "---".join(floor_map).replace("X", ".").split("---")


if __name__ == "__main__":
    with open("input.txt") as input_file:
        floor_map = input_file.read().split()

    floor_copy = deepcopy(floor_map)
    printf(floor_map)

    total_removals_per_iter = []

    total_removed, floor_map = get_total_removals(floor_map)
    printf(floor_map)
    cleaned_floor = cleanup_floor(floor_map)
    total_removals_per_iter.append(total_removed)

    while cleaned_floor != floor_map:
        print(f"Iteration: {len(total_removals_per_iter)}; {total_removals_per_iter=}")
        total_removed, floor_map = get_total_removals(cleaned_floor)
        printf(floor_map)
        cleaned_floor = cleanup_floor(floor_map)
        total_removals_per_iter.append(total_removed)

    print(f"{sum(total_removals_per_iter)=}")
