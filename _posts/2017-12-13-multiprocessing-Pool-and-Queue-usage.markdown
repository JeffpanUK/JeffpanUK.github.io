---
layout:     post
title:      "Multiprocessing中pool和queue的使用"
subtitle:   " multiprocessing makes life hard "
date:       2017-12-13 11:32:13
author:     "Jeff"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - python
---
### 使用多进程可以采用的两种方式

- Queue
- Pool

### Queue 队列,先进先出

#### 使用queue的流程

1. 使用`multiprocessing.Queue(N)`申明一个大小为N的Queue
2. 定义一个`putQueue`函数将任务加入队列： `queue.put(task)`
3. 使用`multiprocessing.Process(target=putQueue, args=(queue,))` 调用`putQueue` 函数。 需要注意如果是queue作为参数，后面需要加逗号
4. 定义一个`subProcess` 子进程函数，然后调用`multiprocessing.Process(target=subProcess, args=(queue,))` 调用该函数

#### 注意事项

- 若多进程定义在类内，则`putQueue`和`subProcess` 函数需定义为类函数，使用标识符`@classmethod` 修饰。
- 获取队列时，如果使用`queue.get()` ，在队列为空时会阻塞。 一般使用`queue.get_nowait()` ，当队列为空时会报Empty Error
- 使用queue时会默认跑满所有CPU

#### 示例代码

```python
 class SelectWord(object):
    def __init__(self):
        ......
        ......
    def process(self):
    taskQ = multiprocessing.Queue(4)
    taskP = multiprocessing.Pool()
    procP = multiprocessing.Pool()
    taskR=[]
    resultR = []
    result_list = set([])
    for f in self.fs:
      f = os.path.join(self.base, f)
      taskP.apply_async(SelectWord.putQ, args=(os.path.join(self.base, f),))
      taskT = multiprocessing.Process(target=SelectWord.putQ, args=(taskQ, os.path.join(self.base, f)))
      taskR.append(taskT)
      taskT.start()
    for i in range(len(self.fs)):
      result_list = result_list.union(procP.apply_async(SelectWord.subProcess, args=(f, self.puncs, self.wlist)).get())      
      worker = multiprocessing.Process(target=SelectWord.subProcess, args=(taskQ, self.puncs, self.wlist))
      resultR.append(worker)
      worker.start()    
    with codecs.open(self.outfile, 'w', 'utf-8') as fo:
      for w in list(result_list):
        print("Find word: %s"%w)
        fo.write("%s\n"%w)
      
    for r in taskR:
      r.join()   # main process holds and waits for all subprocess complete
    taskQ.close() #close queue as no further task coming 
    for r in resultR:
      r.join()
    
  @classmethod  
  def subProcess(cls, queue):
      fn = queue.get()
      print(fn+str(os.getpid()))
  
  @classmethod    
  def putQueue(cls, queue, f):
      queue.put(f)
```

### Pool 进程池

#### 使用Pool的流程

1. 使用`multiprocessing.Pool(N)` 定义一个N进程的进程池，$N \leq CPU数目$ . N也可以不指定
2. 定义`subProcess` 子进程函数，通过`pool.apply_async(subProcess, args=(args*)` 来调用。 如果需要获取返回值，可用`pool.apply_async(subProcess, args=(args*)).get()` 来获取
3. 当进程池填完后，使用`pool.close()` 和`pool.join()` 关闭进程池并等待子进程完成

#### 示例代码

```python
def process(self):
    procP = multiprocessing.Pool()
    result_list = set([])
    for f in self.fs:
      f = os.path.join(self.base, f)
      result_list = result_list.union(procP.apply_async(SelectWord.subProcess, args=(f, self.puncs, self.wlist)).get())
    procP.close()
    procP.join()
    print(result_list)
    with codecs.open(self.outfile, 'w', 'utf-8') as fo:
      for w in list(result_list):
        print("Find word: %s"%w)
        fo.write("%s\n"%w)
        
@classmethod
def subProcess(cls, f, puncs, wlist):
    print('Processing:%s'%f)
    with codecs.open(f, 'r', 'utf-8') as fn:
      nwlist = set([])
      for line in fn:
        line = re.sub(puncs, ' ',line)
        line = line.strip().split()
        for w in line:
          if re.search('[a-za-z0-9]', w) is None and w not in wlist:
            print(w)
            nwlist.add(w)
    return nwlist
```



