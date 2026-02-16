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

def _parse_tokens(tokens, index=0) -> (dict | tuple):
    """Recursively parse tokens into a dictionary structure."""
    result = {}
    
    while index < len(tokens):
        token = tokens[index]
        
        if token == "{":
            index += 1
            if index < len(tokens):
                marker = tokens[index]
                index += 1
                
                if marker == "q":  # Question
                    q_id = tokens[index]
                    index += 1
                    q_text = tokens[index]
                    index += 1
                    
                    result["question"] = {
                        "id": q_id,
                        "text": q_text,
                        "answers": []
                    }
                    
                elif marker == "a":  # Answer
                    a_id = tokens[index]
                    index += 1
                    a_text = tokens[index]
                    index += 1
                    
                    answer = {
                        "id": a_id,
                        "text": a_text,
                        "details": []
                    }
                    
                    # Parse details until we hit }
                    while index < len(tokens) and tokens[index] != "}":
                        if tokens[index] == "{":
                            index += 1
                            if index < len(tokens) and tokens[index] == "d":
                                index += 1
                                detail_type = tokens[index]
                                index += 1
                                detail_value = tokens[index]
                                index += 1
                                
                                answer["details"].append({
                                    "type": detail_type,
                                    "value": detail_value
                                })
                        else:
                            index += 1
                    
                    if "question" in result:
                        result["question"]["answers"].append(answer)
                    
                elif marker == "d":  # Detail
                    pass
        
        elif token == "}":
            return result, index + 1
        
        index += 1
    
    return result

def parse(text):
    """Parse QAN format into a dictionary structure."""
    tokens = _tokenize(text)
    print(tokens)

if __name__ == "__main__":
    sample_text = "" \
    "{q 1 What is the capital of France? " \
    "{a 1 Paris {d s Wikipedia}} " \
    "{a 2 London {d s Wikipedia}}}"
    parsed = parse(sample_text)