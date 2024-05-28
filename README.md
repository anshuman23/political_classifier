# Political Classifier
### A fine-tuned RoBERTa model for classifying text as either political (1) or non-political (0). 


#### MODEL USAGE:
- Download the pretrained model, unzip it, and place the folder in the `saved_models/` directory
- Install requirements using `pip install -r requirements.txt` (I would recommend creating a virtual environment before doing so)
- Your input data needs to be a csv with a `text` column and the model can then generate predictions for it-- a sample data file is included in the repository as `sample_data.csv`
- To generate predictions (if your dataset is named `sample_data.csv`, otherwise change accordingly), run the following command inside the main directory: `python test_model.py -m saved_models/pol_clf_checkpoint -d sample_data.csv`
- You should now have a `predictions.csv` file with a classifier output column named `prediction`
- If you need the checkpoint files please reach out by email to anshumanc[at]usf[dot]edu.


#### TRAINING DATA:
- Available [here](https://github.com/anshuman23/political_classifier/blob/main/trainset_political_classifier.csv)

#### CITATION:
If you use our model/data, please cite the following papers:
- **Plain-text**:
  
  ```Askari, H., Chhabra, A., von Hohenberg, B. C., Heseltine, M., & Wojcieszak, M. (2024). Incentivizing News Consumption on Social Media Platforms Using Large Language Models and Realistic Bot Accounts. arXiv preprint arXiv:2403.13362.```
- **Bib**:

  ```@article{askari2024incentivizing,
  title={Incentivizing News Consumption on Social Media Platforms Using Large Language Models and Realistic Bot Accounts},
  author={Askari, Hadi and Chhabra, Anshuman and von Hohenberg, Bernhard Clemm and Heseltine, Michael and Wojcieszak, Magdalena},
  journal={arXiv preprint arXiv:2403.13362},
  year={2024}}
