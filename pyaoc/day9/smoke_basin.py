
from numpy import prod
from pyaoc.utils.map_utils import Coord, get_valid_neighbor_coords
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
        neighbormap.append([[]] * len(row))
        for col_idx in range(len(row)):
            valid_neighbor_coords = get_valid_neighbor_coords(
                row_idx, col_idx, len(heightmap), len(row)
            )
            neighbormap[row_idx][col_idx] = [
                heightmap[coord.r][coord.c] for coord in valid_neighbor_coords
            ]
    return neighbormap


def find_local_min_and_its_coordinates(heightmap, neighbormap):
    local_mins = []
    local_mins_coord = []
    for row_idx, (row_heightmap, row_neighbors) in enumerate(
        zip(heightmap, neighbormap)
    ):
        for col_idx, (ele_heightmap, ele_neighbors) in enumerate(
            zip(row_heightmap, row_neighbors)
        ):
            if _is_local_min(ele_heightmap, ele_neighbors):
                local_mins.append(ele_heightmap)
                local_mins_coord.append(Coord(r=row_idx, c=col_idx))
    return local_mins, local_mins_coord


def compute_risk_level_sum_from_local_mins(local_mins_list):
    return sum(local_mins_list) + len(local_mins_list)


def find_basins_sizes(local_mins_coord, heightmap):
    len_row = len(heightmap)
    len_col = len(heightmap[0])
    basins_sizes = []
    for local_min in local_mins_coord:
        basin_size = 0
        seed = [local_min]
        processed = []
        while len(seed) > 0:
            current_coord = seed[0]

            if (
                current_coord not in processed
                and heightmap[current_coord.r][current_coord.c] < 9
            ):

                valid_neighbor_coords = get_valid_neighbor_coords(
                    current_coord.r, current_coord.c, len_row, len_col
                )
                seed = seed + valid_neighbor_coords

                processed.append(seed[0])
                del seed[0]
                basin_size += 1

            elif (
                current_coord not in processed
                and heightmap[current_coord.r][current_coord.c] == 9
            ):

                processed.append(seed[0])
                del seed[0]

            elif current_coord in processed:
                processed.append(seed[0])
                del seed[0]
            else:
                raise Exception("Unexpected situation.")
        basins_sizes.append(basin_size)
    return basins_sizes


def main():
    logging.basicConfig(
        format="%(asctime)s | %(levelname)-7s | %(message)s",
        datefmt="%H:%M:%S",
        level=logging.INFO,
    )

    heightmap = _parse_input("/home/eileen/workspace/adventofcode2021/pyaoc/day9/input.txt")

    neighbormap = generate_neighbormap(heightmap)
    local_mins, local_mins_coord = find_local_min_and_its_coordinates(
        heightmap, neighbormap
    )
    risk_level_sum = compute_risk_level_sum_from_local_mins(local_mins)
    logger.info(f"Part 1 answer is '{risk_level_sum}'")  # 550

    basins_sizes = find_basins_sizes(local_mins_coord, heightmap)
    sorted_basins_sizes = sorted(basins_sizes)
    logger.debug(f"sorted_basins_sizes_descending: {sorted_basins_sizes[-3:]}")
    logger.info(f"Part 2 answer is '{prod(sorted_basins_sizes[-3:])}'")  # 1100682


if __name__ == "__main__":
    main()
