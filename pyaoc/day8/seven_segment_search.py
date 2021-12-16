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


def generate_unique_signal_patterns_to_digits_dict(unique_signal_patterns_list):
    unique_signal_patterns_to_digits_dict = {}
    len5_patterns = []
    len6_patterns = []
    for unique_signal_pattern in unique_signal_patterns_list:
        logger.debug(unique_signal_pattern)
        length = len(unique_signal_pattern)
        if length == 2:
            unique_signal_patterns_to_digits_dict["1"] = unique_signal_pattern
        elif length == 3:
            unique_signal_patterns_to_digits_dict["7"] = unique_signal_pattern
        elif length == 4:
            unique_signal_patterns_to_digits_dict["4"] = unique_signal_pattern
        elif length == 7:
            unique_signal_patterns_to_digits_dict["8"] = unique_signal_pattern
        elif length == 5:
            len5_patterns.append(unique_signal_pattern)
        elif length == 6:
            len6_patterns.append(unique_signal_pattern)
        else:
            raise Exception(
                f"No known unique signal pattern would have length '{length}'."
            )

    logger.debug(unique_signal_patterns_to_digits_dict)

    one_compositions = [x for x in unique_signal_patterns_to_digits_dict["1"]]
    four_compositions = [x for x in unique_signal_patterns_to_digits_dict["4"]]

    while len6_patterns:
        for idx, len6_pattern in enumerate(len6_patterns):
            if not all(one_ele in len6_pattern for one_ele in one_compositions):
                unique_signal_patterns_to_digits_dict["6"] = len6_patterns.pop(idx)
            elif all(four_ele in len6_pattern for four_ele in four_compositions):
                unique_signal_patterns_to_digits_dict["9"] = len6_patterns.pop(idx)
            elif len(len6_patterns) == 1:
                unique_signal_patterns_to_digits_dict["0"] = len6_patterns.pop(idx)

    nine_compositions = [x for x in unique_signal_patterns_to_digits_dict["9"]]

    while len5_patterns:
        for idx, len5_pattern in enumerate(len5_patterns):
            if all(one_ele in len5_pattern for one_ele in one_compositions):
                unique_signal_patterns_to_digits_dict["3"] = len5_patterns.pop(idx)
            elif all(
                five_candidate_ele in nine_compositions
                for five_candidate_ele in len5_pattern
            ):
                unique_signal_patterns_to_digits_dict["5"] = len5_patterns.pop(idx)
            elif len(len5_patterns) == 1:
                unique_signal_patterns_to_digits_dict["2"] = len5_patterns.pop(idx)

    logger.debug(unique_signal_patterns_to_digits_dict)
    return unique_signal_patterns_to_digits_dict


def _decode(x, unique_signal_patterns_to_digits_dict):
    for k, v in unique_signal_patterns_to_digits_dict.items():
        if sorted(x) == sorted(v):
            return k
    return "0"
    # raise Exception(f"'{x}' is not known.")


def _map_strlist_to_int(str_list):
    return int("".join(str_list))


def decode_and_sum(ten_digits, four_digits_output):
    digits_list = []
    for ten_digits_ele, four_digits_output_ele in zip(ten_digits, four_digits_output):
        unique_signal_patterns_to_digits_dict = generate_unique_signal_patterns_to_digits_dict(
            ten_digits_ele
        )
        digits_list.append(
            _map_strlist_to_int(
                [
                    _decode(ele, unique_signal_patterns_to_digits_dict)
                    for ele in four_digits_output_ele
                ]
            )
        )
    return sum(digits_list)


def main():
    logging.basicConfig(
        format="%(asctime)s | %(levelname)-7s | %(message)s",
        datefmt="%H:%M:%S",
        level=logging.INFO,
    )
    ten_digits, four_digits_output = _parse_input(
        "/home/eileen/workspace/adventofcode2021/pyaoc/day8/input.txt"
    )

    instances_of_digits = count_unique_number_of_segments_instances_of_digits(
        four_digits_output
    )
    logger.info(f"Part 1 answer is '{instances_of_digits}'")  # 514

    sum_of_decoded_outputs = decode_and_sum(ten_digits, four_digits_output)
    logger.info(f"Part 2 answer is '{sum_of_decoded_outputs}'")  # 1012272


if __name__ == "__main__":
    main()
