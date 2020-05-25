#job_num=1 size=64        sh multiple_osu.sh
#job_num=1 size=256       sh multiple_osu.sh
#job_num=1 size=1024      sh multiple_osu.sh
#job_num=1 size=4096      sh multiple_osu.sh
#job_num=1 size=16384     sh multiple_osu.sh
#job_num=1 size=65536     sh multiple_osu.sh
#job_num=1 size=262144    sh multiple_osu.sh
#job_num=1 size=1048576    sh multiple_osu.sh

#job_num=2 size=64        sh multiple_osu.sh
#job_num=2 size=256       sh multiple_osu.sh
#job_num=2 size=1024      sh multiple_osu.sh
#job_num=2 size=4096      sh multiple_osu.sh
#job_num=2 size=16384     sh multiple_osu.sh
#job_num=2 size=65536     sh multiple_osu.sh
#job_num=2 size=262144    sh multiple_osu.sh

#job_num=4 size=64        sh multiple_osu.sh
#job_num=4 size=256       sh multiple_osu.sh
#job_num=4 size=1024      sh multiple_osu.sh
#job_num=4 size=4096      sh multiple_osu.sh
#job_num=4 size=16384     sh multiple_osu.sh
#job_num=4 size=65536     sh multiple_osu.sh
#job_num=4 size=1048576    sh multiple_osu.sh

#job_num=8 size=64        sh multiple_osu.sh
#job_num=8 size=256       sh multiple_osu.sh
#job_num=8 size=1024      sh multiple_osu.sh
#job_num=8 size=4096      sh multiple_osu.sh
#job_num=8 size=16384     sh multiple_osu.sh
#job_num=8 size=65536     sh multiple_osu.sh
#job_num=8 size=262144    sh multiple_osu.sh
#
##job_num=16 size=64        sh multiple_osu.sh
#job_num=16 size=256       sh multiple_osu.sh
#job_num=16 size=1024      sh multiple_osu.sh
#job_num=16 size=4096      sh multiple_osu.sh
#job_num=16 size=16384     sh multiple_osu.sh
#job_num=16 size=65536     sh multiple_osu.sh
#job_num=16 size=262144    sh multiple_osu.sh
#
##job_num=32 size=64        sh multiple_osu.sh
#job_num=32 size=256       sh multiple_osu.sh
#job_num=32 size=1024      sh multiple_osu.sh
#job_num=32 size=4096      sh multiple_osu.sh
#job_num=32 size=16384     sh multiple_osu.sh
#job_num=32 size=65536     sh multiple_osu.sh
#job_num=32 size=262144    sh multiple_osu.sh
#
#job_num=3 size=209715200 iter=100 ./multiple_nccl.sh
#job_num=4 size=209715200 iter=100 ./multiple_nccl.sh
#job_num=3 size=104857600 iter=100 ./multiple_nccl.sh
#job_num=8 size=104857600 iter=100 ./multiple_nccl.sh
#job_num=16 size=104857600 iter=100 ./multiple_nccl.sh
#job_num=32 size=104857600 iter=100 ./multiple_nccl.sh
#job_num=64 size=104857600 iter=100 ./multiple_nccl.sh

#nworkers=2 job_num=2 size=104857600 iter=100 ./multiple_nccl.sh
#nworkers=8 job_num=1 size=104857600 iter=100 ./multiple_nccl.sh
#nworkers=8 job_num=2 size=104857600 iter=100 ./multiple_nccl.sh
#nworkers=8 job_num=4 size=104857600 iter=100 ./multiple_nccl.sh
#nworkers=8 job_num=8 size=104857600 iter=100 ./multiple_nccl.sh
#size=52428800
#size=104857600
#ns=( "5" "6" "7" "9" "10" "11" "12" "13" "14" "15" )
##ns=( "4" "8" )
#js=( "1" "2" "3" "4" "5" "6" "7" "8" )
#for nworkers in "${ns[@]}"
#do
#    for job_num in "${js[@]}"
#    do
#        #csize=$(expr $size "*" $nworkers )
#        csize=$size
#        echo $csize
#        nworkers=$nworkers job_num=$job_num size=$csize iter=20 ./multiple_nccl.sh
#    done
#done
ns=( "3" "5" "6" "7" "9" "10" "11" "12" "13" "14" "15" )
for nworkers in "${ns[@]}"
do
    iter=20 nworkers=$nworkers ./nccl_mpi.sh>logs/nccl_lg_nw$nworkers.log
done
#nworkers=2
#iter=20 nworkers=$nworkers ./nccl_mpi.sh>logs/nccl_lg_nw$nworkers.log
#nworkers=4
#iter=20 nworkers=$nworkers ./nccl_mpi.sh>logs/nccl_lg_nw$nworkers.log
#nworkers=8
#iter=20 nworkers=$nworkers ./nccl_mpi.sh>logs/nccl_lg_nw$nworkers.log
