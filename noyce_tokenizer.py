from transformers import AutoTokenizer


def Tokenizer(name='bert', path = ''):
    tokenizers = {"bert": "bert-base-uncased",
                  "roberta": "roberta-base",
                  "xlmr": "xlm-roberta-base"}
    if len(path):
        return AutoTokenizer.from_pretrained(path)

    return AutoTokenizer.from_pretrained(tokenizers[name])
