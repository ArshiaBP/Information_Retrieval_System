class Document:
    def __init__(self, doc_id: str, doc_title: str, doc_url: str):
        self.doc_id = doc_id
        self.doc_title = doc_title
        self.doc_url = doc_url
        self.term_frequency = 0
        self.positions = []

    def stringify(self):
        return self.doc_id + " " + self.doc_title + " " + self.doc_url

    def parse_string(self, info: str):
        doc_info = info.split()
        self.doc_id = doc_info[0]
        self.doc_title = doc_info[1]
        self.doc_url = doc_info[2]