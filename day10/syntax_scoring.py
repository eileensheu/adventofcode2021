from collections import namedtuple
import logging

logger = logging.getLogger(__name__)


def _parse_input(input_file_path):
    logger.debug(f"Input file: {input_file_path}")
    with open(input_file_path, "r") as f:
        parsed_input = f.read().splitlines()
    return parsed_input


closers_openers_dict = {")": "(", "]": "[", "}": "{", ">": "<"}


def remove_char_from_str_at_idx(str_obj, idx):
    return str_obj[0:idx:] + str_obj[idx + 1 : :]


Inconsistency = namedtuple("Inconsistency", ["expected", "found"])


def find_corrupted_and_incomplete_lines(syntax_lines):
    corrupted_lines = {}
    incomplete_lines = []
    for syntax_line in syntax_lines:
        logger.debug(syntax_line)
        syntax_line_processed = syntax_line
        is_a_corrupted_line = False
        while not is_a_corrupted_line:
            for idx, char in enumerate(syntax_line_processed):
                logger.debug(f"idx: {idx}, char: '{char}'")

                # if is a opener
                if char in closers_openers_dict.values():
                    continue

                # if is a closer
                elif char in closers_openers_dict.keys():

                    # if previous char and current char form a pair
                    if syntax_line_processed[idx - 1] == closers_openers_dict[char]:
                        syntax_line_processed = remove_char_from_str_at_idx(
                            syntax_line_processed, idx
                        )
                        syntax_line_processed = remove_char_from_str_at_idx(
                            syntax_line_processed, idx - 1
                        )
                        logger.debug(syntax_line_processed)
                        break
                    else:
                        corrupted_lines[syntax_line] = Inconsistency(
                            expected=syntax_line_processed[idx - 1],
                            found=syntax_line_processed[idx],
                        )
                        logger.debug(
                            f"corrupted_line: expected '{syntax_line_processed[idx - 1]}', found'{syntax_line_processed[idx]}'"
                        )
                        is_a_corrupted_line = True
                        break
                else:
                    raise Exception("Unknown syntax detected: '{char}'")
            if idx == len(syntax_line_processed) - 1 and not is_a_corrupted_line:
                incomplete_lines.append(syntax_line)
                logger.debug(f"incomplete_lines")
                break
    return corrupted_lines, incomplete_lines


syntax_score_table = {")": 3, "]": 57, "}": 1197, ">": 25137}


def compute_syntax_error_score(inconsistencies_list):
    found_inconsistencies_list = [
        inconsistency.found for inconsistency in inconsistencies_list
    ]
    score = 0
    for char, weight in syntax_score_table.items():
        score += weight * found_inconsistencies_list.count(char)
    return score


def main():
    logging.basicConfig(
        format="%(asctime)s | %(levelname)-7s | %(message)s",
        datefmt="%H:%M:%S",
        level=logging.INFO,
    )

    syntax_lines = _parse_input(
        "/home/eileen/workspace/adventofcode2021/day10/input.txt"
    )
    corrupted_lines, incomplete_lines = find_corrupted_and_incomplete_lines(
        syntax_lines
    )

    score = compute_syntax_error_score(list(corrupted_lines.values()))
    logger.info(f"Part 1 answer is '{score}'")  # 296535

    # logger.info(f"Part 2 answer is '{}'")  #


if __name__ == "__main__":
    main()
