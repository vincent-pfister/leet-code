from typing import List, Union

import numpy as np


PathType = list[tuple[int, int]]
IndexType = dict[str, set[tuple[int, int]]]


Tree = dict[str, Union[str, "Tree"]]


def make_tree(words: list[str]) -> Tree:
    words = sorted(words)
    return words_to_dict(words)


def words_to_dict(words: list[str], depth: int = 0) -> Tree:
    sub_list = {word[depth : depth + 1]: [] for word in words}
    for word in words:
        sub_list[word[depth : depth + 1]].append(word)
    sub_dict = {}
    for letter, sub_words in sub_list.items():
        if letter == "" and len(sub_words) == 1 and len(sub_words[0]) == depth:
            sub_dict[letter] = sub_words[0]
        else:
            non_leaf = [word for word in sub_words if len(word) > depth]
            sub_dict[letter] = words_to_dict(non_leaf, depth + 1)
    return sub_dict


def dict_to_words(tree: Tree) -> list[str]:
    words: list[str] = []
    for items in tree.values():
        if isinstance(items, str):
            words.append(items)
        else:
            words += dict_to_words(items)
    return words


def explore(
    path: PathType, word_tree: Tree, letter_index: IndexType, found: set[str]
) -> None:
    path_set = set(path)
    word_set = set(dict_to_words(word_tree))
    for letter, sub_tree in word_tree.items():
        if letter == "":
            found.add(sub_tree)
            continue
        locations = letter_index.get(letter, set())
        n = len(path)
        if n > 0:
            i, j = path[-1]
            adjacent = {(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)}
            locations = adjacent.intersection(locations).difference(path_set)
        for loc in locations:
            explore(path + [loc], sub_tree, letter_index, found)
            word_set.difference_update(found)
            if len(word_set) == 0:
                break


def reverse_word(word: str, letter_count: dict[str, int]) -> str:
    n = len(word)
    f = np.log([letter_count.get(letter, 1) for letter in word]) + 1e-5
    w_right = np.arange(n) + 1
    w_left = n - np.arange(n)
    if (w_right / f).sum() > (w_left / f).sum():
        return word[::-1]
    else:
        return word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        letter_index = {letter: set() for row in board for letter in row}
        for i, row in enumerate(board):
            for j, letter in enumerate(row):
                letter_index[letter].add((i, j))

        letter_count = {letter: len(locations) for letter, locations in letter_index.items()}
        sym_words = [reverse_word(word, letter_count) for word in words]
        word_tree = make_tree(sym_words)

        found: set[str] = set()
        explore([], word_tree, letter_index, found)
        return [word for word, sym in zip(words, sym_words) if sym in found]
