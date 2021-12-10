import logging

logger = logging.getLogger(__name__)


def _parse_input(input_file_path):
    logger.debug(f"Input file: {input_file_path}")
    with open(input_file_path, "r") as f:
        _input_content = f.read().splitlines()
    ten_digits = []
    four_digits_output = []
    for a_line in _input_content:
        ten_digits.append(a_line.split("|")[0].split())
        four_digits_output.append(a_line.split("|")[1].split())
    return ten_digits, four_digits_output


def _flatten(t):
    return [item for sublist in t for item in sublist]


def count_unique_number_of_segments_instances_of_digits(unique_signal_patterns_list):
    return len(
        list(
            filter(
                lambda x: (len(x) == 2)
                or (len(x) == 4)
                or (len(x) == 3)
                or (len(x) == 7),
                _flatten(unique_signal_patterns_list),
            )
        )
    )


unique_signal_patterns_to_digits_dict = {
    "cefabd": "9",
    "acedgfb": "8",
    "dab": "7",
    "cdfgeb": "6",
    "cdfbe": "5",
    "eafb": "4",
    "fbcad": "3",
    "gcdfa": "2",
    "ab": "1",
    "cagedb": "0",
}


def _map_unique_signal_patterns_to_digits(x):
    for k, v in unique_signal_patterns_to_digits_dict.items():
        if sorted(x) == sorted(k):
            return v
    return "0"
    # raise Exception(f"'{x}' is not known.")


def _map_strlist_to_int(str_list):
    return int("".join(str_list))


def generate_unique_signal_patterns_to_digits_dict(unique_signal_patterns_list):
    # TODO: implementation
    global unique_signal_patterns_to_digits_dict
    unique_signal_patterns_to_digits_dict = "TODO"


def decode_and_sum(unique_signal_patterns_list):
    digits_list = []
    for output in unique_signal_patterns_list:
        digits_list.append(
            _map_strlist_to_int(
                list(map(_map_unique_signal_patterns_to_digits, output))
            )
        )
    return sum(digits_list)


def main():
    logging.basicConfig(
        format="%(asctime)s | %(levelname)-7s | %(message)s",
        datefmt="%H:%M:%S",
        level=logging.DEBUG,
    )
    ten_digits, four_digits_output = _parse_input(
        "/home/eileen/workspace/adventofcode2021/day8/example_input.txt"
    )

    instances_of_digits = count_unique_number_of_segments_instances_of_digits(
        four_digits_output
    )
    logger.info(f"Part 1 answer is '{instances_of_digits}'")  # 514

    generate_unique_signal_patterns_to_digits_dict(ten_digits)
    sum_of_outputs = decode_and_sum(four_digits_output)
    logger.info(f"Part 2 answer is '{sum_of_outputs}'")  #


if __name__ == "__main__":
    main()
