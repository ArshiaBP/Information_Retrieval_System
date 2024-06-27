import sys
from operator import attrgetter
from models import document
from models import term


dictionary = []


def reducer():
    pairs_list = []
    for line in sys.stdin:
        pair = line.split('\t')
        pairs_list.append(pair)
    pairs_list = sorted(pairs_list, key=lambda x: (x[0], x[1]))
    dictionary_terms = []
    current_term = ""
    current_term_id = -1
    for pair in pairs_list:
        doc = document.Document()
        doc.parse_string(pair[1].strip("\n"))
        if pair[0] == current_term:
            dictionary_terms[current_term_id].add_collection_frequency()
            dictionary_terms[current_term_id].update_posting(doc)
        else:
            current_term = pair[0]
            dictionary_term = term.Term(pair[0])
            dictionary_term.add_collection_frequency()
            dictionary_term.update_posting(doc)
            dictionary_terms.append(dictionary_term)
            current_term_id = len(dictionary_terms) - 1

    for index, dictionary_term in enumerate(dictionary_terms):
        dictionary_terms[index].doc_frequency = len(dictionary_term.posting_list)

    sorted_dictionary = sorted(dictionary_terms, key=attrgetter('collection_frequency'))
    final_dictionary = sorted_dictionary[:-50]
    final_dictionary = sorted(final_dictionary, key=attrgetter('content'))
    global dictionary
    dictionary = final_dictionary

    for dictionary_term in final_dictionary:
        print(dictionary_term.stringify())


reducer()
