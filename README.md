# BENCHMARKING MACHINE LEARNING AND DEEP LEARNING TECHNIQUES USING THE CICIDS2017 DATASET

This repository store the source code the benchmark clasical machine learning, deep learning and tranformers techniques using the CICIDS2017 dataset..

## FILES' DESCRIPTION

### dependencies.txt

This file contains the used libraries by the notebook the performs de benchmark of techniques.

### pre_load_file.py

This script load the files, merge them into a new one  and then randomly generates files with different sizes.

### full.ipynb

This notebook is designed for descriptive task. It generates charts used to feed the final document of the thesis.


### benchmark.ipynb

This is the notebook that perform the benchmark of  clasical machine learning, deep learning and tranformers techniques.

For local execution, the dependicies  must included and the files located properly. 


## Utilities functions.

In the UTILITIES section, several functions are implemented. 

train_val_test_split: This function receives a dataset and return three new datasets with the following ratio, 60% for trainig, 20% for test and 20% for validation.


srt_corr: process correlation matrix, list highly correlated feature pairs

class F1ScoreMetric: A customized class for the F1 Score metric that is used by DL models (RNN, CNN, Transformes)

get_feature_importances_rf: Calculates the features importance using a Random Forest Classifier.

def get_feature_importances_xgb: Calculates the features importance using a XGBoost Classifier.


what_to_del: fucntion the return a list of correlated features.

class PositionalEncoding: class the defines a PositionalEncoding object.

build_transformer_model: Factory function that helps to generate a transfomer model with some default options

calculate_metrics: function that receives the expected and predicted values and return f1, accuracy, precision , recall and specificity metrics.
