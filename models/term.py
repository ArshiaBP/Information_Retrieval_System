from models import document


class Term:
    def __init__(self, content: str):
        self.content = content
        self.collection_frequency = 0
        self.doc_frequency = 0
        self.champion_list = []
        self.posting_list = []

    def add_collection_frequency(self):
        self.collection_frequency += 1

    def update_posting(self, doc: document.Document):
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
                positions += str(position) + "_"
            positions = positions[:len(positions) - 1]
            postings_str += str(posting.doc_id) + "*" + posting.doc_title + "*" + posting.doc_url + "*" + str(posting.term_frequency) + "*" + positions + "*"
        postings_str = postings_str[:len(postings_str) - 1]
        return self.content + "&" + str(self.collection_frequency) + "&" + str(self.doc_frequency) + "&" + postings_str

    def parse_string(self, info: str):
        comma_separated = info.split("&")
        if comma_separated[0] == "":
            return
        if not comma_separated[1].isdigit() or not comma_separated[2].isdigit():
            return
        self.content = comma_separated[0]
        self.collection_frequency = int(comma_separated[1])
        self.doc_frequency = int(comma_separated[2])
        postings = []
        posting_str = comma_separated[3].split("*")
        for i in range(self.doc_frequency):
            doc_id = posting_str[0 + 5 * i]
            doc_title = posting_str[1 + 5 * i]
            doc_url = posting_str[2 + 5 * i]
            doc = document.Document(doc_id, doc_title, doc_url)
            term_frequency = int(posting_str[3 + 5 * i])
            doc.term_frequency = term_frequency
            positions = []
            positions_list = posting_str[4 + 5 * i].split("_")
            for j in range(term_frequency):
                positions.append(int(positions_list[j]))
            positions.sort()
            doc.positions = positions
            postings.append(doc)
        self.posting_list = postings
