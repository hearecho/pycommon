# 定时任务
### 1.While 实现定时任务
> 缺点:不容易控制，而且是一个阻塞函数
~~~python
def timer(n):
    '''
    每n秒执行一次
    '''
    while True:
        print(time.strftime('%Y-%m-%d %X',time.localtime()))
        #执行任务
        time.sleep(n)
~~~

### 2.schedule模块
> 优点：可以管理和调度多个任务，可以进行控制
> 缺点：阻塞式函数
