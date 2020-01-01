from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import torch
import time
from horovod.torch.mpi_ops import allreduce_async_
from horovod.torch.mpi_ops import synchronize
import horovod.torch as hvd
os.environ['HOROVOD_FUSION_THRESHOLD'] = '0'
os.environ['HOROVOD_CACHE_CAPACITY'] = '0'


class CommunicationProfiler(object):
    def __init__(self, comm_op, sync_op, sizes=None):
        self.comm_op = comm_op
        self.sync_op = sync_op
        self.sizes = sizes

    def benchmark(self, num_iters=100):
        if self.sizes is None:
            small_sizes = [8*1024*i for i in range(1, 64)] # 1K to 1M
            large_sizes = [] #[1024*1024*i for i in range(8)] # 1M to 512M
            sizes = small_sizes+large_sizes
        else:
            sizes = self.sizes
        warmup = 5
        size = 1024
        tensor = torch.rand(size).float().cuda()
        stime = time.time()
        for i in range(warmup):
            name = 'warmup-%d' % i
            h = self.comm_op(tensor, average=True, name=name)
            self.sync_op(h)
        etime = time.time()
        elapsed_times = []
        for s in sizes:
            tensor = torch.rand(s).float().cuda()
            torch.cuda.synchronize()
            stime = time.time()
            for i in range(num_iters):
                name = 'run-size%d-%d'% (s, i)
                h = self.comm_op(tensor, average=True, name=name)
                self.sync_op(h)
            etime = time.time()
            elapsed_times.append((etime-stime)/num_iters)
        return sizes, elapsed_times


ngpus_per_node = 4

hvd.init()
rank = hvd.rank()
torch.cuda.set_device(rank%ngpus_per_node)

comm_profiler = CommunicationProfiler(allreduce_async_, synchronize)
sizes, times = comm_profiler.benchmark(num_iters=10)

for s, t in zip(sizes, times):
    print('%d %f' % (s, t))
