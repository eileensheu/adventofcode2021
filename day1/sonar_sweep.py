
import logging

logger = logging.getLogger(__name__)


def rotate(list_of_numbers, n):
    return list_of_numbers[n:] + list_of_numbers[:n]


def count_next_larger_than_current(list_of_numbers):
    list_of_numbers_next = rotate(list_of_numbers, 1)
    next_larger_than_current = [True if next_element > current_element else False for current_element, next_element in zip(list_of_numbers[:-1], list_of_numbers_next[:-1])]
    return next_larger_than_current.count(True)


def list_of_sums_in_sliding_window(list_of_numbers, window_size):
    new_list = []
    for i in range(len(list_of_numbers) - window_size + 1):
        new_list.append(sum(map(int, list_of_numbers[i: i + window_size])))
    return new_list


def main():
    logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

    with open("/home/eileen/workspace/adventofcode2021/day1/input.txt", "r") as f:
        depth_list = [line.rstrip() for line in f.readlines()]
    logger.info(f"Part 1 answer is '{count_next_larger_than_current(depth_list)}'")  # 1722

    sliding_window_list = list_of_sums_in_sliding_window(depth_list, 3)
    logger.info(f"Part 2 answer is '{count_next_larger_than_current(sliding_window_list)}'")  # 1748


if __name__ == "__main__":
    main()
