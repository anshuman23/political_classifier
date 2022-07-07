# Political Classifier
### A fine-tuned RoBERTa model for classifying text as either political (1) or non-political (0). 


#### Generating Predictions:
- Download the pretrained model, unzip it, and place the folder in the `saved_model/` directory
- Install requirements using `pip install -r requirements.txt` (I would recommend creating a virtual environment before doing so)
- Your input data needs to be a csv with a `text` column and the model can then generate predictions for it-- a sample data file is included in the repository as `sample_data.csv`
- To generate predictions, run: `python`
- You should now have a `predictions.csv` file with a classifier output column named `prediction`
