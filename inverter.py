import sys
from operator import attrgetter
from models import document
from models import term


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
            dictionary_term = dictionary_terms[current_term_id]
            dictionary_term.add_collection_frequency()
            dictionary_term.add_new_posting(doc)
        else:
            current_term = pair[0]
            dictionary_term = term.Term(pair[0])
            dictionary_term.add_collection_frequency()
            dictionary_term.add_new_posting(doc)
            dictionary_terms.append(dictionary_term)
            current_term_id = len(dictionary_terms) - 1

    for dictionary_term in dictionary_terms:
        dictionary_term.doc_frequency = len(dictionary_term.posting_list)

    sorted_dictionary = sorted(dictionary_terms, key=attrgetter('doc_frequency'))
    final_dictionary = sorted_dictionary[51:]
    final_dictionary = sorted(final_dictionary, key=attrgetter('content'))

    for dictionary_term in final_dictionary:
        print(dictionary_term.stringify())
