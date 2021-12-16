import logging

logger = logging.getLogger(__name__)


def _parse_input(input_file_path):
    logger.debug(f"Input file: {input_file_path}")
    with open(input_file_path, "r") as f:
        parsed_input = [line.rstrip() for line in f.readlines()]
    return parsed_input


def rotate(list_of_numbers, n):
    return list_of_numbers[n:] + list_of_numbers[:n]


def count_next_larger_than_current(list_of_numbers):
    list_of_numbers_next = rotate(list_of_numbers, 1)
    next_larger_than_current = [
        True if next_element > current_element else False
        for current_element, next_element in zip(
            list_of_numbers[:-1], list_of_numbers_next[:-1]
        )
    ]
    return next_larger_than_current.count(True)


def list_of_sums_in_sliding_window(list_of_numbers, window_size):
    new_list = []
    for i in range(len(list_of_numbers) - window_size + 1):
        new_list.append(sum(map(int, list_of_numbers[i : i + window_size])))
    return new_list


def main():
    logging.basicConfig(
        format="%(asctime)s | %(levelname)-7s | %(message)s",
        datefmt="%H:%M:%S",
        level=logging.INFO,
    )

    depth_list = _parse_input("/home/eileen/workspace/adventofcode2021/pyaoc/day1/input.txt")

    logger.info(
        f"Part 1 answer is '{count_next_larger_than_current(depth_list)}'"
    )  # 1722

    sliding_window_list = list_of_sums_in_sliding_window(depth_list, 3)
    logger.info(
        f"Part 2 answer is '{count_next_larger_than_current(sliding_window_list)}'"
    )  # 1748


if __name__ == "__main__":
    main()
