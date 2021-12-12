import logging

logger = logging.getLogger(__name__)


def _parse_input(input_file_path):
    logger.debug(f"Input file: {input_file_path}")
    with open(input_file_path, "r") as f:
        parsed_input = f.read().splitlines()
    return [[int(ele) for ele in line] for line in parsed_input]


def _is_local_min(x, neighbors_list):
    if all(x < neighbor for neighbor in neighbors_list):
        return True
    else:
        False


def generate_neighbormap(heightmap):
    neighbormap = []
    for row_idx, row in enumerate(heightmap):
        neighbormap.append([[]]*len(row))
        for col_idx in range(len(row)):
            # First row
            if row_idx == 0:
                # first col
                if col_idx == 0:
                    neighbor = [
                        heightmap[row_idx][col_idx+1], # right
                        heightmap[row_idx+1][col_idx], # below
                    ]
                # last col
                elif col_idx == len(row)-1:
                    neighbor = [
                        heightmap[row_idx][col_idx-1], # left
                        heightmap[row_idx+1][col_idx], # below
                    ]
                else:
                    neighbor = [
                        heightmap[row_idx][col_idx+1], # right
                        heightmap[row_idx][col_idx-1], # left
                        heightmap[row_idx+1][col_idx], # below
                    ]
            # Last row
            elif row_idx == len(heightmap)-1:
                # first col
                if col_idx == 0:
                    neighbor = [
                        heightmap[row_idx][col_idx+1], # right
                        heightmap[row_idx-1][col_idx], # above
                    ]
                # last col
                elif col_idx == len(row)-1:
                    neighbor = [
                        heightmap[row_idx][col_idx-1], # left
                        heightmap[row_idx-1][col_idx], # above
                    ]
                else:
                    neighbor = [
                        heightmap[row_idx][col_idx+1], # right
                        heightmap[row_idx][col_idx-1], # left
                        heightmap[row_idx-1][col_idx], # above
                    ]
            else:
                # first col
                if col_idx == 0:
                    neighbor = [
                        heightmap[row_idx][col_idx+1], # right
                        heightmap[row_idx-1][col_idx], # above
                        heightmap[row_idx+1][col_idx], # below
                    ]
                # last col
                elif col_idx == len(row)-1:
                    neighbor = [
                        heightmap[row_idx][col_idx-1], # left
                        heightmap[row_idx-1][col_idx], # above
                        heightmap[row_idx+1][col_idx], # below
                    ]
                else:
                    neighbor = [
                        heightmap[row_idx][col_idx+1], # right
                        heightmap[row_idx][col_idx-1], # left
                        heightmap[row_idx-1][col_idx], # above
                        heightmap[row_idx+1][col_idx], # below
                    ]
            neighbormap[row_idx][col_idx] = neighbor
    return neighbormap


def find_local_min_and_its_coordinates(heightmap, neighbormap):
    local_mins = []
    local_mins_coord = []
    for row_idx, (row_heightmap, row_neighbors) in enumerate(zip(heightmap, neighbormap)):
        for col_idx, (ele_heightmap, ele_neighbors) in enumerate(zip(row_heightmap, row_neighbors)):
            if _is_local_min(ele_heightmap, ele_neighbors):
                    local_mins.append(ele_heightmap)
                    local_mins_coord.append([row_idx, col_idx])
    return local_mins, local_mins_coord


def compute_risk_level_sum_from_local_mins(local_mins_list):
    return sum(local_mins_list) + len(local_mins_list)


def main():
    logging.basicConfig(
        format="%(asctime)s | %(levelname)-7s | %(message)s",
        datefmt="%H:%M:%S",
        level=logging.DEBUG,
    )

    heightmap = _parse_input(
        "/home/eileen/workspace/adventofcode2021/day9/input.txt"
    )

    neighbormap = generate_neighbormap(heightmap)
    local_mins, local_mins_coord = find_local_min_and_its_coordinates(heightmap, neighbormap)
    risk_level_sum = compute_risk_level_sum_from_local_mins(local_mins)
    logger.info(f"Part 1 answer is '{risk_level_sum}'")  # 550


    # logger.info(f"Part 2 answer is '{}'")  #


if __name__ == "__main__":
    main()
