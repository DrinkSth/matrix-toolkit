# Matirx Tookit
## 项目说明

一些方便日常使用的小工具，以及在工作中制造过的轮子。

## 工具列表

#### config

实现部分dict协议的配置操作混合类（Mixin），简化配置文件的读取与继承。

#### cache

基于Python3-memcached的浅封装，支持在key之前加入统一的前缀，提供两个函数装饰器：cached() 用于缓存函数执行结果， delcache()用于在函数执行完成后清理缓存。