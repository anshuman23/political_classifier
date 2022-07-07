
import pandas as pd
from utils.normalizer import normalize
from sklearn.model_selection import train_test_split


def load_csv(path):
    df = pd.read_csv(path, encoding='unicode_escape')
    df['text'] = df['text'].apply(normalize)
    return df['text'].tolist()

