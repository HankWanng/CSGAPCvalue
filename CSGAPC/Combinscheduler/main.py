from datetime import datetime
import time
import DDE
import os
from apscheduler.schedulers.blocking import BlockingScheduler
import schedule
import psutil


def timefunc():
    # SpotTime = datetime.now().strftime("%m/%d/%Y %H:%M:%S") #24小时制
    SpotTime = datetime.now().strftime("%m/%d/%Y %I:%M:%S %p") #12小时制
    return SpotTime


def Opentxt(file):
    taglist = []
    with open(file, 'r') as txt:
        for line in txt.readlines():
            if "Root." in line:
                taglist.append(line.replace("\n", ".Value"))
                result = ','.join(taglist)
    return result


def ddefunc(datahubname, topic, filename, txtname):
    arrname = Opentxt(filename).split(",")  # tagname
    timestamp = timefunc()  # timestamp
    dde = DDE.DDEClient(datahubname, topic)
    if(os.path.exists(txtname)):
        os.remove(txtname)
    for i in arrname:
        # repi = i.replace(".value", "")
        DDEVALUE = dde.request(i)
        # print(DDEVALUE)

        linex = 'TAGNAME='+i.replace(".Value", "") + '\n'
        liney = 'ITEM=VALUE,VALUE={},TIMESTAMP={},QUALITY=192'.format(
            DDEVALUE, timestamp) + '\n'
        linez = linex+liney
#             print(linez)
        with open(txtname, "a+") as f:
            f.write(linez)


#CSGAPCValues
def main1():
    datahubname = "JSPIMSTEST"
    topic = "JSPIMSTEST"
    filename = r".\CSGAPCTags.txt"
    txtname = r'\\192.168.218.65\bpapimsdata\CSGEXPORT\CSGAPCValues.Txt'
    ddefunc(datahubname, topic, filename, txtname)
    print("*****"*5)
    print("CSGAPC程式运行OK")
    print(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
    print('当前进程的内存使用：', psutil.Process(os.getpid()).memory_info().rss)
    print('当前进程的内存使用：%.4f GB' %
          (psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024 / 1024))
    print("*****"*5)


#ELAPCVALUES
def main2():
    datahubname = "JSPIMSTEST"
    topic = "JSPIMSTEST"
    filename = r".\ELAPCTags.txt"
    txtname = r'\\192.168.218.65\bpapimsdata\ELEXPORT\ELAPCValues.Txt'
    ddefunc(datahubname, topic, filename, txtname)
    print("*****"*5)
    print("ELAPC程式运行OK")
    print(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
    print('当前进程的内存使用：', psutil.Process(os.getpid()).memory_info().rss)
    print('当前进程的内存使用：%.4f GB' %
          (psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024 / 1024))
    print("*****"*5)


def ramused():
    curr_pid = os.getpid()
    currApp = psutil.Process(curr_pid)
    currApp_ramused = currApp.memory_full_info()
    usedram = currApp_ramused.uss / 1024. / 1024. / 1024.
    return usedram


def job2():
    main1()
    time.sleep(1)
    main2()


def main():
    job_defaults = { 'max_instances': 10 }
    scheduler = BlockingScheduler(timezone='MST', job_defaults=job_defaults)
    scheduler.add_job(job2, 'interval', seconds=60)
    try:
        scheduler.start()
    except Exception as err:
        print(err)
        return


if __name__ == '__main__':
    main()
