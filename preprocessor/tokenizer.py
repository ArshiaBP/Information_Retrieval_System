def tokenize(content):
    delimiters = ["'", ",", "+", "=", "]", "[", '"', "/", "-", "*", "؟", "!", "«", "»", "(", ")", "؛", ":", ".", "،", "\t", "\n"]
    for delimiter in delimiters:
        content = " ".join(content.split(delimiter))
    return content.split()
