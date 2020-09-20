#!/usr/bin/env python3


def getScore(inputText, expectedText):
    cleanInput, cleanExpected = cleanText(inputText, expectedText)
    result = getAllScore(cleanInput, cleanExpected)
    dict1 = getColorsToIndices(cleanExpected, result[0])
    return (result[1], dict1)


def getColorsToIndices(expectedTextTuples, resultTuplesFromScore):
    colors_to_indices = {"green": [], "yellow": [], "red": []}
    dict_color_mapping = dict(resultTuplesFromScore)
    for initial_word, base_word, index in expectedTextTuples:
        if (initial_word, index) in dict_color_mapping.keys():
            colors_to_indices[dict_color_mapping[(initial_word, index)]].append(index)
        else:
            colors_to_indices["red"].append(index)
    return colors_to_indices


def cleanText(inputText, expectedText):
    inputTextSplit = inputText.split()
    expectedSplit = expectedText.split()
    bothTexts = []
    for j in (inputTextSplit, expectedSplit):
        finalText = []
        word_num = 0
        for i in j:
            lower = i.lower()
            result = lower
            if lower[-1] == "s" and len(lower) >= 3:
                ch2 = lower[-2]
                if ch2 == "e":
                    i = i[:-2]
                elif not (ch2 == "s") and not (ch2 == "i") and not (ch2 == "u"):
                    i = i[:-1]
                result = i
            if len(result) >= 5:
                exclude = {"ed", "er", "ls", "ing", "ion", "est"}
                if result[-2:] in exclude:
                    result = result[:-2]
                elif result[-3:] in exclude:
                    result = result[:-3]
            finalText.append((i, result, word_num))
            word_num += 1
        bothTexts.append(finalText)
    return bothTexts


def getAllScore(inputText, expectedText):
    listText = [
        [[] for i in range(len(expectedText) + 1)] for j in range(len(inputText) + 1)
    ]
    arr = [[0] * (len(expectedText) + 1)] * (len(inputText) + 1)
    for i in reversed(range(len(inputText))):
        for j in reversed(range(len(expectedText))):
            curr_best = arr[i][j + 1]
            list_best = listText[i][j + 1]
            if arr[i + 1][j] >= curr_best:
                curr_best = arr[i + 1][j]
                list_best = listText[i + 1][j]
            scoreHelper = getOneScore(inputText[i], expectedText[j])
            if arr[i + 1][j + 1] + scoreHelper[0] > curr_best:
                curr_best = arr[i + 1][j + 1] + scoreHelper[0]
                list_best = listText[i + 1][j + 1]
                if scoreHelper[1] != tuple():
                    list_best = list_best.copy() + [scoreHelper[1]]
            arr[i][j] = curr_best
            listText[i][j] = list_best
    return (listText[0][0], arr[0][0] / len(expectedText))


def getOneScore(inputTextValue, expectedTextValue):
    scoreGreen = 1
    scoreYellow = 0.5
    scoreRed = 0
    if inputTextValue[0] == expectedTextValue[0]:
        return (scoreGreen, ((expectedTextValue[0], expectedTextValue[2]), "green"))
    if (
        inputTextValue[0] == expectedTextValue[1]
        or inputTextValue[1] == expectedTextValue[0]
        or inputTextValue[1] == expectedTextValue[1]
    ):
        return (scoreYellow, ((expectedTextValue[0], expectedTextValue[2]), "yellow"))
    return (scoreRed, tuple())
