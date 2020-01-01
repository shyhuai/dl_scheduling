#!/bin/bash
#dnn="${dnn:-resnet20}"
#source exp_configs/$dnn.conf
#nworkers=4
#nwpernode=4
#nstepsupdate=1
global_sync="${global_sync:-2019_5_9_12_23_0}"
job_root="${job_root:-job_configs}"
job_set="${job_set:-job_set_0}"
job_id="${job_id:-0}"
hostfile="${hostfile:-job_configs/job_set_0/cluster_j0}"
#PY=$HOME/anaconda2/bin/python
PY=/usr/local/bin/python
#MPIPATH=$HOME/software/openmpi-3.1.0
MPIPATH=/usr/local/openmpi/openmpi-4.0.1
$MPIPATH/bin/mpirun --prefix $MPIPATH -hostfile $hostfile -bind-to none -map-by slot --allow-run-as-root \
    -x NCCL_DEBUG=INFO -x LD_LIBRARY_PATH -x PATH \
    -mca pml ob1 -mca btl ^openib \
    $PY horovod_trainer.py --job-root $job_root --job-set $job_set --job-id $job_id --global-sync $global_sync --mode real
