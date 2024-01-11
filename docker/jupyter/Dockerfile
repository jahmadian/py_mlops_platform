############## custom jupyter image ###############
FROM jupyter/scipy-notebook:x86_64-python-3.11 AS jupyter

ARG MLFLOW_ARTIFACT_STORE
ARG MLFLOW_VERSION
ARG JUPYTER_USERNAME
ENV HOME_DIR=/home/$JUPYTER_USERNAME
ENV WORK_DIR=$HOME_DIR/work


RUN apt-get update
RUN apt install -y git

RUN pip install --upgrade notebook==6.4.12
RUN pip install --upgrade jupyterlab jupyterlab-git
COPY ./requirements.txt ./
RUN pip install --upgrade pip && \
    pip install -r ./requirements.txt

RUN jupyter contrib nbextension install --sys-prefix

RUN fix-permissions $CONDA_DIR

USER root
RUN ldconfig
RUN mkdir -p $MLFLOW_ARTIFACT_STORE
RUN jupyter nbextension enable toc2/main --sys-prefix
RUN jupyter nbextension enable collapsible_headings/main --sys-prefix

USER $NB_UID
# Install Python dependencies from requirements.txt in advance
# Useful for development since changes in code will not trigger a layer re-build
WORKDIR $WORK_DIR
#RUN fix-permissions $HOME_DIR
#COPY ./requirements.txt ./
#RUN pip install --upgrade notebook==6.4.12
#RUN pip install --upgrade pip
#RUN pip install -r ./requirements.txt --user

# install experiment code in editable mode
#COPY ./setup.py ./
#COPY ./src/ ./src/
#
#USER root
#RUN chown -R $NB_UID:$NB_GID ./src/
USER $NB_UID