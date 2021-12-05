
import logging

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
    return (drawn_numbers, boards)


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


def _mark_drawn_number(drawn_number, boards, markboards):
    for board_idx, board in enumerate(boards):
            for row_idx, row in enumerate(board):
                for ele_idx, ele in enumerate(row):
                    if drawn_number == ele:
                        markboards[board_idx][row_idx][ele_idx] = True
    return (boards, markboards)


def _bingo(markboard):
    for row in markboard:
        if False not in row:
            return True
    return False


def play_bingo(drawn_numbers, boards, markboards):
    for drawn_number in drawn_numbers:
        boards, markboards = _mark_drawn_number(drawn_number, boards, markboards)
        logger.debug(f"=== drawn_number: {drawn_number} ===")
        for markboard_idx, markboard in enumerate(markboards):
            logger.debug(f"--- markboard_idx: {markboard_idx} ---")
            logger.debug(markboard)
            markboard_transpose = list(map(list, zip(*markboard)))
            logger.debug(markboard_transpose)
            if _bingo(markboard) or _bingo(markboard_transpose):
                return (drawn_number, markboard_idx)
    raise Exception("None of the boards would bingo with the given drawn numbers.")


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
    final_drawn_number, bingo_board_idx = play_bingo(drawn_numbers, boards, markboards)

    score = count_score(final_drawn_number, boards[bingo_board_idx], markboards[bingo_board_idx])
    logger.info(f"Part 1 answer is '{score}'")  # 44088

    # logger.info(f"Part 2 answer is '{life_support_rating}'")  # 


if __name__ == "__main__":
    main()
