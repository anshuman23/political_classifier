import argparse
import torch
import pandas as pd

from models import Model
from noyce_tokenizer import Tokenizer
from load_data import load_csv
from dataset import Dataset
from torch.utils.data import DataLoader
from utils.normalizer import normalize

import warnings #Remove in future, bad practice
warnings.filterwarnings("ignore")

if __name__ == '__main__':

  device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

  parser = argparse.ArgumentParser()
  parser.add_argument("-m", "--modelpath", help="Path to trained model")
  parser.add_argument("-d", "--datapath", help="Path to test data")

  args = parser.parse_args()
  model = Model(path = args.modelpath).to(device)
  tokenizer = Tokenizer(path = args.modelpath)
  df = pd.read_csv(open(args.datapath, 'rU'), encoding='utf-8', engine='c').dropna()

  df['text'] = df['text'].apply(normalize)
  x = df['text'].tolist()

  y = [0 for _ in range(len(x))]

  encodings = tokenizer(x, truncation=True, padding=True,
                                max_length=128,  return_tensors='pt')
  ds = Dataset(encodings, y)
  dl = DataLoader(ds, batch_size=32, shuffle=False)

  model.eval()
  text = []
  predictions = []
  confidence = []
  with torch.no_grad():
      for batch in dl:
          outputs = model(batch['input_ids'].to(device)).logits
          text = text + tokenizer.batch_decode(batch['input_ids'],skip_special_tokens=True)
          predictions = predictions + torch.argmax(outputs, axis=1).cpu().numpy().tolist()
          confidence = confidence + torch.nn.functional.softmax(outputs,dim=1).cpu().numpy().tolist()

  confidence = [ ["{:0.2%}".format(x) for x in v] for v in confidence]

  data={"text": x, "prediction" : predictions,"confidence":confidence}

  for index , c in enumerate(list(df.columns)):
    data[c] = df.iloc[:,index]

  predictions_df = pd.DataFrame(data=data)
  predictions_df.to_csv('predictions.csv')
