#! /bin/bash

docker run --name jupyter \
  -p 8888:8888 -v "$PWD":/home/jovyan/jupyter \
  --user root --restart=always -it \
  jupyter/tensorflow-notebook \
  bash

# pip install jupyterlab
# jupyter lab --allow-root