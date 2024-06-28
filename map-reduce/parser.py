import json
from preprocessor import tokenizer
from preprocessor import linguistic
from models import document


def mapper():
    collection = json.load(open("../data/IR_data_news_5k.json", "r", encoding="cp1256"))
    for doc_id, doc_value in collection.items():
        doc_title = doc_value.get('title', '')
        doc_url = doc_value.get('url', '')
        doc_content = doc_value.get('content', '')
        doc_info = document.Document(doc_id, doc_title, doc_url)
        doc_raw_tokens = tokenizer.tokenize(doc_content)
        doc_tokens = linguistic.normalize(doc_raw_tokens)
        doc_tokens = linguistic.stemmer(doc_tokens)
        token_position = 0
        for token in doc_tokens:
            info = doc_info.stringify()
            info += "*" + str(token_position)
            token_position += 1
            with open('../data/intermediate.txt', 'a', encoding="utf_8_sig") as f:
                f.write(token + "\t" + info + "\n")


mapper()
