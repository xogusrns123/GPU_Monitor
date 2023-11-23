# GPU_Monitor

## 1시간동안 gpu-burn을 통해서 GPU 최대로 사용할 때의 GPU의 여러 status monitoring
~~~
git clone https://github.com/xogusrns123/GPU_Monitor.git
cd GPU_Monitor
cd gpu-burn
sudo docker build -t gpu_burn .
cd ..
cd nvidia-monitor
sudo docker build -t nvidia_monitor .
cd ..
./run.sh
