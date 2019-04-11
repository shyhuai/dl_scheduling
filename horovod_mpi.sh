#!/bin/bash
#dnn="${dnn:-resnet20}"
#source exp_configs/$dnn.conf
#nworkers=4
#nwpernode=4
#nstepsupdate=1
hostfile="${hostfile:-job_configs/job_set_1/cluster_j0}"
job_root=job_configs
job_set="${job_set:-job_set_1}"
job_id="${job_id:-0}"
PY=/home/comp/qiangwang/anaconda2/bin/python
MPIPATH=/home/comp/qiangwang/software/openmpi-3.1.0
$MPIPATH/bin/mpirun --prefix $MPIPATH -hostfile $hostfile -bind-to none -map-by slot \
    -x NCCL_DEBUG=INFO -x LD_LIBRARY_PATH -x PATH \
    -mca pml ob1 -mca btl ^openib \
    -x NCCL_P2P_DISABLE=1 \
    $PY horovod_trainer.py --job-root $job_root --job-set $job_set --job-id $job_id