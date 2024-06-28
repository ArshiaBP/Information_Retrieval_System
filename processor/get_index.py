import math
import processor.champion_score
from models import term


def get_dictionary():
    dictionary = []
    with open('data/output.txt', 'r', encoding='utf-8') as file:
        for line in file:
            dictionary_term = term.Term("")
            dictionary_term.parse_string(line)
            if dictionary_term.content == "":
                continue
            dictionary.append(dictionary_term)
    processor.champion_score.create_champion_list(dictionary)
    return dictionary


def calculate_length(dictionary: []):
    n = 13000
    length = [0.0] * n
    for dictionary_term in dictionary:
        for posting in dictionary_term.posting_list:
            w_d = (1 + math.log(posting.term_frequency, 10))
            length[int(posting.doc_id)] += w_d * w_d
    for i in range(n):
        if length[i] != 0.0:
            length[i] = math.sqrt(length[i])
    return length
