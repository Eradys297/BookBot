def word_count(content):
    split_words = content.split()
    num_words = len(split_words)
    return num_words

def char_count(content):
    char_dict = {}
    for s in content:
        s_low = s.lower()
        char_dict[s_low] = char_dict.get(s_low, 0) + 1
    return char_dict

def sort_on(input_dict):
    result = []
    for char, count in input_dict.items():
        result.append({"character": char, "count": count})
    result.sort(reverse=True, key=lambda item: item["count"])
    return result
