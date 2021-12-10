import logging

logger = logging.getLogger(__name__)


def _parse_input(input_file_path):
    logger.debug(f"Input file: {input_file_path}")
    with open(input_file_path, "r") as f:
        parsed_input = list(map(int, f.read().splitlines()[0].split(",")))
    return parsed_input


def _fuel(a, b):
    return abs(a - b)


def _triangular_sum(dist):
    return int((1 + dist) * dist / 2)


def _fuel_complicated(a, b):
    return _triangular_sum(abs(a - b))


def get_least_fuel(positions_list):
    needed_fuel = []
    for optimized_position in range(min(positions_list), max(positions_list) + 1):
        needed_fuel.append(
            sum([_fuel(pos, optimized_position) for pos in positions_list])
        )
    return min(needed_fuel)


def get_least_fuel_complicated(positions_list):
    needed_fuel = []
    for optimized_position in range(min(positions_list), max(positions_list) + 1):
        needed_fuel.append(
            sum([_fuel_complicated(pos, optimized_position) for pos in positions_list])
        )
    return min(needed_fuel)


def main():
    logging.basicConfig(
        format="%(asctime)s | %(levelname)-7s | %(message)s",
        datefmt="%H:%M:%S",
        level=logging.INFO,
    )
    horizontal_positions = _parse_input(
        "/home/eileen/workspace/adventofcode2021/day7/input.txt"
    )

    least_fuel = get_least_fuel(horizontal_positions)
    logger.info(f"Part 1 answer is '{least_fuel}'")  # 337488

    least_fuel_complicated = get_least_fuel_complicated(horizontal_positions)
    logger.info(f"Part 2 answer is '{least_fuel_complicated}'")  # 89647695


if __name__ == "__main__":
    main()
