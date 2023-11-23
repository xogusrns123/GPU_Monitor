import matplotlib.pyplot as plt
file_path = '/home/jovyan/jupyter/gpu_status.txt'

try:
    with open(file_path, 'r') as f:
        lines = f.readlines()

    machine_num = 0
    gpu_names = []
    for line in lines:
        if line.startswith('GPU'):
            machine_num = machine_num + 1
            # print(line.split())
            name = line.split()[2] + ' ' + line.split()[3] + ' ' + line.split()[4]
            gpu_names.append(name)
        else:
            break
            
    buffer = 0
    times = []
    gflops = [[] for _ in range(machine_num)]
    temps = [[] for _ in range(machine_num)]
    for line in lines:
        line = line.strip()  # 공백 및 개행 문자 제거
        if line.startswith('Summary at:'):
            part = buffer.split()
       
            times.append(float(part[0]))
            for i in range(machine_num):

 
                gflops[i].append(int(part[i*4 + 3].split('(')[1]))

                temps[i].append(int(part[-2 + -3 * i]))
        else:
            buffer = line

    fig, axs = plt.subplots(8, 1, figsize=(12, 25))

    for i in range(machine_num):
        axs[0].plot(times, gflops[i], label=f'GPU {i} {gpu_names[i]}')
        axs[1].plot(times, temps[i], label=f'GPU {i} {gpu_names[i]}')

    axs[0].set_title('Gflop/s Over Time')
    axs[0].set_xlabel('Time (s)')
    axs[0].set_ylabel('Gflop/s')
    axs[0].legend(bbox_to_anchor=(1.02,1), loc='upper left')
    
    axs[1].set_title('Temperature Over Time')
    axs[1].set_xlabel('Time (s)')
    axs[1].set_ylabel('Temperature (C)')
    axs[1].legend(bbox_to_anchor=(1.02,1), loc='upper left')

    # 100s까지
    for i in range(machine_num):
        axs[2].plot(times[:100], gflops[i][:100], label=f'GPU {i} {gpu_names[i]}')
        axs[3].plot(times[:100], temps[i][:100], label=f'GPU {i} {gpu_names[i]}')

    axs[2].set_title('Gflop/s Over Time (First 268s)')
    axs[2].set_xlabel('Time (s)')
    axs[2].set_ylabel('Gflop/s')
    axs[2].legend(bbox_to_anchor=(1.02,1), loc='upper left')

    axs[3].set_title('Temperature Over Time (First 268s)')
    axs[3].set_xlabel('Time (s)')
    axs[3].set_ylabel('Temperature')
    axs[3].legend(bbox_to_anchor=(1.02,1), loc='upper left')

    # 100s 이후
    for i in range(machine_num):
        axs[4].plot(times[100:], gflops[i][100:], label=f'GPU {i} {gpu_names[i]}')
        axs[5].plot(times[100:], temps[i][100:], label=f'GPU {i} {gpu_names[i]}')


    axs[4].set_title('Gflop/s Over Time (After 269s)')
    axs[4].set_xlabel('Time (s)')
    axs[4].set_ylabel('Gflop/s')
    axs[4].legend(bbox_to_anchor=(1.02,1), loc='upper left')

    axs[5].set_title('Temperature Over Time (After 269s)')
    axs[5].set_xlabel('Time (s)')
    axs[5].set_ylabel('Temperature')
    axs[5].legend(bbox_to_anchor=(1.02,1), loc='upper left')

    for i in range(machine_num):
        axs[6].plot(times[1050:], gflops[i][1050:], label=f'GPU {i} {gpu_names[i]}')
        axs[7].plot(times[1050:], temps[i][1050:], label=f'GPU {i} {gpu_names[i]}')


    axs[6].set_title('Gflop/s Over Time (After 2773s)')
    axs[6].set_xlabel('Time (s)')
    axs[6].set_ylabel('Gflop/s')
    axs[6].legend(bbox_to_anchor=(1.02,1), loc='upper left')

    axs[7].set_title('Temperature Over Time (After 2773s)')
    axs[7].set_xlabel('Time (s)')
    axs[7].set_ylabel('Temperature')
    axs[7].legend(bbox_to_anchor=(1.02,1), loc='upper left')
        
    
    plt.tight_layout()
    plt.show()
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
