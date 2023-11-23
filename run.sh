#! /bin/bash

sudo docker run --name my_gpu_burn -d --rm --gpus all -v /home/kth/GPU_Monitor:/app/data gpu_burn


sudo docker run --name my_gpu_monitor -d --rm --gpus all -it -v /home/kth/GPU_Monitor:/app/data nvidia_monitor

