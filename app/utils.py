import re


def lower_first_letter(data):
    if isinstance(data, dict):
        new_dict = {}
        for key, value in data.items():
            new_key = key[0].lower() + key[1:]
            new_dict[new_key] = lower_first_letter(value)
        return new_dict
    elif isinstance(data, list):
        return [lower_first_letter(item) for item in data]
    else:
        return data


def remove_text_inside_brackets(text: str) -> str:
    # 移除尖括号及其内容
    text = re.sub(r"<[^>]*>", "", text)
    # 移除所有换行符
    text = text.replace(" ", "").replace("test/", "")
    return text
