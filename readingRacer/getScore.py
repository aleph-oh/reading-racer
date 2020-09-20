#!/usr/bin/env python3
import random
import getData
import json
import format_color


def get_random(grade_level):
    """
    Given a string of grade level (e.g. '1'), generate a random score within the range.
    """
    random_num = random.random()
    grade_level += random_num
    newTitle, newString = getData.get_difficulty(grade_level, 0)
    return newTitle, newString


def getScore(speechToTextInput, originalText):
    userInputText = getSpeechToTextFromJson(speechToTextInput)
    cleanInput, cleanExpected = cleanText(userInputText, originalText)
    result = getAllScore(cleanInput, cleanExpected, originalText)
    colorDictionary = getColorsToIndices(cleanExpected, result[0])
    #coloredString = format_color.format_color(originalText, colorDictionary)
    newTitle, newString = getNextString(result[1], originalText)
    return (newTitle, newString, colorDictionary)


def getNextString(score, originalText):
    oldDifficulty = getData.get_text_data(originalText)[2]
    newDifficulty = oldDifficulty + (score - 0.6) / 4 + random.random() * 0.2
    newText = getData.get_difficulty(newDifficulty, oldDifficulty)
    return newText


def getSpeechToTextFromJson(json1):
    # with open(json1, 'r') as f:
    #     x = json.load(f)
    json_data = json.loads(json1)
    i = json_data['results'][0]
    text = i['alternatives'][0]
    speech_to_text = text['transcript']
    return speech_to_text


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


def getAllScore(inputText, expectedTextList, expectedText):
    useful_len = getData.get_text_data(expectedText)[1]
    expectedText = expectedTextList
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
    return (listText[0][0], arr[0][0] / useful_len)


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


if __name__ == '__main__':
    print(getScore('{"result_index": 0, "results": [{"final": true, "alternatives": [{"transcript": "as I have said only these two magical pins are powerful enough to write on its pages when a story is completed within the book lore it becomes known to all the kingdoms in every corner of the globe so that the world may learn from them unable to find them and use their magic king was not strong enough to defeat his brother and sister ", "confidence": 0.86}], "word_alternatives": [{"start_time": 1.34, "end_time": 1.43, "alternatives": [{"word": "I", "confidence": 1.0}]}, {"start_time": 1.43, "end_time": 1.6, "alternatives": [{"word": "have", "confidence": 1.0}]}, {"start_time": 4.69, "end_time": 4.85, "alternatives": [{"word": "to", "confidence": 0.99}]}, {"start_time": 7.81, "end_time": 7.91, "alternatives": [{"word": "the", "confidence": 0.97}]}, {"start_time": 9.55, "end_time": 9.64, "alternatives": [{"word": "the", "confidence": 1.0}]}, {"start_time": 11.07, "end_time": 11.18, "alternatives": [{"word": "the", "confidence": 0.93}]}, {"start_time": 12.25, "end_time": 12.53, "alternatives": [{"word": "world", "confidence": 0.97}]}, {"start_time": 12.53, "end_time": 12.65, "alternatives": [{"word": "may", "confidence": 0.93}]}, {"start_time": 12.65, "end_time": 12.9, "alternatives": [{"word": "learn", "confidence": 0.94}]}, {"start_time": 12.9, "end_time": 13.09, "alternatives": [{"word": "from", "confidence": 0.94}]}, {"start_time": 13.65, "end_time": 14.02, "alternatives": [{"word": "unable", "confidence": 0.99}]}, {"start_time": 14.02, "end_time": 14.16, "alternatives": [{"word": "to", "confidence": 0.99}]}, {"start_time": 16.14, "end_time": 16.41, "alternatives": [{"word": "strong", "confidence": 0.97}]}, {"start_time": 16.41, "end_time": 16.62, "alternatives": [{"word": "enough", "confidence": 0.96}]}, {"start_time": 16.62, "end_time": 16.75, "alternatives": [{"word": "to", "confidence": 0.96}]}, {"start_time": 16.75, "end_time": 17.12, "alternatives": [{"word": "defeat", "confidence": 0.98}]}, {"start_time": 17.12, "end_time": 17.28, "alternatives": [{"word": "his", "confidence": 0.98}]}, {"start_time": 17.28, "end_time": 17.57, "alternatives": [{"word": "brother", "confidence": 1.0}]}, {"start_time": 17.57, "end_time": 17.76, "alternatives": [{"word": "and", "confidence": 1.0}]}, {"start_time": 17.76, "end_time": 18.32, "alternatives": [{"word": "sister", "confidence": 0.94}]}]}]}', "As I have said, only these two magical pens are powerful enough to write on its pages. And when a story is completed within the Book of Lore, it becomes known to all the kingdoms in every corner of the globe, so that the world may learn from them. Unable to find them and use their magic, the king was not strong enough to defeat his brother and sister."))
