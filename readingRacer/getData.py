#!/usr/bin/env python3

import random
import json


def create_text_dict(json_file):
    '''
    Given a string of texts and the json file, return a dictionary mapping the text to a
    tuple containing: {text: (num_words, num_frequent_words, difficulty, reading_time)}
    '''
    grades = ('1', '2', '3', '4', '5', '6', '7', '8')
    result = {}
    for grade in grades:
        grade_data = json_file[grade]
        for text_dicts in grade_data:
            text_content = text_dicts['text']
            num_words = text_dicts['number_words']
            num_frequent_words = text_dicts['num_frequent_words']
            diff = text_dicts['difficulty']
            reading_time = text_dicts['reading_time']
            result[text_content]=(num_words, num_frequent_words, diff, reading_time)
    return result


def create_difficulty_dictionary(json_file):
    dict_with_difficulties = {}
    for i in json_file.keys():
        items = json_file[i]
        list_by_difficulty = []
        for j in items:
            dict1 = {'text': j['text'], 'title':j['title'], 'number_words':j['number_words'], 'num_frequent_words':j['num_frequent_words']}
            tup = (j['difficulty'], dict1)
            list_by_difficulty.append(tup)
        list_by_difficulty = sorted(list_by_difficulty, key=lambda x: x[0])
        dict_with_difficulties[i] = list_by_difficulty
    return dict_with_difficulties


def get_text_data(text):
    return txt_dictionary[text]


def get_difficulty(difficulty, old_difficulty):
    grade_level = str(int(difficulty))
    grade_level_list = difficulty_dictionary[grade_level]
    lower = 0
    higher = len(grade_level_list)
    values = []
    mid = (higher-lower)//2
    while higher > lower:
        mid = lower + (higher - lower)//2
        if grade_level_list[mid][0] == difficulty or (
                grade_level_list[mid][0] < difficulty < grade_level_list[mid + 1][0]):
            values += grade_level_list[max(mid-2, 0):min(mid+2, len(grade_level_list))]
            break
        elif grade_level_list[mid][0] < difficulty:
            lower = mid + 1
        elif grade_level_list[mid][0] > difficulty:
            higher = mid
    if not values:
        values += grade_level_list[max(mid-2, 0):min(mid+2, len(grade_level_list))]
    randDiff = values[random.randint(0, len(values)-1)]
    while randDiff[0] == old_difficulty:
        randDiff = values[random.randint(0, len(values)-1)]
    return (randDiff[1]['title'], randDiff[1]['text'])


with open("../passages.json") as f:
    x = json.load(f)
    json_file = json.loads(x)
    txt_dictionary = create_text_dict(json_file)
    difficulty_dictionary = create_difficulty_dictionary(json_file)