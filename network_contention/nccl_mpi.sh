nworkers="${nworkers:-2}"
MPIPATH=/usr/local/openmpi/openmpi-4.0.1
$MPIPATH/bin/mpirun -np $nworkers --hostfile cluster$nworkers ./all_reduce_perf -b 1M -e 512M -f 2 -g 1 -c 0 
