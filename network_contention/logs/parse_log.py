from __future__ import print_function
import os
import numpy as np
import matplotlib.pyplot as plt


def read_times_from_nccl_log(logfile, mode='allreduce', start=0, end=128*1024*1024):
    print('fn: ', logfile)
    f = open(logfile)
    sizes = []
    times = []
    size_comms = {}
    for line in f.readlines():
        items = ' '.join(line.split()).split(' ')
        if (len(items) == 11 or len(items) == 12) and items[0] != '#':
            try:
                size = int(items[0])
            except:
                continue
            if size == 8:
                continue
            if (size >= start and size <= end):
                if size not in size_comms:
                    size_comms[size] = [] 
                try:
                    if mode == 'allreduce':
                        t = float(items[4])/(1000*1000)
                    else:
                        t = float(items[3])/(1000*1000)
                    size_comms[size].append(t)
                    sizes.append(size)
                    times.append(t)
                except:
                    continue
            #print(items)
    f.close()
    sizes = list(size_comms.keys())
    sizes.sort()
    comms = [np.mean(size_comms[s]) for s in sizes]
    errors = [np.std(size_comms[s]) for s in sizes]
    #print('sizes: ', sizes)
    #print('errors: ', errors)
    return np.array(sizes), np.array(comms), np.array(errors)


ns = [2, 4, 8]
js = list(range(1, 9))
size=104857600
all_comms = []
for nworkers in ns:
    comms = []
    for job_num in js:
        folder='logs/nccl_job_nw%d_n%d_s%d' % (nworkers, job_num, size)
        fn = 'nccl_job_1.log'
        logfile = os.path.join(folder, fn)
        _, c, _ = read_times_from_nccl_log(logfile)
        comms.append(c[0])
    all_comms.append(comms)
for i, c in enumerate(all_comms):
    plt.plot(c, label='%d workers'%ns[i])
plt.xlabel('# of jobs')
plt.ylabel('latency/us]us')
plt.legend()
plt.show()
