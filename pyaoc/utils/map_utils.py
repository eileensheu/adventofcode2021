from collections import namedtuple

Coord = namedtuple("Coord", ["r", "c"])


def get_valid_neighbor_coords(row_idx, col_idx, len_row, len_col):
    neighbor_directions = {
        "right": Coord(r=row_idx, c=col_idx + 1),
        "left": Coord(r=row_idx, c=col_idx - 1),
        "below": Coord(r=row_idx + 1, c=col_idx),
        "above": Coord(r=row_idx - 1, c=col_idx),
    }

    # First row
    if row_idx == 0:
        neighbor_directions.pop("above")
    # Last row
    elif row_idx == len_row - 1:
        neighbor_directions.pop("below")
    else:
        pass

    # First col
    if col_idx == 0:
        neighbor_directions.pop("left")
    # Last col
    elif col_idx == len_col - 1:
        neighbor_directions.pop("right")
    else:
        pass

    return list(neighbor_directions.values())
