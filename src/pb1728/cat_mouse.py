"""Module.

(c) Raise Partner 2022
Vincent Pfister
"""
from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Cell:
    row: int
    col: int

    def __add__(self, other: "Cell") -> "Cell":
        return Cell(self.row + other.row, self.col + other.col)

    def __mul__(self, other: int) -> "Cell":
        return Cell(self.row * other, self.col * other)


NO_CELL = Cell(-1, -1)
DIRECTIONS = [
    Cell(-1, 0),
    Cell(1, 0),
    Cell(0, 1),
    Cell(0, -1),
]


class Board:

    def __init__(self, grid: list[str]):
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.grid = grid
        self.flat = "".join(grid)
        self.food = self.flat.find('F')
        self.cat = self.flat.find('C')
        self.mouse = self.flat.find('M')

    def to_cell(self, k: int) -> Cell:
        return Cell(k // self.cols, k % self.cols)

    def to_index(self, cell: Cell) -> int:
        return cell.row * self.cols + cell.col

    def __getitem__(self, item: tuple[int, int] | int):
        k = item if isinstance(item, int) else self.to_index(Cell(*item))
        return self.flat[k:k + 1]

    def get_moves(self, k: int, jump: int) -> list[int]:
        position = self.to_cell(k)
        candidates = [k]
        for direction in DIRECTIONS:
            for distance in range(1, jump + 1):
                candidate = position + direction * distance
                if 0 <= candidate.row < self.rows and 0 <= candidate.col < self.cols:
                    kc = self.to_index(candidate)
                    if self[kc] == "#":
                        break
                    candidates.append(kc)
                else:
                    break
        return candidates


@dataclass(frozen=True)
class Turn:
    mouse: int
    cat: int

    def __str__(self) -> str:
        return f"({self.mouse}, {self.cat})"


class Game:

    def __init__(self, grid: list[str], cat_jump: int, mouse_jump: int):
        self.board = Board(grid)
        self.jump: Turn = Turn(mouse_jump, cat_jump)
        self.nodes: dict[Turn, "Node"] = {}

    def add_node(self, turn: Turn, parent: Optional["Node"] = None) -> "Node":
        if turn in self.nodes:
            node = self.nodes[turn]
            if node.has_value:
                parent.set_value_from_child(node.turn, node.value)
            else:
                node.parents.append(parent)
        else:
            node = Node(turn, parent=parent)
            self.nodes[turn] = node
            mouse_moves = set(self.board.get_moves(turn.mouse, self.jump.mouse))
            cat_moves = set(self.board.get_moves(turn.cat, self.jump.cat))
            if self.board.food in mouse_moves:
                node.set_mouse_wins(True)
            elif self.board.food in cat_moves:
                node.set_mouse_wins(False)
            else:
                for next_turn in node.get_next_turns(mouse_moves, cat_moves):
                    self.add_node(next_turn, parent=node)
        return node

    def play(self) -> bool:
        start = self.add_node(Turn(self.board.mouse, self.board.cat))
        return start.has_value and start.value

    def show_graph(self) -> str:

        start = Turn(self.board.mouse, self.board.cat)
        m = {}
        i = 0

        def _get_node_name(node):
            nonlocal i
            if node.turn in m:
                s = m[node.turn]
            else:
                i += 1
                if node.turn == start:
                    if node.value:
                        before, after = "[[ fa:fa-check ", "]]"
                    else:
                        before, after = "[( fa:fa-xmark ", ")]"
                else:
                    if node.value:
                        before, after = "[", "]"
                    else:
                        before, after = "((", "))"
                s = f"T{i}{before}{node.turn.mouse}, {node.turn.cat}{after}"
                m[node.turn] = f"T{i}"
            return s

        txt = ["graph TD"]
        for turn, node in self.nodes.items():
            for parent in node.parents:
                s_turn = _get_node_name(node)
                s_parent = _get_node_name(parent)
                txt.append(f"{s_parent} --> {s_turn}")
        return "\n".join(txt)



class Node:

    def __init__(self, turn: Turn, parent: Optional["Node"] = None) -> None:
        self.has_value = False
        self.value = False
        self.turn = turn
        self.parents: list[Node] = [] if parent is None else [parent]
        self.wins_for_mouse: dict[int, int] = {}
        self.wins_for_cat: dict[int, int] = {}

    def get_next_turns(self, mouse_moves: set[int], cat_moves: set[int]):
        next_turns: list[Turn] = []
        mouse_moves.difference_update(cat_moves)
        if len(mouse_moves) == 0:
            self.set_mouse_wins(False)
        else:
            count_mouse_moves = len(mouse_moves)
            count_cat_moves = len(cat_moves)
            self.wins_for_mouse = {next_mouse: count_cat_moves for next_mouse in mouse_moves}
            self.wins_for_cat = {next_cat: count_mouse_moves for next_cat in cat_moves}
            for next_mouse in mouse_moves:
                for next_cat in cat_moves:
                    next_turns.append(Turn(next_mouse, next_cat))
        return next_turns

    def set_mouse_wins(self, mouse_wins: bool) -> None:
        self.has_value = True
        self.value = mouse_wins
        for parent in self.parents:
            parent.set_value_from_child(self.turn, mouse_wins)

    def set_value_from_child(self, turn: Turn, mouse_wins: bool) -> None:
        if self.has_value:
            return
        if mouse_wins:
            self.wins_for_mouse[turn.mouse] = self.wins_for_mouse[turn.mouse] - 1
            if min(self.wins_for_mouse.values()) == 0:
                self.set_mouse_wins(True)
        else:
            self.wins_for_cat[turn.cat] = self.wins_for_cat[turn.cat] - 1
            if min(self.wins_for_cat.values()) == 0:
                self.set_mouse_wins(False)


class Solution:

    def canMouseWin(self, grid: list[str], catJump: int, mouseJump: int) -> bool:
        game = Game(grid, catJump, mouseJump)
        result = game.play()
        print(game.show_graph())
        return result
