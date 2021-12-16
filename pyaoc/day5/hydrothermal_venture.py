from enum import Enum
import logging

logger = logging.getLogger(__name__)


def _parse_input(input_file_path):
    logger.debug(f"Input file: {input_file_path}")
    with open(input_file_path, "r") as f:
        input_lines = f.read().splitlines()
    lines = []
    for input_line in input_lines:
        line = []
        for pos in input_line.split(" -> "):
            line.append(list(map(int, pos.split(","))))
        lines.append(line)

    logger.debug(lines)
    return lines


class ConsideredDirection(Enum):
    hori_verti = 1
    hori_verti_diagonal = 2


def _add_1_to_point(points_dict, point):
    if point not in points_dict:
        points_dict[point] = 1
    else:
        points_dict[point] += 1
    return points_dict


def _get_points_of_vents(
    lines_of_vents,
    considered_direction: ConsideredDirection = ConsideredDirection.hori_verti,
):
    points_of_vents = {}

    for line in lines_of_vents:
        xa = line[0][0]
        ya = line[0][1]
        xb = line[1][0]
        yb = line[1][1]

        # vertical line; line x=X
        if xa == xb:
            for y in range(min(ya, yb), max(ya, yb) + 1):
                point = f"{xa},{y}"
                points_of_vents = _add_1_to_point(points_of_vents, point)

        # horizontal line; line y=Y
        elif ya == yb:
            for x in range(min(xa, xb), max(xa, xb) + 1):
                point = f"{x},{ya}"
                points_of_vents = _add_1_to_point(points_of_vents, point)

        # diagonal line
        elif (considered_direction == ConsideredDirection.hori_verti_diagonal) and (
            (xa - xb) == (ya - yb)
        ):
            y = min(ya, yb)
            for x in range(min(xa, xb), max(xa, xb) + 1):
                point = f"{x},{y}"
                points_of_vents = _add_1_to_point(points_of_vents, point)
                y += 1

        # diagonal line
        elif (considered_direction == ConsideredDirection.hori_verti_diagonal) and (
            xa - xb
        ) == -(ya - yb):
            y = max(ya, yb)
            for x in range(min(xa, xb), max(xa, xb) + 1):
                point = f"{x},{y}"
                points_of_vents = _add_1_to_point(points_of_vents, point)
                y -= 1
        else:
            continue
    return points_of_vents


def count_points_where_at_least_two_lines_overlap(
    lines_of_vents,
    considered_direction: ConsideredDirection = ConsideredDirection.hori_verti,
):
    points_of_vents = _get_points_of_vents(lines_of_vents, considered_direction)
    logger.debug(f"points_of_vents(<coordinates>:<count>): {points_of_vents}")

    points_where_at_least_two_lines_overlap = [
        k for k, v in points_of_vents.items() if v >= 2
    ]
    return len(points_where_at_least_two_lines_overlap)


def main():
    logging.basicConfig(
        format="%(asctime)s | %(levelname)-7s | %(message)s",
        datefmt="%H:%M:%S",
        level=logging.INFO,
    )
    lines_of_vents = _parse_input(
        "/home/eileen/workspace/adventofcode2021/pyaoc/day5/input.txt"
    )

    count_1 = count_points_where_at_least_two_lines_overlap(
        lines_of_vents, ConsideredDirection.hori_verti
    )
    logger.info(f"Part 1 answer is '{count_1}'")  # 4745

    count_2 = count_points_where_at_least_two_lines_overlap(
        lines_of_vents, ConsideredDirection.hori_verti_diagonal
    )
    logger.info(f"Part 2 answer is '{count_2}'")  # 18442


if __name__ == "__main__":
    main()
