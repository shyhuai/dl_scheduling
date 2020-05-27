#rsync -u -avz -r --include="*.log" esetstore@10.1.82.11:/home/esetstore/repos/dl_scheduling/network_contention/logs/* ./logs/
rsync -u -avz -r --include="*.log" esetstore@10.1.82.11:/home/esetstore/repos/dl_scheduling/network_contention/results.csv ./
#rsync -u -avz -r --include="**/dgx*.log" --exclude="*" shshi@158.182.9.141:/home/shshi/work/p2p-dl/logs/* ./logs/
