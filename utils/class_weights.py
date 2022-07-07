import torch

def compute_class_weights(y):
  labels = set(y)
  weights = []
  for label in sorted(labels):
    count = y.count(label)
    weights.append(1/count)
  return torch.tensor(weights)

if __name__ == '__main__':
  y = [3,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,2,2,2,3,1,1,1,4]
  print(compute_class_weights(y))