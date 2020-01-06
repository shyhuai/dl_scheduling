size="${size:-65536}"
iter="${iter:-1000}"
#PY=/home/comp/qiangwang/anaconda2/bin/python
#MPIPATH=/home/t716/blackjack/software/openmpi-3.1.0
#MPIPATH=/usr/local/openmpi/openmpi-4.0.1
MPIPATH=/home/esetstore/.local/openmpi-4.0.1
hostfile="${hostfile:-cluster2}"
$MPIPATH/bin/mpirun --prefix $MPIPATH -np 2 -hostfile $hostfile -bind-to none -map-by slot \
        --mca btl_tcp_if_include enp136s0f0 \
        ./osu_allreduce -m $size:$size -i $iter
