from __future__ import print_function
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def read_times_from_nccl_log(logfile, mode='allreduce', start=0, end=128*1024*1024, original=False):
    print('fn: ', logfile)
    f = open(logfile)
    sizes = []
    times = []
    size_comms = {}
    for line in f.readlines():
        if original and line[0:2] != '--':
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
        elif line[0:2] == '--':
            items = ' '.join(line.split()).split(' ')
            size = int(items[0][2:])
            t = float(items[1])/(1000*1000)
            times.append(t)
            if size not in size_comms:
                size_comms[size] = [] 
            size_comms[size].append(t)
            
    f.close()
    sizes = list(size_comms.keys())
    sizes.sort()
    #comms = [np.mean(size_comms[s]) for s in sizes]
    comms = [np.max(size_comms[s]) for s in sizes]
    comms = []
    for s in sizes:
        a = np.array(size_comms[s])
        a.sort()
        comms.append(np.mean(a[-2:]))
    errors = [np.std(size_comms[s]) for s in sizes]
    print('sizes: ', sizes)
    print('comms: ', comms)
    print('errors: ', errors)
    return np.array(sizes), np.array(comms), np.array(errors)

def _fit_linear_function(x, y):
    X = np.array(x).reshape((-1, 1))
    Y = np.array(y)
    #print('x: ', X)
    #print('y: ', Y)
    model = LinearRegression()
    model.fit(X, Y)
    alpha = model.intercept_
    beta = model.coef_[0]
    #A = np.vstack([X, np.ones(len(X))]).T
    #beta, alpha = np.linalg.lstsq(A, Y, rcond=None)[0]
    return alpha, beta

markers=['+', 'x', 'o']
fig, ax = plt.subplots(figsize = (12, 8))
def plot_contention():
    ns = [10] #, 4, 8]
    js = list(range(1, 9))
    #size=104857600/2*ns[0]
    size=104857600
    all_comms = []
    for nworkers in ns:
        comms = []
        for job_num in js:
            folder='logs/nccl_job_nw%d_n%d_s%d' % (nworkers, job_num, size)
            tmp_cs = []
            for k in range(1, job_num+1):
                fn = 'nccl_job_%d.log' % k
                logfile = os.path.join(folder, fn)
                _, c, _ = read_times_from_nccl_log(logfile, end=512*1024*1024, original=False)
                tmp_cs.append(c[0])
            c = np.max(tmp_cs)
            comms.append(c)
        all_comms.append(comms)
    
    for i, c in enumerate(all_comms):
        ax.plot(js, c, label='Measured (%d workers)'%ns[i], marker=markers[i])

    alpha_betas = {2: (0.0005662789473684163, 8.564366792377673e-10),
            4: (0.0002603352299668238, 1.2949395937171236e-09),
            #4: (0.0005662789473684163, 8.564366792377673e-10),
            #8: (0.0005662789473684163, 8.564366792377673e-10),
            8: (0.0024653663101605328, 1.490005930477285e-09), #(0.0016574696969697406, 1.5062312146166814e-09)
            }

    fitted = []
    for nworkers in ns:
        alpha, beta = alpha_betas.get(nworkers, alpha_betas[8])
        comms = []
        for j in js:
            comms.append(alpha+beta*j*size)
        fitted.append(comms)
        ax.plot(js, fitted[0], label='T=a+bkN ({} workers, a={:.2e}, b={:.2e})'.format(nworkers, alpha, beta), marker='o')

    ax.set_xlabel('# of jobs')
    ax.set_ylabel('Latency [s]')
    ax.legend()
    plt.show()


def plot_fitted():
    nworkers = 8
    MB = 1024 * 1024
    fn = 'logs/nccl_lg_nw%d.log' % nworkers
    sizes, comms, _ = read_times_from_nccl_log(fn, start=20*1024*1024*nworkers/2, end=1024*1024*1024)
    ax.plot(sizes/MB, comms, label='Measured (%d workers)'%nworkers, marker=markers[0])
    alpha, beta = _fit_linear_function(sizes, comms)
    ax.plot(sizes/MB, (alpha+np.array(sizes)*beta), label=r'Fitted ($a$=%.2e,$b$=%.2e)'%(alpha, beta), linewidth=1, color='r', linestyle='--')
    print('alpha beta: ', (alpha, beta))
    ax.set_xticklabels(sizes/MB, size=18)
    ax.set_xlabel('Message size [MB]')
    ax.set_ylabel('Elapse time [ms]')
    ax.grid(linestyle=':')
    ax.legend(fontsize=18, loc='upper left')
    plt.show()

plot_contention()
#plot_fitted()
