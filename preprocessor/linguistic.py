from parsivar import FindStems


def normalize_space(tokens):
    normal_tokens = []
    for i in range(len(tokens)):
        if 0 < i < len(tokens) - 1:
            if tokens[i] == "می" or tokens[i] == "نمی":
                new_token = tokens[i] + "‌" + tokens[i + 1]
                normal_tokens.append(new_token)
                i += 1
            elif tokens[i] == "ی" or tokens[i] == "ای" or tokens[i] == "ها" or tokens[i] == "های" or tokens[i] == "هایی" or tokens[i] == "تر" or tokens[i] == "تری" or tokens[i] == "ترین" or tokens[i] == "گر" or tokens[i] == "گری" or tokens[i] == "ام" or tokens[i] == "ات" or tokens[i] == "اش":
                new_token = tokens[i - 1] + "‌" + tokens[i]
                normal_tokens.append(new_token)
                i += 1
            else:
                normal_tokens.append(tokens[i])
        elif i == 0:
            if tokens[i] == "می" or tokens[i] == "نمی":
                new_token = tokens[i] + "‌" + tokens[i + 1]
                normal_tokens.append(new_token)
                i += 1
            else:
                normal_tokens.append(tokens[i])
        else:
            if tokens[i] == "ی" or tokens[i] == "ای" or tokens[i] == "ها" or tokens[i] == "های" or tokens[i] == "هایی" or tokens[i] == "تر" or tokens[i] == "تری" or tokens[i] == "ترین" or tokens[i] == "گر" or tokens[i] == "گری" or tokens[i] == "ام" or tokens[i] == "ات" or tokens[i] == "اش":
                new_token = tokens[i - 1] + "‌" + tokens[i]
                normal_tokens.append(new_token)
                i += 1
            else:
                normal_tokens.append(tokens[i])

    for i in range(len(normal_tokens)):
        english_digits = '0123456789'
        persian_digits = '۰۱۲۳۴۵۶۷۸۹'
        trans_table = str.maketrans(english_digits, persian_digits)
        normal_tokens[i] = str(normal_tokens[i]).replace("آ", "ا").replace("َ", "").replace("ُ", "").replace("ِ", "").replace("ّ", "").replace("ٍ", "").replace("ٌ", "").replace("ً", "").replace("ء", "")
        normal_tokens[i] = normal_tokens[i].translate(trans_table)




# semi_space = "‌"
# my_stemmer = FindStems()
# w1 = "کتاب‌ها"
# w2 = "بروم"
# print(my_stemmer.convert_to_stem(w1).split("&"))