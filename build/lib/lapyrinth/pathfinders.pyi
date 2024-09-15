from _typeshed import Incomplete
from lapyrinth import Maze as Maze

class UnsolvableMaze(Exception):
    message: Incomplete
    def __init__(self, algorithm: str, error_message: str = "") -> None: ...

def left_hand(self) -> list[tuple[int, int]]: ...
def right_hand(self) -> list[tuple[int, int]]: ...
def random_mouse(self) -> list[tuple[int, int]]: ...
def pledge(self, following_direction: str) -> list[tuple[int, int]]: ...
def dead_end_filler(self) -> list[tuple[int, int]]: ...
def depth_first_search(self) -> list[tuple[int, int]]: ...
def breadth_first_search(self) -> list[tuple[int, int]]: ...
def greedy_best_first_search(self) -> list[tuple[int, int]]: ...
def dijkstra(self) -> list[tuple[int, int]]: ...
def a_star(self) -> list[tuple[int, int]]: ...
def turn_right(direction: tuple[int, int]) -> tuple[int, int]: ...
def turn_left(direction: tuple[int, int]) -> tuple[int, int]: ...
def update_path(
    path: list[tuple[int, int]], new_cell: tuple[int, int]
) -> list[tuple[int, int]]: ...
def update_cell_directions(
    cell_with_direction: dict[tuple[int, int], list[tuple[int, int]]],
    current_cell: tuple[int, int],
    direction: tuple[int, int],
    algorithm: str,
    error_message: str = "",
) -> None: ...
def get_dead_ends(self) -> list[tuple[int, int]]: ...
def directions_to_path(
    self, cell_with_directions: dict[tuple[int, int], list[tuple[int, int]]]
) -> list[tuple[int, int]]: ...
def reconstruct_path(
    self, came_from: dict[tuple[int, int], tuple[int, int]]
) -> list[tuple[int, int]]: ...
def generate_path(self, path: list[tuple[int, int]], filename: str | None = None) -> None: ...
def print_path(self, path: list[tuple[int, int]]) -> None: ...
