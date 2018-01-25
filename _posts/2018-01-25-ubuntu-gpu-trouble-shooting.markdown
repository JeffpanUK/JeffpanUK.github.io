---
layout:     post
title:      "Ubuntu中使用gpu遇到的问题"
subtitle:   "GPU makes life easier, while Unix does not."
date:       2017-12-15 16:49:36
author:     "Jeff"
header-img: "img/in-post/post-gpu-linux.jpg"
catalog: true
tags:
    - LINUX
    - GPU
    - CUDA
---

**作者：Jeff Pan**

**转载请联系作者(kevinjjp@gmail.com)或在下方留言，侵权必究。**

=======================================================================================

##### Q1: Ubuntu中使用nvidia-smi命令查看GPU状态时，永远有一个GPU使用率为99%

##### A1: 

这个占用率其实是nvidia-smi对gpu状态进行采样时的瞬间的使用率。 可以通过打开persistence mode来解决这个问题。并且可以使nvidia-smi命令运行时间大幅度缩短。

`nvidia-smi -i <target gpu> -pm ENABLED`

但是这在我的使用中，会在N次运行GPU后，出现core dump的错误。 关闭后则无问题。

-----------------------------------------------------------------------------------------------------------------------------------------------------------

##### Q2: CUDA开启或者关闭error correcting code (ECC)

#####A2:

ECC(error correcting code,  错误检查和纠正)能够提高数据的正确性，随之而来的是可用内存的减少和性能上的损失。对于Tesla系列伺服器该功能默认开启。

通过命令 `nvidia-smi -i n`

可查看第n个个显卡的简要信息（详细信息可通过 nvidia-smi -q -i 0获取），其中有一项是volatile Uncorr. ECC, 可通过该选项查看当前配置。

通过 `nvidia-smi -i n -e 0/1` 可关闭(0)/开启(1)第n号GPU的ECC模式。

通过实践，关闭ECC程序的性能能得到13%~15%的提升



[1]http://docs.nvidia.com/deploy/driver-persistence/index.html#persistence-mode

[2]https://devtalk.nvidia.com/default/topic/539632/k20-with-high-utilization-but-no-compute-processes-/

[3]https://tlanyan.me/cuda-enable-disable-ecc/