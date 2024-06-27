import json
import sys
from preprocessor import tokenizer
from preprocessor import linguistic
from models import document


def mapper():
    for doc_json in sys.stdin:
        try:
            doc = json.loads(doc_json)
            doc_id = doc.get('id', 0)
            doc_title = doc.get('title', '')
            doc_url = doc.get('URL', '')
            doc_info = document.Document(doc_id, doc_title, doc_url)
            doc_content = str(doc.get('content', ''))
            doc_raw_tokens = tokenizer.tokenize(doc_content)
            doc_tokens = linguistic.normalize(doc_raw_tokens)
            doc_tokens = linguistic.stemmer(doc_tokens)
            token_position = 0
            for token in doc_tokens:
                info = doc_info.stringify()
                info += " " + str(token_position)
                token_position += 1
                print(f"{token}\t{doc_info.stringify()}")
        except json.JSONDecodeError:
            continue


mapper()
