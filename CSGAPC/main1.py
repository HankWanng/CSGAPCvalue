from datetime import datetime
import time
import os
import psutil


def main1():
    # datahubname = "JSPIMSTEST"
    # topic = "JSPIMSTEST"
    # filename = r".\CSGAPCTags.txt"
    # txtname = r'\\192.168.218.65\bpapimsdata\CSGEXPORT\CSGAPCValues.Txt'
    # ddefunc(datahubname, topic, filename, txtname)
    print("*****"*5)
    print(datetime.now().strftime("%Y/%m/%d %I:%M:%S %p"))
    print('当前进程的内存使用：', psutil.Process(os.getpid()).memory_info().rss)
    print('当前进程的内存使用：%.4f GB' %
          (psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024 / 1024))
    print("*****"*5)


def main2():
    # datahubname = "JSPIMSTEST"
    # topic = "JSPIMSTEST"
    # filename = r".\ELAPCTags.txt"
    # txtname = r'\\192.168.218.65\bpapimsdata\ELEXPORT\ELAPCValues.Txt'
    # ddefunc(datahubname, topic, filename, txtname)
    print("*****"*5)
    print(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
    print('当前进程的内存使用：', psutil.Process(os.getpid()).memory_info().rss)
    print('当前进程的内存使用：%.4f GB' %
          (psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024 / 1024))
    print("*****"*5)
