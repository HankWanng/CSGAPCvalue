from datetime import datetime
import time
import os
from apscheduler.schedulers.blocking import BlockingScheduler
import schedule
import psutil
from main1 import main1,main2


def ramused():
    curr_pid = os.getpid()
    currApp = psutil.Process(curr_pid)
    currApp_ramused = currApp.memory_full_info()
    usedram = currApp_ramused.uss / 1024. / 1024. / 1024.
    return usedram


def job1():
    main1()


def job2():
    main2()


def main():
    job_defaults = {'max_instances': 10}
    scheduler = BlockingScheduler(timezone='MST', job_defaults=job_defaults)
    scheduler.add_job(job1, 'interval', seconds=60)
    scheduler.add_job(job2, 'interval', seconds=5)
    try:
        scheduler.start()
    except Exception as err:
        print(err)
        return


if __name__ == '__main__':
    main()
