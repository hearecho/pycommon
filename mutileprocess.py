#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/22 12:25
# @Author  : hearecho
# @Site    : 
# @File    : mutileprocess.py
# @Software: PyCharm

from multiprocessing import Process,Pool,Queue,cpu_count,active_children
import os,time,random,subprocess

#子进程要执行的代码
def run_process(name):
    print("Run child process %s (%s)...." %(name,os.getpid()))

#进程池
def long_time_task(name):
    print('Run task %s (%s)....' %(name,os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print("Task %s run %0.2f seconds " %(name,end-start))

#进程间通信  使用Queue
def write(q):
    print('Process to write :%s' %os.getpid())
    for value in ['A','B','C']:
        print('Put %s to queue' %value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    print("Process to read :%s" %os.getpid())
    while True:
        value = q.get(True)
        print("Get %s from queue." %value)

def process(num):
    time.sleep(num)
    print('Process',num)

if __name__ == "__main__":
    print('Parent process %s.' % os.getpid())
    # p = Process(target=run_process,args=('test',))
    # print("Child process will start.")
    # p.start()
    # p.join()#join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    # print("Child process end")
    # p = Pool(4)
    # for i in range(5):
    #     p.apply_async(long_time_task,args=(i,))
    # print('Waiting for all subprocesses done...')
    # p.close()
    # p.join()
    # print("All subprocesses done.")

    #subprocess 子进程
    # print('$ nslookup www.python.org')
    # r = subprocess.call(['nslookup', 'www.python.org'])
    # print('Exit code:', r)
    #进程间通信  使用Queue
    # q = Queue()
    # pw = Process(target=write,args=(q,))
    # pr = Process(target=read,args=(q,))
    #
    # pw.start()
    # pr.start()
    #
    # pw.join()

    #pr进程是死循环，无法等待期结束，所以使用 terminate
    # pr.terminate()

    for i in range(5):
        p = Process(target=process, args=(i,))
        p.start()

    print('CPU number:' + str(cpu_count()))
    for p in active_children():
        print('Child process name: ' + p.name + ' id: ' + str(p.pid))

    print('Process Ended')




