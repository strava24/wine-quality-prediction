# Building Complete ML Flow | Wine Quality Prediction

## Workflow to follow in all the stages

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py

## Setup

1. Clone the repo and go into it:
   ```bash
   git clone <repo-url>
   cd wine-quality-prediction
   ```
2. Create and activate a conda environment:
   ```bash
   conda create -p ./venv python=3.11 -y
   conda activate ./venv
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the pipeline:
   ```bash
   python main.py
   ```

## Data Ingestion

The goal: get the raw wine quality data onto your machine, ready for the next steps.

1. **Download** the dataset zip from `source_URL` (set in `config/config.yaml`). It is skipped if the file already exists.
2. **Extract** the zip into `artifacts/data_ingestion/`.

How the code is split:
- `config/config.yaml`: URL and paths
- `entity/`: holds the config as a simple object
- `config/configuration.py`: reads the YAML and builds that object
- `components/data_ingestion.py`: does the download and extract
- `pipeline/stage_01_data_ingestion.py`: runs the steps in order
- `main.py`: runs the stage and logs it

## Data Validation

The goal: make sure the data has the columns we expect before using it.

1. **Read** the CSV from `artifacts/data_ingestion/winequality-red.csv`.
2. **Check** that every column name exists in `schema.yaml`.
3. **Save** the result (`True` or `False`) to `artifacts/data_validation/status.txt`.

How it is set up:
- `schema.yaml`: the expected columns and their types
- `config/config.yaml`: the `data_validation` paths
- `research/data_validation.ipynb`: the first working version (not yet a pipeline stage)

## Data Transformation

The goal: split the data into a training set and a test set for the model.

1. **Check** the validation result in `artifacts/data_validation/status.txt`. If it is not `True`, stop.
2. **Read** the CSV from `artifacts/data_ingestion/winequality-red.csv`.
3. **Split** it into train (75%) and test (25%).
4. **Save** them as `train.csv` and `test.csv` in `artifacts/data_transformation/`.

How the code is split:
- `config/config.yaml`: the `data_transformation` paths
- `components/data_transformation.py`: does the split and saves the files
- `pipeline/stage_03_data_transformation.py`: checks the status, then runs the split
- `main.py`: runs this stage after validation

## Model Trainer

The goal: train a model on the training data and save it.

1. **Read** `train.csv` and `test.csv` from `artifacts/data_transformation/`.
2. **Separate** the inputs from the target column `quality` (set in `schema.yaml`).
3. **Train** an ElasticNet model using `alpha` and `l1_ratio` from `params.yaml`.
4. **Save** the model to `artifacts/model_trainer/model.joblib`.

How it is set up:
- `config/config.yaml`: the `model_trainer` paths and model name
- `params.yaml`: the ElasticNet settings
- `research/model_trainer.ipynb`: the first working version (not yet a pipeline stage)
