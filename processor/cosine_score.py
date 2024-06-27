import bisect
import math
import inverter


def choose_high_idf(query: str):
    query_terms_tuple = []
    for term in query:
        index = bisect.bisect_left(inverter.dictionary, term, key=lambda x: x.content)
        if inverter.dictionary[index].content != term:
            continue
        query_terms_tuple.append((index, inverter.dictionary[index].doc_frequency))
    if len(query_terms_tuple) == 0:
        return dict()
    query_terms_tuple = sorted(query_terms_tuple, key=lambda x: x[1])
    chosen_number = math.ceil(len(query_terms_tuple) * 0.75)
    chosen_terms_tuple = query_terms_tuple[:chosen_number + 1]
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
def calculate_cosine(index_counts):
    n = 10000
    k = 20
    scores = [0.0] * n
    length = [0.0] * n
    doc_info = [("", "")] * n
    for index, count in index_counts.items():
        w_q = (1 + math.log(count, 10)) * (math.log(n / inverter.dictionary[index].doc_frequency, 10))
        for posting in inverter.dictionary[index].posting_list:
            w_d = (1 + math.log(posting.term_frequency, 10))
            scores[posting.doc_id] += w_d * w_q
            length[posting.doc_id] += w_d * w_d
            if doc_info[posting.doc_id] == ("", ""):
                doc_info[posting.doc_id] = (posting.doc_title, posting.doc_url)
    for i in range(n):
        if length[i] != 0:
            length[i] = math.sqrt(length[i])
            scores[i] /= length[i]
    for i in range(k):
        max_score = max(scores)
        max_doc_id = scores.index(max_score)
        doc_title = doc_info[max_doc_id][0]
        doc_url = doc_info[max_doc_id][1]
        scores[max_doc_id] = 0.0
        print(f"document_title: {doc_title}, document_url: {doc_url}")
