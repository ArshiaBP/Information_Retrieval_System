from bisect import bisect_left
import math
from preprocessor import tokenizer
from preprocessor import linguistic


def choose_high_idf(query_string: str, dictionary: []):
    query_terms_tuple = []
    query_raw_tokens = tokenizer.tokenize(query_string)
    query_tokens = linguistic.normalize(query_raw_tokens)
    query = linguistic.stemmer(query_tokens)
    for term in query:
        index = bisect_left([dictionary_term.content for dictionary_term in dictionary], term)
        if dictionary[index].content != term:
            continue
        query_terms_tuple.append((index, dictionary[index].doc_frequency))
    if len(query_terms_tuple) == 0:
        return dict()
    query_terms_tuple = sorted(query_terms_tuple, key=lambda x: x[1])
    chosen_number = math.ceil(len(query_terms_tuple) * 0.75)
    chosen_terms_tuple = query_terms_tuple[:chosen_number]
    chosen_terms_indexes = []
    for term_tuple in chosen_terms_tuple:
        chosen_terms_indexes.append(term_tuple[0])
    index_counts = {}
    for index in chosen_terms_indexes:
        if index in index_counts:
            index_counts[index] += 1
        else:
            index_counts[index] = 1
    return index_counts


# lnc-ltc
def calculate_cosine_high_idf(index_counts, length, dictionary: []):
    n = 13000
    k = 20
    scores = [0.0] * n
    doc_info = [("", "")] * n
    for index, count in index_counts.items():
        w_q = (1 + math.log(count, 10)) * (math.log(n / dictionary[index].doc_frequency, 10))
        for posting in dictionary[index].posting_list:
            w_d = (1 + math.log(posting.term_frequency, 10))
            scores[int(posting.doc_id)] += w_d * w_q
            if doc_info[int(posting.doc_id)] == ("", ""):
                doc_info[int(posting.doc_id)] = (posting.doc_title, posting.doc_url)
    for i in range(n):
        if length[i] != 0.0:
            scores[i] /= length[i]
    for i in range(k):
        max_score = max(scores)
        if max_score == 0:
            continue
        max_doc_id = scores.index(max_score)
        doc_title = doc_info[max_doc_id][0]
        doc_url = doc_info[max_doc_id][1]
        doc_url = doc_url[:44]
        print(f"document_title: {doc_title}, document_url: {doc_url}, score: {scores[max_doc_id]}")
        scores[max_doc_id] = 0.0
        print()
