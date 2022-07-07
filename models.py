from transformers import AutoModelForSequenceClassification


def Model(name='bert', path='', num_labels = 2):

    models = {"bert": "bert-base-uncased",
              "roberta": "roberta-base",
              "xlmr": "xlm-roberta-base"}
    if len(path):
        return AutoModelForSequenceClassification.from_pretrained(path)

    return AutoModelForSequenceClassification.from_pretrained(models[name], num_labels= num_labels)


