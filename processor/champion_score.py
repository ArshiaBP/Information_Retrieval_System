import bisect
import math
import inverter


def create_champion_list():
    n = 10000
    r = 100
    for index, term in enumerate(inverter.dictionary):
        weights = []
        for posting in term.posting_list:
            tf_idf = (1 + math.log(posting.term_frequency, 10)) * (math.log(n / term.doc_frequency, 10))
            weights.append((tf_idf, posting))
        sorted_weights = sorted(weights, key=lambda x: x[0])
        champion_postings = sorted_weights[-r:]
        champion_postings = sorted(champion_postings, key=lambda x: int(x[1].doc_id))
        for posting in champion_postings:
            inverter.dictionary[index].champion_list.append(posting)


# lnc-ltc
def calculate_cosine_champion(query_string: str):
    n = 10000
    k = 20
    scores = [0.0] * n
    length = [0.0] * n
    doc_info = [("", "")] * n
    query = query_string.split()
    indexes = []
    for term in query:
        index = bisect.bisect_left(inverter.dictionary, term, key=lambda x: x.content)
        if inverter.dictionary[index].content != term:
            continue
        indexes.append(index)
    index_counts = {}
    for index in indexes:
        if index in index_counts:
            index_counts[index] += 1
        else:
            index_counts[index] = 1
    for index, count in index_counts.items():
        w_q = (1 + math.log(count, 10)) * (math.log(n / inverter.dictionary[index].doc_frequency, 10))
        for posting in inverter.dictionary[index].champion_list:
            w_d = (1 + math.log(posting.term_frequency, 10))
            scores[int(posting.doc_id)] += w_d * w_q
            length[int(posting.doc_id)] += w_d * w_d
            if doc_info[int(posting.doc_id)] == ("", ""):
                doc_info[int(posting.doc_id)] = (posting.doc_title, posting.doc_url)
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
