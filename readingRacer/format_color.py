from misc_utils import invert_dict


def format_color(expected_text, colors_to_indices):
    """
    >>> c2i = {'green': [0, 2, 3], 'yellow': [], 'red': [1, 4]}
    >>> res = format_color("mary had a little lamb", c2i)
    >>> res == "<span markGreen>mary </span><span markRed>had </span><span markGreen>a little </span><span markRed>lamb</span>"
    :param expected_text: the original, correct text
    :param colors_to_indices: dict mapping colors (red, yellow, green) to indices of words
    with that color
    :return: valid html string highlighting words in appropriate colors
    """
    result_string = ""
    color_openings = {
        "green": "<span markGreen>",
        "yellow": "<span markYellow>",
        "red": "<span markRed>"
    }
    curr_color = None
    indices_to_colors = invert_dict(colors_to_indices)
    for i, word in enumerate(expected_text):
        assert len(indices_to_colors[i]) == 1
        for c in indices_to_colors[i]:
            color = c
        if i != 0:
            result_string += " "
        if color != curr_color:
            if curr_color is not None:
                result_string += "</span>"
            result_string += color_openings[color]
            curr_color = color
        result_string += word
    result_string += "</span>"
    return result_string
