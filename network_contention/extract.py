#import matplotlib.pyplot as plt
import glob
import itertools
import numpy as np
import pandas as pd

markers=['.','x','o','v','^','<','>','1','2','3','4','8','s','p','*']
#markers=[None]
colors = ['b', 'g', 'r', 'm', 'y', 'k', 'orange', 'purple', 'olive']
markeriter = itertools.cycle(markers)
coloriter = itertools.cycle(colors)

def parse_log(log_root):

    print(log_root)
    filelist = glob.glob(r'%s/*.log' % log_root)
    #start_frame = pd.DataFrame({'Date':[], \
    #                           'Time':[], \
    #                           'Microsecond':[], \
    #                           'Latency':[]})
    #end_frame = pd.DataFrame({'Date':[], \
    #                           'Time':[], \
    #                           'Microsecond':[], \
    #                           'Latency':[]})
    start_frame = pd.DataFrame({'Datetime':[], \
                                'Latency':[]})
    end_frame = pd.DataFrame({'Datetime':[], \
                              'Latency':[]})
 
    dfs = []
    for log in filelist:
        print(log)
        with open(log, 'r') as f:
            content = f.readlines()[4:]
            content = [line for line in content if not ("failed" in line)]
            content = content[2:]
            content = [line.split() for line in content]
            #df = pd.DataFrame({'Date':[elem[0] for elem in content], \
            #                   'Time':[elem[1] for elem in content], \
            #                   'Microsecond':[elem[2] for elem in content], \
            #                   'Latency':[elem[3] for elem in content]})
            df = pd.DataFrame({'Datetime':["%s-%s-%09d" % (elem[0], elem[1], int(elem[2])) for elem in content], \
                               'Latency':[elem[3] for elem in content]})

            #df['Date'] = df['Date'].astype('str')
            #df['Time'] = df['Time'].astype('str')
            #df['Microsecond'] = df['Microsecond'].astype('int')
            df['Datetime'] = df['Datetime'].astype('str')
            df['Latency'] = df['Latency'].astype('float')
            #df = df.sort_values(by=['Date', 'Time', 'Microsecond'])
            df = df.sort_values(by=['Datetime'])
      
            start_frame.loc[len(start_frame)] = df.loc[0]
            end_frame.loc[len(end_frame)] = df.loc[len(df) - 1]

            dfs.append(df)

    print('dfs: ', dfs)
    #start_frame = start_frame.sort_values(by=['Date', 'Time', 'Microsecond']).loc[len(start_frame) - 1]
    #end_frame = end_frame.sort_values(by=['Date', 'Time', 'Microsecond']).loc[0]
    start_frame = start_frame.sort_values(by=['Datetime']).reset_index(drop=True)
    end_frame = end_frame.sort_values(by=['Datetime']).reset_index(drop=True)

    #print(start_frame)
    #print(end_frame)

    start_frame = start_frame.loc[len(start_frame) - 1]
    end_frame = end_frame.loc[0]
    
    latencies = []
    for df in dfs:
        #print len(df)
        #data = df[(df['Datetime'] >= start_frame.Datetime) & (df['Datetime'] <= end_frame.Datetime)]
        data = df #df[(df['Datetime'] >= start_frame.Datetime) & (df['Datetime'] <= end_frame.Datetime)]

        print(len(data))
        #latencies.extend(list(data.Latency))
        latency = list(data.Latency)
        latency.sort()
        #latencies.append(np.mean(latency))
        latencies.append(np.mean(latency[-10:]))
        #latencies.append(latency[-1])
    
    #latencies.sort()
    #return latencies[-1]
    return np.mean(latencies)

def main():

    with open("results.csv", "w") as f:

        f.write("node_num,job_num,msg_size,avg_latency\n")
        job_nums = [1, 2, 3, 4, 5, 6, 7, 8]
        #msg_sizes = [256, 1024, 4096, 16384, 65536, 262144]
        msg_sizes = [104857600]
        nodes = [2,3,4,5,6,7,8]
        #job_nums = [16]

        #fig, ax = plt.subplots(figsize = (12, 8))
        for msg_size in msg_sizes:
            
            throughput = []
            for n in nodes:
                for job_num in job_nums:
                    #latency.append(parse_log("logs/job_n%d_s%d" % (job_num, msg_size)))
                    #throughput.append(sum([msg_size / l for l in parse_log("logs/job_n%d_s%d" % (job_num, msg_size))]))
                    f.write("%d,%d,%d,%f\n" % (n, job_num, msg_size, parse_log("logs/v2_job_nnodes%d_n%d_s%d" % (n, job_num, msg_size))))


if __name__ == '__main__':
    main()
