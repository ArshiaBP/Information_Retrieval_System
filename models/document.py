import models.term


class Document:
    def __init__(self, doc_id: str, doc_title: str, doc_url: str):
        self.doc_id = doc_id
        self.doc_title = doc_title
        self.doc_url = doc_url
        self.term_frequency = 0
        self.positions = []

    @classmethod
    def from_value(cls, doc: models.document.Document):
        return cls(doc.doc_id, doc.doc_title, doc.doc_url)

    def stringify(self):
        return self.doc_id + " " + self.doc_title + " " + self.doc_url

    def parse_string(self, info: str):
        doc_info = info.split()
        self.doc_id = doc_info[0]
        self.doc_title = doc_info[1]
        self.doc_url = doc_info[2]
        self.positions.append(doc_info[3])