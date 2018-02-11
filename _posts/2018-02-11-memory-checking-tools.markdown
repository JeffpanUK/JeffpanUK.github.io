---
layout:     post
title:      "内存问题检测的四种写法"
subtitle:   "我不是孔乙己."
date:       2018-02-11 15:58:25 +0800
author:     "Jeff"
header-img: "img/in-post/post-memory-leak.jpg"
catalog: true
tags:
    - Memory
    - LINUX
    - WINDWOS
---

**作者：Jeff Pan**

**转载请联系作者(kevinjjp@gmail.com)或在下方留言，侵权必究。**

# 四种内存检测方法

#### 1. VS2017     推荐指数：未知

(未使用过)

#### 2. sanitizer[^1]     推荐指数： ★★★★★

- 包括*address, memory, leak*等多种sanitizer检测工具

- 在使用*gcc*或者*clang*编译时，加入额外编译选项``"-fsanitize=leak"``

- *memsanitizer*和*leaksanitizer*只能够在*clang*中使用

- 能够准确检测出任何memory leak或者error

- 如果需要定位到源文件，需要指定以下环境: (否则只会定位到内存地址)

  ``export ASAN_OPTIONS=symbolize=1 ``

  ``export ASAN_SYMBOLIZER_PATH=$(which llvm-symbolizer)``

  ``export MSAN_OPTIONS=symbolize=1``

  ``export MSAN_SYMBOLIZER_PATH=$(which llvm-symbolizer)``

  ``export LSAN_OPTIONS=symbolize=1``

  ``export LSAN_SYMBOLIZER_PATH=$(which llvm-symbolizer)``

- **优点**： 定位准确， 检查全面

- **缺点**： 需要重新编译可执行文件

#### 3. DocMemory[^2]   推荐指数： ★★★☆☆ 

- windows平台下的内存检测工具
- Usage: ``docMemory.exe program.exe args``
- **优点**： 可以对任何可执行文件使用
- **缺点**： 定位不一定准确

#### 4. valgrind[^3]         推荐指数： ★★★★☆

- linux平台下的内存检测工具包含多种tool包
  - massif
    - Usage: ``valgrind --tool=massif ./target args``
    - 输出: *massif.id.out*文件, 使用``ms_print massif.id.out`` 即可打印出结果
    - 作用： 检测runtime时的内存消耗。 
    - 如果是debug版本的程序，可以直接定位到行。
  - memcheck
    - Usage: ``valgrind --tool=memcheck --leak-check=full ./target args``
    - 输出：内存泄漏、越界的代码位置
    - 作用：检测内存泄漏或者内存越界。
    - 如果是debug版本的程序，可以直接定位到行。
    - Note：*still reacheable*部分可以忽略。
    - 常见问题：
      - malloc, calloc 与free不配对提前return或者goto使用时，造成possible leak

      - free 多次同一内存free未初始化的内存

      - 如果使用了**tcmalloc**[^4] 代替原始的*malloc*, 会使得valgrind失效

- **优点**： 可以对任何可执行文件使用， 可视化图像显示内存使用

- **缺点**： 常常会有误报， 受编译环境影响较大

# 总结

工程开发中，在测试阶段，应该在debug版本中强制加入sanitizer选项，以便及时发现内存问题。 
对于用户端，应该在上线前，使用第三种检测方式确保没有内存问题。

# Reference
[^1]: https://github.com/google/sanitizers/wiki
[^2]: http://www.syschat.com/download95.html
[^3]: http://valgrind.org/docs/manual/quick-start.html
[^4]: tcmalloc相比于glibc的内存分配管理机制，效率更高，碎片更少，并且自带内存检测。使用只需要在编译时向makefile中加入-ltcmalloc即可。如果是cmake，则直接链接tcmalloc.so动态库即可。但是tcmalloc自带的内存检测功能十分有限，并且无法检测内存越界。