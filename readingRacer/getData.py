#!/usr/bin/env python3






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
    for i in x2.keys():
        items = x2[i]
        list_by_difficulty = []
        for j in items:
            dict1 = {'text': j['text'], 'title':j['title'], 'number_words':j['number_words'], 'num_frequent_words':j['num_frequent_words']}
            tup = (j['difficulty'], dict1)
            list_by_difficulty.append(tup)
        list_by_difficulty = sorted(list_by_difficulty, key=lambda x: x[0])
        dict_with_difficulties[i] = list_by_difficulty
    return dict_with_difficulties

with open("../passages.json") as f:
    txt_dictionary = create_text_dict(f)
    difficulty_dictionary = create_difficulty_dictionary(f)