def tokenize(content):
    delimiters = ["'", ",", "+", "=", "]", "[", '"', "/", "-", "*", "؟", "!", "«", "»", "(", ")", "؛", ":", ".", "،", "\t", "\n"]
    for delimiter in delimiters:
        content = " ".join(content.split(delimiter))
    tokens = content.split()
    normal_tokens = []
    jump_index = -1
    for i in range(len(tokens)):
        if i != jump_index:
            if 0 < i < len(tokens) - 1:
                if tokens[i] == "می" or tokens[i] == "نمی":
                    new_token = tokens[i] + "‌" + tokens[i + 1]
                    normal_tokens.append(new_token)
                    jump_index = i + 1
                elif tokens[i] == "ی" or tokens[i] == "ای" or tokens[i] == "ها" or tokens[i] == "های" or tokens[i] == "هایی" or tokens[i] == "تر" or tokens[i] == "تری" or tokens[i] == "ترین" or tokens[i] == "گر" or tokens[i] == "گری" or tokens[i] == "ام" or tokens[i] == "ات" or tokens[i] == "اش":
                    new_token = tokens[i - 1] + "‌" + tokens[i]
                    normal_tokens[len(normal_tokens) - 1] = new_token
                elif tokens[i] == "com":
                    if "@" in tokens[i - 1]:
                        new_token = tokens[i - 1] + "." + tokens[i]
                        normal_tokens[len(normal_tokens) - 1] = new_token
                else:
                    normal_tokens.append(tokens[i])
            elif i == 0:
                if tokens[i] == "می" or tokens[i] == "نمی":
                    new_token = tokens[i] + "‌" + tokens[i + 1]
                    normal_tokens.append(new_token)
                    jump_index = i + 1
                else:
                    normal_tokens.append(tokens[i])
            else:
                if tokens[i] == "ی" or tokens[i] == "ای" or tokens[i] == "ها" or tokens[i] == "های" or tokens[i] == "هایی" or tokens[i] == "تر" or tokens[i] == "تری" or tokens[i] == "ترین" or tokens[i] == "گر" or tokens[i] == "گری" or tokens[i] == "ام" or tokens[i] == "ات" or tokens[i] == "اش":
                    new_token = tokens[i - 1] + "‌" + tokens[i]
                    normal_tokens[len(normal_tokens) - 1] = new_token
                elif tokens[i] == "com":
                    if "@" in tokens[i - 1]:
                        new_token = tokens[i - 1] + "." + tokens[i]
                        normal_tokens[len(normal_tokens) - 1] = new_token
                else:
                    normal_tokens.append(tokens[i])
    return normal_tokens
