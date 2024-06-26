import json
import sys
from preprocessor import tokenizer


class Document:
    def __init__(self, doc_id, doc_title, doc_url):
        self.doc_id = doc_id
        self.doc_title = doc_title
        self.doc_url = doc_url
        self.term_frequency = 0
        self.positions = []


class Term:
    def __init__(self, content):
        self.content = content
        self.frequency = 0
        self.doc_frequency = 0


def mapper():
    for doc_json in sys.stdin:
        tokens = set()
        try:
            doc = json.loads(doc_json)
            doc_id = doc.get('id', 0)
            doc_title = doc.get('title', '')
            doc_url = doc.get('URL', '')
            content = str(doc.get('content', ''))
            doc_tokens = tokenizer.tokenize(content)
            for token in doc_tokens:
                tokens.add(token)
            for token in tokens:
                print(f"{doc_id}\t{token}")
        except json.JSONDecodeError:
            continue


mapper()
