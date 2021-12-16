import logging

logger = logging.getLogger(__name__)


def _parse_input(input_file_path):
    logger.debug(f"Input file: {input_file_path}")
    with open(input_file_path, "r") as f:
        parsed_input = list(map(int, f.read().splitlines()[0].split(",")))
    return parsed_input


def lanternfish_amount_after_n_days(list_of_lanternfish_ages, n):
    logger.debug(f"Initial state : {list_of_lanternfish_ages}")
    for i in range(n):
        list_of_lanternfish_ages = [
            6 if lanternfish_age == 0 else lanternfish_age - 1
            for lanternfish_age in list_of_lanternfish_ages
        ] + [8] * list_of_lanternfish_ages.count(0)
        logger.debug(f"After {i+1} day(s): {list_of_lanternfish_ages}")
    return len(list_of_lanternfish_ages)


def lanternfish_amount_after_n_days_dict_solution(list_of_lanternfish_ages, n):
    lanternfish_age_to_amount_dict = {}
    for age in range(8 + 1):
        lanternfish_age_to_amount_dict[age] = list_of_lanternfish_ages.count(age)

    for i in range(n):
        for age in range(8 + 1):
            if age == 0:
                amount_of_age_0 = lanternfish_age_to_amount_dict[age]
            else:
                lanternfish_age_to_amount_dict[
                    age - 1
                ] = lanternfish_age_to_amount_dict[age]
        lanternfish_age_to_amount_dict[6] += amount_of_age_0
        lanternfish_age_to_amount_dict[8] = amount_of_age_0
        logger.debug(f"After {i+1} day(s): {lanternfish_age_to_amount_dict.values()}")
    return sum(lanternfish_age_to_amount_dict.values())


def main():
    logging.basicConfig(
        format="%(asctime)s | %(levelname)-7s | %(message)s",
        datefmt="%H:%M:%S",
        level=logging.INFO,
    )
    list_of_lanternfish_ages = _parse_input(
        "/home/eileen/workspace/adventofcode2021/pyaoc/day6/input.txt"
    )
    logger.debug(f"Initial amount: {len(list_of_lanternfish_ages)}")

    lanternfish_amount_after_80_days = lanternfish_amount_after_n_days(
        list_of_lanternfish_ages, 80
    )
    logger.info(f"Part 1 answer is '{lanternfish_amount_after_80_days}'")  # 394994

    lanternfish_amount_after_256_days = lanternfish_amount_after_n_days_dict_solution(
        list_of_lanternfish_ages, 256
    )
    logger.info(
        f"Part 2 answer is '{lanternfish_amount_after_256_days}'"
    )  # 1765974267455


if __name__ == "__main__":
    main()
