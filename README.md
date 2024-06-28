# Lapyrinth

![Static Badge](https://img.shields.io/badge/made_in-France-red?labelColor=blue)
![Static Badge](https://img.shields.io/badge/language-Python-f7d54d?labelColor=4771a4)

This **Mazer Maker Solver** made entirely in Python is a program where you can generate maze with many different algorithm and solving them with different pathfinders. Nothing more, nothing less.

## Summary

### 1. [Features](#1---features)

### 2. [Installation](#2---installation)

### 3. [Generate a maze](#3---generate-a-maze)

### 4. [Example of mazes](#4---example-of-mazes)

### 5. [Save a maze](#5---save-a-maze)

### 6. [Load a maze](#6---load-a-maze)

### 7. [Solve a maze](#7---solve-a-maze)

### 8. [Maze Generation Benchmarks](#8---maze-generation-benchmarks)

### 9. [Pathfinders Benchmarks](#9---pathfinders-benchmarks)

### 10. [Improve the project](#10---improve-the-project)

## 1 - Features

- Generate any maze of any size

- Choose different algorithms from 11 of them (and more with different parameters)

- Generate an image of the maze generated

- Save the maze to load it later

- Solve them with various pathfinders among 9 of them

- Generate an image of the maze solved

## 2 - Installation

To begin, download and uncompress the **[latest version](https://github.com/Pietot/Maze-Maker-Solver/archive/refs/heads/main.zip)** or clone it by using one of the following command:

```
https://github.com/Pietot/Maze-Maker-Solver.git
```

or

```
git@github.com:Pietot/Maze-Maker-Solver.git
```

Then, you need to install all dependencies by opening a CLI (command line interface) and write these lines

```
cd "{the path to the project directory}"
pip install -r requirements.txt
```

## 3 - Generate a maze

To generate your first maze, write these lines at the end of <a href="https://github.com/Pietot/Maze-Maker-Solver/blob/main/maze.py">maze.py</a>:

```python
# Optional
start = (1, 7)
end = (5, 9)
# Or Maze(x) for a maze of x*x cells
maze = Maze(x, y, start, end)
# Choose the algorithm you want below
maze.binary_tree()
# If you want to make a so-called imperfect maze.
# You can specify the number of wall to removed
# or the probability that a wall will be removed
maze.make_imperfect_maze("number", 5)
# If you want to print the maze in the CLI
print(maze)
# If you want to generate a .png file of the maze
maze.generate_image()
```

or write the same lines in another python file in the same directory as <a href="https://github.com/Pietot/Maze-Maker-Solver/blob/main/maze.py">maze.py</a> but with an import at the beginning of the file like this:

```python
from maze import Maze

# Optional
start = (1, 7)
end = (5, 9)
# Or Maze(x) for a maze of x*x cells
maze = Maze(x, y, start=start, end=end)
# Choose the algorithm you want below
maze.binary_tree()
# If you want to make a so-called imperfect maze.
# You can specify the number of wall to removed
# or the probability that a wall will be removed
maze.make_imperfect_maze("number", 5)
# If you want to print the maze in the CLI
print(maze)
# If you want to generate a .png file of the maze
maze.generate_image()
```

> **Note**: Obviously, the larger the maze, the longer it will take to create and generate the image.

## 4 - Example of mazes

That's it. See, it's very simple. You can go with all of these algorithms:

- Kruskal
<p align="center">
<img src="assets/images/kruskal.png" width="49%" alt="Image illustrating a maze after using Kruskal's algorithm">
<img src="assets/gifs/kruskal.gif" width="49%" alt="Animation showing the process of Kruskal's algorithm"> <br><br>
</p>

- Randomized Depth First Search
<p align="center">
<img src="assets/images/rdfs.png" width="49%"alt="Image illustrating a maze after using Randomized Depth First Search algorithm"/>&nbsp;
<img src="assets/gifs/rdfs.gif" width="49%"alt="Animation showing the process of Randomized Depth First Search algorithm"> <br><br>
</p>

- Prim
<p align="center">
<img src="assets/images/prim.png" width="49%"alt="Image illustrating a maze after using Prim's algorithm"/>&nbsp;
<img src="assets/gifs/prim.gif" width="49%"alt="Animation showing the process of Prim's algorithm"> <br><br>
</p>

- Hunt and Kill
<p align="center">
<img src="assets/images/hunt_and_kill.png" width="49%"alt="Image illustrating a maze after using Hunt and Kill algorithm"/>&nbsp;
<img src="assets/gifs/hunt_and_kill.gif" width="49%"alt="Animation showing the process of Hunt and Kill algorithm"> <br><br>
</p>

- Eller (may vary depending on parameters)
<p align="center">
<img src="assets/images/eller.png" width="49%"alt="Image illustrating a maze after using Eller's algorithm"/>&nbsp;
<img src="assets/gifs/eller.gif" width="49%"alt="Animation showing the process of Eller's algorithm"> <br><br>
</p>

- Iterative Division
<p align="center">
<img src="assets/images/iterative_division.png" width="49%"alt="Image illustrating a maze after using Iterative Division algorithm"/>&nbsp;
<img src="assets/gifs/iterative_division.gif" width="49%"alt="Animation showing the process of Iterative Division algorithm"> <br><br>
</p>

- Binary Tree (may vary depending on parameters)
<p align="center">
<img src="assets/images/binary_tree.png" width="49%"alt="Image illustrating a maze after using Binary Tree algorithm"/>&nbsp;
<img src="assets/gifs/binary_tree.gif" width="49%"alt="Animation showing the process of Binary Tree algorithm"> <br><br>
</p>

- Sidewinder (may vary depending on parameters)
<p align="center">
<img src="assets/images/sidewinder.png" width="49%"alt="Image illustrating a maze after using Sidewinder algorithm"/>&nbsp;
<img src="assets/gifs/sidewinder.gif" width="49%"alt="Animation showing the process of Sidewinder algorithm"> <br><br>
</p>

- Growing Tree (may vary depending on parameters)
<p align="center">
<img src="assets/images/growing_tree.png" width="49%"alt="Image illustrating a maze after using Growing Tree algorithm"/>&nbsp;
<img src="assets/gifs/growing_tree.gif" width="49%"alt="Animation showing the process of Growing Tree algorithm"> <br><br>
</p>

- Aldous-Broder
<p align="center">
<img src="assets/images/aldous_broder.png" width="49%"alt="Image illustrating a maze after using Aldous-Broder algorithm"/>&nbsp;
<img src="assets/gifs/aldous_broder.gif" width="49%"alt="Animation showing the process of Aldous-Broder algorithm"> <br><br>
</p>

- Wilson
<p align="center">
<img src="assets/images/wilson.png" width="49%"alt="Image illustrating a maze after using Wilson's algorithm"/>&nbsp;
<img src="assets/gifs/wilson.gif" width="49%"alt="Animation showing the process of Wilson's algorithm"> <br><br>
</p>

## 5 - Save a maze

If you want to save the maze you've created, three options are available to you:

#### - Save the entire object:

```py
# Filename is optional
filename = "maze_object"
maze.save_maze("pkl", filename)
```

Pros / Cons:

- Saves all the data of the maze
- Can't be edited
- Easy to load
- Heavy file (~15Mo for a 1000x1000 cell maze)

#### - Save the maze's array as a binary file:

```py
# Filename is optional
filename = "maze_binary"
maze.save_maze("npy", filename)
```

Pros / Cons:

- Only saves the maze's array
- Can't be edited
- Fast to load
- Heavy file (~15Mo for a 1000x1000 cell maze)

#### - Save the maze's array as a text file:

```py
# Filename is optional
filename = "maze_text"
maze.save_maze("txt", filename)
```

Pros / Cons:

- Only saves the maze's array
- Easy to read and edit
- Slow to load
- Light file (~7.5Mo for a 1000x1000 cell maze)

## 6 - Load a maze

If you want to load the maze you've saved, two options are available to you depending on the file format:

#### - Load a .pkl file:

```py
from maze import load_object

maze = load_object("maze_object.pkl")
```

#### - Load a .npy or a .txt file:

```py
from maze import Maze

maze = Maze()
maze.load_maze("maze_binary.npy")
# Or
maze.load_maze("maze_text.txt")
```

> **Note**: The file must be in the same directory as the script or you must specify the path to the file.

## 7 - Solve a maze

Here's the code to follow to solve a maze:

```py
from maze import Maze

import pathfinders

maze = Maze(10)
maze.iterative_division()
path = pathfinders.depth_first_search(maze)
# If you want to print the solved maze in the CLI
pathfinders.print_path(maze, path)
# If you want to generate a .png file of the solved maze
pathfinders.generate_path(maze, path)
```

Here are all the pathfinders available:

- Right Hand Rule
<p align="center">
<img src="assets/gifs/right_hand.gif" width="49%"alt="Animation showing the process of the Right Hand rule pathfinder"> <br><br>
</p>

- Left Hand Rule
<p align="center">
<img src="assets/gifs/left_hand.gif" width="49%"alt="Animation showing the process of the Left Hand rule pathfinder"> <br><br>
</p>

- Random Mouse
<p align="center">
<img src="assets/gifs/random_mouse.gif" width="49%"alt="Animation showing the process of the Random Mouse pathfinder"> <br><br>
</p>

- Pledge (may vary depending on parameters)
<p align="center">
<img src="assets/gifs/pledge.gif" width="49%"alt="Animation showing the process of Pledge's pathfinder"> <br><br>
</p>

- Dead End Filler
<p align="center">
<img src="assets/gifs/dead_end_filler.gif" width="49%"alt="Animation showing the process of Dead End Filler pathfinder"> <br><br>
</p>

- Depth First Search
<p align="center">
<img src="assets/gifs/dfs.gif" width="49%"alt="Animation showing the process of Deep First Search pathfinder"> <br><br>
</p>

- Breadth First Search
<p align="center">
<img src="assets/gifs/bfs.gif" width="49%"alt="Animation showing the process of Breadth First Search pathfinder"> <br><br>
</p>

- Greedy Best First Search
<p align="center">
<img src="assets/gifs/gbfs.gif" width="49%"alt="Animation showing the process of Greedy Best First Search pathfinder"> <br><br>
</p>

- A\*
<p align="center">
<img src="assets/gifs/a_star.gif" width="49%"alt="Animation showing the process of A* pathfinder"> <br><br>
</p>

## 8 - Maze Generation Benchmarks

Wonder which algorithm is **faster**?

Well.. I already did it for you! So here you are:

- Chart for slow algorithms:

<img src="assets/svg/slow.svg"><br>

- Chart for moderately fast algorithms:

<img src="assets/svg/medium.svg"><br>

- Chart for fast algorithms:

<img src="assets/svg/fast.svg"><br>

- Chart for all algorithms:

<img src="assets/svg/full.svg"><br>

> **Note**: Aldous-Broder and Wilson algorithms were not tested because they are truly random (""luck"" based in other words), so their times are very inconsistent on a generation to another. But for an idea, they are even slower than Kruskal's algorithm

If you want the values of these graphs, watch this:

<img src="assets/images/screenshot.png">
<p align="center">
<br>
<a href="assets/csv/maze_generation_time.csv">Download csv here
</a>
<br>
</p>

> **Note**: These values can change depending on the version of Python and your PC<br><br>
> For these benchmarks, I used Python 3.12.0 implemented with CPython on a ryzen 5 3600, rtx 2060 with 2\*8GB of RAM clocked at 3600Hz on Windows 10.<br>
> These benchmarks were all tested at the same time (multiprocessing) so the results are higher than if they were tested one by one

## 9 - Pathfinders Benchmarks

Wonder which pathfinder is the most **efficient**?

Well.. I already did it for you! So here you are:

## 10 - Improve the project

If you like this project and/or want to help or improve it, you can:

- Create an issue if you find a bug or want to suggest a feature or any improvement (no matter how small it is).

- Create a pull request if you want to add a feature, fix a bug or improve the code.

- Contact me if you want to talk about the project or anything else (Discord: pietot).

> **Note**: If you want to be guided/helped, you already have a file named "IMPROVEMENTS.TXT" in the project directory, where you can see all the improvements that can be made.
