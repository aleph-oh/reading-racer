#!/usr/bin/env python3

def getScore(inputText, expectedText):
    texts = cleanText(inputText, expectedText)
    return getAllScore(texts[0], texts[1])


def cleanText(inputText, expectedText):
    inputTextSplit = inputText.split()
    expectedSplit = expectedText.split()
    bothTexts = []
    for j in (inputTextSplit, expectedSplit):
        finalText = []
        for i in j:
            lower = i.lower()
            result = lower
            if lower[-1] == 's' and len(lower) >= 3:
                ch2 = lower[-2]
                if not (ch2 == 's') and not (ch2 == 'i') and not (ch2 == 'u'):
                    result = result[:-1]
            elif len(result) >= 5:
                if result[-2:] == 'ed':
                    result = result[:-2]
                elif result[-3:] == 'ing':
                    result = result[:-3]
                elif result[-3:] == 'ion':
                    result = result[:-3]
                elif result[-2:] == 'er':
                    result = result[:-2]
                elif result[-3:] == 'est':
                    result = result[:-3]
                elif result[-2:] == 'ly':
                    result = result[:-2]
                elif result[-3:] == 'ity':
                    result = result[:-3]
            finalText.append((i, result))
        bothTexts.append(finalText)
    return bothTexts


def getAllScore(inputText, expectedText):
    arr = [[0] * (len(expectedText) + 1)] * (len(inputText) + 1)
    for i in reversed(range(len(inputText))):
        for j in reversed(range(len(expectedText))):
            arr[i][j] = max(arr[i][j + 1], arr[i + 1][j],
                            arr[i + 1][j + 1] + getScoreHelper(inputText[i], expectedText[j]))
    return arr[0][0] / (len(expectedText))


def getOneScore(inputTextValue, expectedTextValue):
    if inputTextValue[0] == expectedTextValue[0]:
        return 1
    if (inputTextValue[0] == expectedTextValue[1] or inputTextValue[1] == expectedTextValue[0] or
            inputTextValue[1] == expectedTextValue[1]):
        return 0.5
    return 0
