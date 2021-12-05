
import logging
from enum import Enum

logger = logging.getLogger(__name__)


def _parse_input(input_file_path):
    logger.debug(f"Input file: {input_file_path}")
    with open(input_file_path, "r") as f:
        diagnostic_report = f.read().splitlines()

    drawn_numbers = list(map(int, diagnostic_report[0].split(',')))
    boards = []
    _line = 2
    while _line < len(diagnostic_report):
        _board_rows = diagnostic_report[_line:_line+5]
        _board = [list(map(int, _board_row.split())) for _board_row in _board_rows]
        boards.append(_board)
        _line += 6

    logger.debug(f"Drawn_numbers: {drawn_numbers}")
    logger.debug(f"Boards: {boards}")
    return drawn_numbers, boards


def initialize_markboards(boards):
    markboards = []
    for board in boards:
        markboard = []
        for row in board:
            markboard_row = []
            for ele in row:
                markboard_row.append(False)
            markboard.append(markboard_row)
        markboards.append(markboard)
    return markboards


def _mark_drawn_number(drawn_number, board, markboard):
    for row_idx, row in enumerate(board):
        for ele_idx, ele in enumerate(row):
            if drawn_number == ele:
                markboard[row_idx][ele_idx] = True
    return markboard


def _bingo(_markboard):
    for row in _markboard:
        if False not in row:
            return True
    return False


def play_bingo(drawn_numbers, boards, markboards):
    bingo_drawn_numbers = []
    bingo_board_ids = []
    bingo_markboards = []
    should_break_now = False
    for drawn_number in drawn_numbers:
        logger.debug(f"=== drawn_number: {drawn_number} ===")
        for markboard_idx, markboard in enumerate(markboards):
            logger.debug(f"--- markboard_idx: {markboard_idx} ---")
            if markboard_idx in bingo_board_ids:
                continue
            markboard = _mark_drawn_number(drawn_number, boards[markboard_idx], markboard)
            markboard_transpose = list(map(list, zip(*markboard)))
            if _bingo(markboard) or _bingo(markboard_transpose):
                logger.debug(markboard)
                bingo_drawn_numbers.append(drawn_number)
                bingo_board_ids.append(markboard_idx)
                bingo_markboards.append(markboard)
                if len(bingo_board_ids) == len(boards):
                    should_break_now = True
                    break
        if should_break_now:
            break
    logger.debug(f"bingo_drawn_numbers: {bingo_drawn_numbers}")
    logger.debug(f"bingo_board_ids: {bingo_board_ids}")
    return bingo_drawn_numbers, bingo_board_ids, bingo_markboards


def count_score(final_drawn_number, board, markboard):
    sum_of_unmarked_numbers = 0
    for row_idx, row in enumerate(board):
        for ele_idx, ele in enumerate(row):
            if markboard[row_idx][ele_idx] == False:
                sum_of_unmarked_numbers += board[row_idx][ele_idx]
    return sum_of_unmarked_numbers*final_drawn_number


def main():
    logging.basicConfig(
        format="%(asctime)s | %(levelname)-7s | %(message)s",
        datefmt="%H:%M:%S",
        level=logging.INFO,
    )
    drawn_numbers, boards = _parse_input("/home/eileen/workspace/adventofcode2021/day4/input.txt")

    markboards = initialize_markboards(boards)
    bingo_drawn_numbers, bingo_board_ids, bingo_markboards = play_bingo(drawn_numbers, boards, markboards)

    first_bingo_drawn_numbers = bingo_drawn_numbers[0]
    first_bingo_board_id = bingo_board_ids[0]
    first_bingo_markboard = bingo_markboards[0]
    logger.debug(f"first_bingo_markboard: {first_bingo_markboard}")
    logger.debug(f"first_bingo_board: {boards[first_bingo_board_id]}")

    score_1 = count_score(first_bingo_drawn_numbers, boards[first_bingo_board_id], first_bingo_markboard)
    logger.info(f"Part 1 answer is '{score_1}'")  # 44088

    last_bingo_drawn_numbers = bingo_drawn_numbers[-1]
    last_bingo_board_id = bingo_board_ids[-1]
    last_bingo_markboard = bingo_markboards[-1]
    logger.debug(f"last_bingo_markboard: {last_bingo_markboard}")
    logger.debug(f"last_bingo_board: {boards[last_bingo_board_id]}")

    score_2 = count_score(last_bingo_drawn_numbers, boards[last_bingo_board_id], last_bingo_markboard)
    logger.info(f"Part 2 answer is '{score_2}'")  # 23670


if __name__ == "__main__":
    main()
