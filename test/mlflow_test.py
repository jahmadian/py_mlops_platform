import mlflow

mlflow.set_experiment('mlflow_experiments')
with mlflow.start_run():
    mlflow.log_param("name", "mlflow_test")
    mlflow.log_param("category", "algorithm")
    mlflow.log_param("type", "classification")
    for i in range(5):
        mlflow.log_metric("i", i, step=i)
    mlflow.log_artifact("mlflow_sample.ipynb")
