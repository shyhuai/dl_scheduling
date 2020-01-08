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
job_num=3 size=209715200 iter=100 ./multiple_nccl.sh
job_num=4 size=209715200 iter=100 ./multiple_nccl.sh
job_num=3 size=104857600 iter=100 ./multiple_nccl.sh
job_num=8 size=104857600 iter=100 ./multiple_nccl.sh
job_num=16 size=104857600 iter=100 ./multiple_nccl.sh
job_num=32 size=104857600 iter=100 ./multiple_nccl.sh
job_num=64 size=104857600 iter=100 ./multiple_nccl.sh
