# end-to-end-kidney-tumor

```bash
## Workflows
1. Update config.yaml
2. Update params.yaml
3. Update the entity
4. Update the configuration manager in src config
5. Update the components
6. Update the pipeline 
7. Update the dvc.yaml
8. Update the app.py
```

## Steps:

1. Git clone the repository and Define template of the project

```bash
touch template.py
python3 template.py
```

2. define setup.py scripts, Create environment and install dependencies

```bash
conda create -n kidney-env python=3.9 -y
conda activate kidney-env
pip install -r requirements.txt
```
3. define logger and utils

4. **Data Ingestion** 
* define config/config.yaml and constant.yaml --> add 01_data_ingestion.ipynb
* entity --> configuration manager --> componenets --> pipeline --> run `dvc repro`

5. **Base Model Section** 
* define config/config.yaml and params.yaml --> add 02_base_model.ipynb
* entity --> configuration manager --> componenets --> pipeline --> run `dvc repro`

5. **Model Training Section** 
* define config/config.yaml and params.yaml --> add 03_model_training.ipynb **(prepare call backs and train the model)**
* entity --> configuration manager --> componenets --> pipeline --> run `dvc repro`

6. **Model Evaluation**

* define config/config.yaml and params.yaml --> add 04_model_evaluation.ipynb
* entity --> configuration manager --> componenets --> pipeline --> run `dvc repro`
* **using mlflow** and **dagshub**
```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/fraidoon_omarzai/end-to-end-kidney-tumor.mlflow \
export MLFLOW_TRACKING_USERNAME=fraidoon_omarzai \
export MLFLOW_TRACKING_PASSWORD=bc25b16bd5206328d8899cf34377f26ad71d1420 \
```