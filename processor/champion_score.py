import math
from bisect import bisect_left

from preprocessor import tokenizer
from preprocessor import linguistic


def create_champion_list(dictionary: []):
    n = 13000
    r = 100
    for index, term in enumerate(dictionary):
        weights = []
        for posting in term.posting_list:
            tf_idf = (1 + math.log(posting.term_frequency, 10)) * (math.log(n / term.doc_frequency, 10))
            weights.append((tf_idf, posting))
        sorted_weights = sorted(weights, key=lambda x: x[0])
        champion_postings = sorted_weights[-r:]
        champion_postings = sorted(champion_postings, key=lambda x: int(x[1].doc_id))
        for posting in champion_postings:
            dictionary[index].champion_list.append(posting)


# lnc-ltc
def calculate_cosine_champion(query_string: str, length, dictionary: []):
    n = 13000
    k = 20
    scores = [0.0] * n
    doc_info = [("", "")] * n
    query_raw_tokens = tokenizer.tokenize(query_string)
    query_tokens = linguistic.normalize(query_raw_tokens)
    query = linguistic.stemmer(query_tokens)
    indexes = []
    for term in query:
        index = bisect_left([dictionary_term.content for dictionary_term in dictionary], term)
        if dictionary[index].content != term:
            continue
        indexes.append(index)
    index_counts = {}
    for index in indexes:
        if index in index_counts:
            index_counts[index] += 1
        else:
            index_counts[index] = 1
    for index, count in index_counts.items():
        w_q = (1 + math.log(count, 10)) * (math.log(n / dictionary[index].doc_frequency, 10))
        for posting in dictionary[index].champion_list:
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
