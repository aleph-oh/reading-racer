import doctest
from typing import Dict, Iterable, List

from readingRacer.misc_utils import invert_dict


def format_color(
    expected_text: List[str], colors_to_indices: Dict[str, Iterable[int]]
) -> str:
    """
    Provide html representing string highlighted in colors matching `colors_to_indiced` for
    expected_text

    :param expected_text: the original, correct text
    :param colors_to_indices: dict mapping colors (red, yellow, green) to indices of words
           with that color
    :return: valid html string highlighting words in appropriate colors

    >>> c2i = {'green': [0, 2, 3], 'yellow': [], 'red': [1, 4]}
    >>> format_color("mary had a little lamb".split(), c2i)
    '<span markGreen>mary </span><span markRed>had </span><span markGreen>a little </span><span markRed>lamb</span>'
    """
    result_string = ""
    color_openings = {
        "green": "<span markGreen>",
        "yellow": "<span markYellow>",
        "red": "<span markRed>",
    }
    curr_color = None
    indices_to_colors = invert_dict(colors_to_indices)
    for i, word in enumerate(expected_text):
        try:
            assert (
                len(indices_to_colors[i]) == 1
            )  # bug: case where no highlight color exists
            for c in indices_to_colors[i]:
                color = c
            if i != 0:
                result_string += " "
            if color != curr_color:
                if curr_color is not None:
                    result_string += "</span>"
                result_string += color_openings[color]
            curr_color = color
        except IndexError:
            if curr_color is not None:  # string has a color already
                result_string += "</span>"
        result_string += word
    result_string += "</span>"
    return result_string


if __name__ == "__main__":
    doctest.testmod()
