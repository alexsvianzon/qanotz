def _tokenize(text) -> list:
    tokens = []
    current = ""
    for char in text:
        if char in "{}":
            if current.strip():
                tokens.append(current.strip())
            tokens.append(char)
            current = ""
        elif char in "\n\t":
            if current and current[-1] != " ":
                current += " "
        else:
            current += char
    if current.strip():
        tokens.append(current.strip())

    tokens = [token for token in tokens if token != "{" and token != "}"]
    
    return tokens

def _parse_tokens(tokens: list) -> dict:
    result = {}
    index = 0
    
    while index < len(tokens):
        token = tokens[index]
        char_index = 0
        char = token[char_index]

        item = result.__len__()

        if char == "q":
            result[item] = {}
            result[item]["type"] = "question"

            char_index += 2
            char = token[char_index]
            if char.isdigit():
                result[item]["id"] = int(char)
                char_index += 1
            else:
                raise ValueError(f"Expected question ID at token: {token}")
            
            char_index += 1

            q_body: str = ""
            while char_index < len(token):
                q_body += token[char_index]
                char_index += 1

            result[item]["body"] = q_body

        if char == "a":
            result[item] = {}
            result[item]["type"] = "answer"

            char_index += 2
            char = token[char_index]
            if char.isdigit():
                result[item]["id"] = int(char)
                char_index += 1
            else:
                raise ValueError(f"Expected answer ID at token: {token}")
            
            char_index += 1

            q_body: str = ""
            while char_index < len(token):
                q_body += token[char_index]
                char_index += 1

            result[item]["body"] = q_body

        if char == "d":
            result[item] = {}
            result[item]["type"] = "data"

            char_index += 2
            char = token[char_index]
            if char in "chs":
                result[item]["id"] = char
                char_index += 1
            else:
                raise ValueError(f"Expected data ID at token '{token}' to be one of 'c', 'h', or 's'")
            
            char_index += 1

            q_body: str = ""
            while char_index < len(token):
                q_body += token[char_index]
                char_index += 1

            result[item]["body"] = q_body
            
        index += 1
            
    return result

        

def parse(text) -> dict:
    tokens = _tokenize(text)
    parsed = _parse_tokens(tokens)
    return parsed

if __name__ == "__main__":
    sample_text = "" \
    "{q 1 What is the capital of France? " \
    "{a 1 Paris {d s Wikipedia}} " \
    "{a 2 London {d s Wikipedia}}}"
    parsed = parse(sample_text)