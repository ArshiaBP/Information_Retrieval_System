import json
from operator import attrgetter
from models import document
from models import term
from preprocessor import tokenizer
from preprocessor import linguistic


def create_index():
    collection = json.load(open("data/IR_data_news_5k.json", "r", encoding="cp1256"))
    pairs_list = []
    for doc_id, doc_value in collection.items():
        doc_title = doc_value.get('title', '')
        doc_url = doc_value.get('url', '')
        doc_content = doc_value.get('content', '')
        doc_info = document.Document(doc_id, doc_title, doc_url)
        doc_raw_tokens = tokenizer.tokenize(doc_content)
        doc_tokens = linguistic.normalize(doc_raw_tokens)
        doc_tokens = linguistic.stemmer(doc_tokens)
        token_position = 0
        for token in doc_tokens:
            info = doc_info.stringify()
            info += "*" + str(token_position)
            token_position += 1
            pair = [token, info]
            pairs_list.append(pair)

    pairs_list = sorted(pairs_list, key=lambda x: (x[0], x[1]))
    dictionary_terms = []
    current_term = ""
    current_term_id = -1
    for pair in pairs_list:
        if pair[0] == "":
            continue
        doc = document.Document("", "", "")
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

    for dictionary_term in final_dictionary:
        with open('data/output.txt', 'a', encoding="utf_8_sig") as f:
            f.write(dictionary_term.stringify() + "\n")


create_index()
