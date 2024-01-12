############## custom jupyter image ###############
FROM jupyter/scipy-notebook:x86_64-python-3.11 AS jupyter

ARG MLFLOW_ARTIFACT_STORE
ARG MLFLOW_VERSION
ARG JUPYTER_USERNAME
ENV HOME_DIR=/home/$JUPYTER_USERNAME
ENV WORK_DIR=$HOME_DIR/work


RUN pip install --upgrade notebook==6.4.12
RUN pip install --upgrade jupyterlab jupyterlab-git
COPY requirements.txt ./
RUN pip install --upgrade pip && \
    pip install -r ./requirements.txt

RUN jupyter contrib nbextension install --sys-prefix

RUN fix-permissions $CONDA_DIR

USER root
RUN sudo apt-get update
RUN sudo apt install -y git
RUN ldconfig
RUN mkdir -p $MLFLOW_ARTIFACT_STORE
RUN jupyter nbextension enable toc2/main --sys-prefix
RUN jupyter nbextension enable collapsible_headings/main --sys-prefix
#RUN fix-permissions $HOME_DIR

USER $NB_UID
WORKDIR $WORK_DIR
#RUN fix-permissions $HOME_DIR