from parsivar import FindStems


def normalize(tokens):
    for i in range(len(tokens)):
        english_digits = '0123456789'
        persian_digits = '۰۱۲۳۴۵۶۷۸۹'
        trans_table = str.maketrans(english_digits, persian_digits)
        tokens[i] = str(tokens[i]).replace("آ", "ا").replace("َ", "").replace("ُ", "").replace("ِ", "").replace("ّ", "").replace("ٍ", "").replace("ٌ", "").replace("ً", "").replace("ء", "")
        tokens[i] = tokens[i].translate(trans_table)
    return tokens


def stemmer(tokens):
    token_stemmer = FindStems()
    for i in range(len(tokens)):
        tokens[i] = token_stemmer.convert_to_stem(tokens[i]).split("&")[0]
    return tokens
