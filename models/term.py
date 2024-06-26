import models.document


class Term:
    def __init__(self, content: str):
        self.content = content
        self.collection_frequency = 0
        self.doc_frequency = 0
        self.posting_list = []

    def add_collection_frequency(self):
        self.collection_frequency += 1

    def add_new_posting(self, doc: models.document.Document):
        exist = False
        index = 0
        for posting in self.posting_list:
            if posting.doc_id == doc.doc_id:
                self.posting_list[index].positions.append(doc.positions[0])
                self.posting_list[index].term_frequency += 1
                exist = True
                break
            index += 1
        if not exist:
            self.posting_list.append(doc)
            self.posting_list[len(self.posting_list) - 1].term_frequency += 1

    def stringify(self):
        postings_str = ""
        for posting in self.posting_list:
            positions = ""
            for position in posting.positions:
                positions += position + " "
            positions = positions[:len(positions) - 1]
            postings_str += posting.doc_id + "-" + posting.doc_title + "-" + posting.doc_url + "-" + posting.term_frequency + "-" + positions + "-"
        postings_str = postings_str[:len(postings_str) - 1]
        return self.content + ", " + str(self.collection_frequency) + ", " + str(self.doc_frequency) + ":" + postings_str
