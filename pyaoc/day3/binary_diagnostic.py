import logging

logger = logging.getLogger(__name__)


def _parse_input(input_file_path):
    logger.debug(f"Input file: {input_file_path}")
    with open(input_file_path, "r") as f:
        parsed_input = f.read().splitlines()
    return parsed_input


def get_gamma_rate(diagnostic_report):
    diagnostic_report_transpose = list(map(list, zip(*diagnostic_report)))
    gamma_rate_str_list = [
        "0" if nst_digit.count("0") > nst_digit.count("1") else "1"
        for nst_digit in diagnostic_report_transpose
    ]
    return "".join(gamma_rate_str_list)


def get_epsilon_rate(diagnostic_report):
    diagnostic_report_transpose = list(map(list, zip(*diagnostic_report)))
    epsilon_rate_str_list = [
        "0" if nst_digit.count("0") < nst_digit.count("1") else "1"
        for nst_digit in diagnostic_report_transpose
    ]
    return "".join(epsilon_rate_str_list)


def get_oxygen_generator_rating(diagnostic_report):
    filtered_diagnostic_report = diagnostic_report
    most_common_value = 0
    idx = 0
    while idx < len(diagnostic_report[0]):
        logger.debug(f"Checking index number '{idx}':")

        nst_digit = [
            diagnostic_record[idx] for diagnostic_record in filtered_diagnostic_report
        ]
        most_common_value = (
            "0" if nst_digit.count("0") > nst_digit.count("1") else "1"
        )  # if "0" and "1" are equally common, keep values with a "1" in the position being considered.
        logger.debug(f"most common value: '{most_common_value}'")

        filtered_diagnostic_report = list(
            filter(
                lambda diagnostic_record: diagnostic_record[idx] == most_common_value,
                filtered_diagnostic_report,
            )
        )
        logger.debug(f"filtered diagnostic report: {filtered_diagnostic_report}")
        logger.debug("--------------------------")

        if len(filtered_diagnostic_report) == 1:
            break

        idx += 1

    return filtered_diagnostic_report[0]


def get_co2_scrubber_rating(diagnostic_report):
    filtered_diagnostic_report = diagnostic_report
    most_common_value = 0
    idx = 0
    while idx < len(diagnostic_report[0]):
        logger.debug(f"Checking index number '{idx}':")

        nst_digit = [
            diagnostic_record[idx] for diagnostic_record in filtered_diagnostic_report
        ]
        most_common_value = (
            "1" if nst_digit.count("1") < nst_digit.count("0") else "0"
        )  # if "0" and "1" are equally common, keep values with a "0" in the position being considered.
        logger.debug(f"most common value: '{most_common_value}'")

        filtered_diagnostic_report = list(
            filter(
                lambda diagnostic_record: diagnostic_record[idx] == most_common_value,
                filtered_diagnostic_report,
            )
        )
        logger.debug(f"filtered diagnostic report: {filtered_diagnostic_report}")
        logger.debug("--------------------------")

        if len(filtered_diagnostic_report) == 1:
            break

        idx += 1

    return filtered_diagnostic_report[0]


def main():
    logging.basicConfig(
        format="%(asctime)s | %(levelname)-7s | %(message)s",
        datefmt="%H:%M:%S",
        level=logging.INFO,
    )

    diagnostic_report = _parse_input(
        "/home/eileen/workspace/adventofcode2021/pyaoc/day3/input.txt"
    )

    gamma_rate = get_gamma_rate(diagnostic_report)
    epsilon_rate = get_epsilon_rate(diagnostic_report)
    logger.debug(f"gamma_rate is '{gamma_rate}'")
    logger.debug(f"epsilon_rate is '{epsilon_rate}'")

    power_consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)
    logger.info(f"Part 1 answer is '{power_consumption}'")  # 1071734

    oxygen_generator_rating = get_oxygen_generator_rating(diagnostic_report)
    co2_scrubber_rating = get_co2_scrubber_rating(diagnostic_report)
    logger.debug(f"oxygen_generator_rating is '{oxygen_generator_rating}'")
    logger.debug(f"co2_scrubber_rating is '{co2_scrubber_rating}'")

    life_support_rating = int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)
    logger.info(f"Part 2 answer is '{life_support_rating}'")  # 6124992


if __name__ == "__main__":
    main()
