
import logging

logger = logging.getLogger(__name__)


def _parse_input(input_file_path):
    logger.debug(f"Input file: {input_file_path}")
    with open(input_file_path, "r") as f:
        parsed_input = f.read().splitlines()
    return parsed_input


def _steps_sum_in_direction(list_of_parsed_commands, direction):
    list_of_steps = [int(steps_cmd) if direction_cmd == direction else 0 for direction_cmd, steps_cmd in list_of_parsed_commands]
    return sum(list_of_steps)


def _parse_commands(list_of_commands):
    list_of_parsed_commands = [ele.split(" ") for ele in list_of_commands]
    forward = _steps_sum_in_direction(list_of_parsed_commands, "forward")
    down = _steps_sum_in_direction(list_of_parsed_commands, "down")
    up = _steps_sum_in_direction(list_of_parsed_commands, "up")
    return (forward, down, up)


def compute_horizontal_and_depth_movements(list_of_commands):
    forward, down, up = _parse_commands(list_of_commands)
    horizontal_sum = forward
    depth_sum = down - up
    return (horizontal_sum, depth_sum)


def compute_horizontal_and_depth_movements_complicated(list_of_commands):
    list_of_split_commands = [ele.split(" ") for ele in list_of_commands]
    _aim = 0
    horizontal_sum = 0
    depth_sum = 0
    for direction_cmd, steps_cmd in list_of_split_commands:
        steps = int(steps_cmd)
        if direction_cmd == "down":
            _aim += steps
        elif direction_cmd == "up":
            _aim -= steps
        elif direction_cmd == "forward":
            horizontal_sum += steps
            depth_sum += _aim*steps
    return (horizontal_sum, depth_sum)


def main():
    logging.basicConfig(
        format="%(asctime)s | %(levelname)-7s | %(message)s",
        datefmt="%H:%M:%S",
        level=logging.INFO,
    )

    list_of_commands = _parse_input("/home/eileen/workspace/adventofcode2021/day2/input.txt")

    horizontal_sum, depth_sum = compute_horizontal_and_depth_movements(list_of_commands)
    logger.info(f"Part 1 answer is '{horizontal_sum*depth_sum}'")  # 1962940

    horizontal_sum, depth_sum = compute_horizontal_and_depth_movements_complicated(list_of_commands)
    logger.info(f"Part 2 answer is '{horizontal_sum*depth_sum}'")  # 1813664422


if __name__ == "__main__":
    main()
