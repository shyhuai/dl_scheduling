kill -9 `ps aux|grep 'python horovod_trainer.py' | awk '{print $2}'`
