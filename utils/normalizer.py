import re


def remove_URL(text):
    try:
        res = re.sub(r"http\S+", "", text)
        return re.sub(r"\s*[^ /]+/[^ /]+", "", res)
    except:
        return text


def remove_hashtag(text):
    try:
        return re.sub(r"#", "", text)
    except:
        return text


def remove_username(text):
    try:
        return re.sub(r"@[^\s]+", '', text)
    except:
        return text


def normalize(text, removeusername=True, removehashtag=True, removeURL=True):
    result = text
    if removeusername:
        result = remove_username(result)

    if removehashtag:
        result = remove_hashtag(result)

    if removeURL:
        result = remove_URL(result)

    return result
