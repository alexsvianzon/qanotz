import token


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

            body: str = ""
            while char_index < len(token):
                body += token[char_index]
                char_index += 1

            result[item]["body"] = body
        elif char == "a":
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

            body: str = ""
            while char_index < len(token):
                body += token[char_index]
                char_index += 1

            result[item]["body"] = body
        elif char == "d":
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

            body: str = ""
            while char_index < len(token):
                body += token[char_index]
                char_index += 1

            result[item]["body"] = body
        elif char == "t":
            result[item] = {}
            result[item]["type"] = "title"

            char_index += 2

            body: str = ""
            while char_index < len(token):
                body += token[char_index]
                char_index += 1

            result[item]["body"] = body
        else:
            raise ValueError(f"Unexpected token type '{char}' in token: '{token}'")
            
        index += 1
            
    return result

        

def parse(text) -> dict:
    tokens = _tokenize(text)
    parsed = _parse_tokens(tokens)
    print(parsed)
    return parsed

if __name__ == "__main__":
    sample_text = """
    {t Common Questions}
    {q 1 How do I center a div?
        {a 1 CSS display and justify
            {d c Set 'display' to 'flex' and 'justify-content' to 'center'}
            {d h 1}}
        {a 2 CSS grid
            {d c Set 'display' to 'grid' and 'place-items' to 'center'}
            {d h 0.8}}}

    {q 1 How do I write a print statement in JavaScript?
        {a 1 CSS display and justify
            {d c 'message' must be a string or can be converted into one}
            {d c Don't forget a semicolon (;)}
            {d h 1}}
        {a 2 CSS grid
            {d c Set 'display' to 'grid' and 'place-items' to 'center'}
            {d h 0.8}}}"""
    parsed = parse(sample_text)