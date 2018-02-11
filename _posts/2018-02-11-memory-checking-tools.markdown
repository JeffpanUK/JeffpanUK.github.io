---
layout:     post
title:      "对程序内存问题的检测方法"
subtitle:   "Fight against memory error."
date:       2018-02-11 14:07:00
author:     "Jeff"
header-img: "img/in-post/post-memory-leak.png"
catalog: true
tags:
    - Memory
    - LINUX
    - WINDWOS
---

**作者：Jeff Pan**

**转载请联系作者(kevinjjp@gmail.com)或在下方留言，侵权必究。**

=======================================================================================

#四种内存检测方法

#### 1. 微软大法：VS2017

(未使用过)

#### 2. 编译时：sanitizer 		推荐指数： ★★★★★

- 包括*address, memory, leak*等多种sanitizer检测工具

- 在使用*gcc*或者*clang*中加入选项即可 ``"-fsanitize=leak"``

- *memsanitizer*和*leaksanitizer*只能够在*clang*中使用

- 能够准确检测出任何memory leak或者error

- 如果需要定位到源文件，需要指定以下环境: (否则只会定位到内存地址)

  ``export ASAN_OPTIONS=symbolize=1 ``

  ``export ASAN_SYMBOLIZER_PATH=$(which llvm-symbolizer)``

  ``export MSAN_OPTIONS=symbolize=1``

   ``export MSAN_SYMBOLIZER_PATH=$(which llvm-symbolizer)``

  ``export LSAN_OPTIONS=symbolize=1``

  ``export LSAN_SYMBOLIZER_PATH=$(which llvm-symbolizer)``

#### 3. 编译后：DocMemory & valgrindD 

- **DocMemory** 		推荐指数： ★★★☆☆
  - windows平台下的内存检测工具
  - Usage: docMemory.exe program.exe args
  - 定位不一定准确
- **valgrind**  		        推荐指数： ★★★★☆
  - linux平台下的内存检测工具包含多种tool包
    - massif
      - Usage: valgrind --tool=massif ./target args
      - 输出: massif.id.out文件, 使用ms_print massif.id.out 即可打印出结果
      - 作用： 检测runtime时的内存消耗。 
      - 如果是debug版本的程序，可以直接定位到行。
    - memcheck
      - Usage: valgrind --tool=memcheck --leak-check=full ./target args
      - 输出：内存泄漏、越界的代码位置
      - 作用：检测内存泄漏或者内存越界。
      - 如果是debug版本的程序，可以直接定位到行。
      - Note：still reacheable可以忽略。
      - 常见问题：
        - malloc, calloc 与free不配对提前return或者goto使用时，造成possible leak
        - free 多次同一内存free未初始化的内存

# 总结

工程开发中，在测试阶段，应该在debug版本中强制加入sanitizer选项，以便及时发现内存问题。 

对于用户端，应该在上线前，使用第三种检测方式确保没有内存问题。