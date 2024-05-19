""" A program capable of solving mazes with different path-finding algorithms. """


# By Pietot
# Discord : Piétôt#1754 | pietot
# Start : 16/05/2024 at 13h30 FR
# End : /05/2024 at h FR

# v1.0 :
# Start : 16/05/2024 at 13h30 FR
# End : 19/05/2024 at 23h15 FR
# Changelogs : Added the left hand rule pathfinder


import colorsys

import numpy as np

from PIL import Image, ImageDraw

from maze import Maze

import maze


def left_hand(self: Maze) -> list[tuple[int, int]]:
    """ Solve the maze with the left hand rule """
    direction_to_left: dict[tuple[int, int], tuple[int, int]] = {
        (0, 1): (-1, 0),
        (-1, 0): (0, -1),
        (0, -1): (1, 0),
        (1, 0): (0, 1)
    }
    current_cell: tuple[int, int] = self.start
    cell_with_direction: dict[tuple[int, int], tuple[int, int]] = {}
    direction = next(iter(direction_to_left))
    cell_with_direction[current_cell] = direction
    while current_cell != self.end:
        left_cell_col = current_cell[1] + direction_to_left[direction][1]
        left_cell_row = current_cell[0] + direction_to_left[direction][0]
        if self.maze[left_cell_row][left_cell_col] not in (0, 1):
            direction = rotate_90_counterclockwise(direction)
            cell_with_direction[current_cell] = direction
            current_cell = (left_cell_row, left_cell_col)
            continue
        front_cell_row = current_cell[0] + direction[0]
        front_cell_col = current_cell[1] + direction[1]
        if self.maze[front_cell_row][front_cell_col] in (0, 1):
            direction = rotate_90_clockwise(direction)
            cell_with_direction[current_cell] = direction
            front_cell_row = current_cell[0] + direction[0]
            front_cell_col = current_cell[1] + direction[1]
        else:
            cell_with_direction[current_cell] = direction
            current_cell = (front_cell_row, front_cell_col)
    path: list[tuple[int, int]] = []
    current_cell = self.start
    while current_cell != self.end:
        path.append(current_cell)
        current_cell = (current_cell[0] + cell_with_direction[current_cell][0],
                        current_cell[1] + cell_with_direction[current_cell][1])
    path.append(current_cell)
    return path


def rotate_90_clockwise(direction: tuple[int, int]) -> tuple[int, int]:
    """ Rotate a direction 90 degrees clockwise.

    Args:
        direction (tuple[int, int]): The direction to rotate.

    Returns:
        tuple[int, int]: The rotated direction.
    """
    row, column = direction
    return (column, -row)


def rotate_90_counterclockwise(direction: tuple[int, int]) -> tuple[int, int]:
    """ Rotate a direction 90 degrees counterclockwise.

    Args:
        direction (tuple[int, int]): The direction to rotate.

    Returns:
        tuple[int, int]: The rotated direction.
    """
    row, column = direction
    return (-column, row)


def generate_path(self: Maze, path: list[tuple[int, int]],
                  filename: str | None = None) -> None:
    """ Generate a maze image from a maze object. """
    size = self.maze.shape
    filename = (filename + '.png' if filename
                else f'Maze_{size[0]}x{size[1]}_{self.algorithm}.png')
    cell_size = 50

    image = Image.new(
        "RGB", (size[0]*cell_size, size[1]*cell_size), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    path_length = len(path)

    def get_color(step: int, total_steps: int) -> tuple[int, int, int]:
        # Adjust hue to go from red (0) to yellow (1/6)
        hue = 1/6 * (step / total_steps)
        r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
        return int(r * 255), int(g * 255), int(b * 255)

    def draw_path() -> None:
        for index, cell_value in np.ndenumerate(self.maze):
            x1 = index[1] * cell_size
            y1 = index[0] * cell_size
            x2 = (index[1] + 1) * cell_size
            y2 = (index[0] + 1) * cell_size

            if int(cell_value) in (0, 1):
                draw.rectangle((x1, y1, x2, y2), fill=(0, 0, 0))
            elif index in path:
                step = path.index(index)
                path_color = get_color(step, path_length)
                draw.rectangle((x1, y1, x2, y2), fill=path_color)
    draw_path()
    image.save(filename)
