FROM ghcr.io/mlflow/mlflow:v2.9.2

ARG SERVER_DIR=/server

RUN pip install psycopg2-binary==2.9.9

WORKDIR ${SERVER_DIR}

CMD mlflow server \
    --backend-store-uri ${MLFLOW_TRACKING_URI} \
    --default-artifact-root /${MLFLOW_ARTIFACT_STORE} \
    --host ${MLFLOW_TRACKING_SERVER_HOST} \
    --port ${MLFLOW_TRACKING_SERVER_PORT}
