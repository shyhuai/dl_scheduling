#!/bin/bash
nworkers="${nworkers:-2}"
size="${size:-26214400}"
iter="${iter:-20}"
gpuid="${gpuid:-0}"
#MPIPATH=/usr/local/openmpi/openmpi-4.0.1
MPIPATH=/home/esetstore/.local/openmpi-4.0.1
ALLREDUCE_BIN=/home/esetstore/downloads/nccl-tests/build/all_reduce_perf
#SOCKET_IFNAME=enp136s0f0,enp137s0f0
SOCKET_IFNAME=192.168.0.0/26
#SOCKET_IFNAME=ib0
$MPIPATH/bin/mpirun --oversubscribe --prefix $MPIPATH -np $nworkers --hostfile cluster$nworkers \
    -mca pml ob1 -mca btl ^openib --mca btl_openib_allow_ib 0 \
    -mca btl_tcp_if_include $SOCKET_IFNAME \
    -x NCCL_DEBUG=INFO \
    -x NCCL_IB_DISABLE=1 \
    -x CUDA_VISIBLE_DEVICES=$gpuid \
     $ALLREDUCE_BIN -b 10485760 -e 419430400 -i 10485760 -g 1 -c 0 -n $iter -z 1
    #$ALLREDUCE_BIN -b $size -e $size -i 10485760 -g 1 -c 0  -n $iter -z 1
    #-x NCCL_SOCKET_IFNAME=$SOCKET_IFNAME \
