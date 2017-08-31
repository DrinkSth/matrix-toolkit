#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2017/8/18 上午9:31
# @Author : Matrix
# @Github : https://github.com/blackmatrix7/
# @Blog : http://www.cnblogs.com/blackmatrix/
# @File : config.py
# @Software: PyCharm
__author__ = 'blackmatrix'


class ConfigMixin:

    """
    Config混合类，支持部分dict协议，实现以类似操作dict的方式操作配置文件。
    """

    def __setattr__(self, key, value):
        raise AttributeError

    def __setitem__(self, key, value):
        raise AttributeError

    def __delitem__(self, key):
        raise AttributeError

    def __getitem__(self, item):
        return getattr(self, item)

    def __iter__(self):
        return (k for k in dir(self) if k.upper() == k)

    def __contains__(self, key):
        return hasattr(self, key)

    def items(self):
        return {k: getattr(self, k, None) for k in dir(self) if k.upper() == k}.items()

    def get(self, item, value=None):
        return getattr(self, item, value)


class BaseConfig(ConfigMixin):
    """
    配置文件基类
    """
    pass


class DefaultConfig(BaseConfig):

    """
    配置文件的具体实现，所有的配置项都必须是全部大写
    """

    # DEBUG
    DEBUG = False

    # Cache
    CACHE_MEMCACHED_SERVERS = ['127.0.0.1:11211']
    CACHE_KEY_PREFIX = ''


default = DefaultConfig()

configs = {'default': default}

# 读取配置文件的名称，在具体的应用中，可以从环境变量、命令行参数等位置获取配置文件名称
config_name = 'default'

# 对本地配置文件的支持，当项目根目录存在localconfig.py文件时
# 优先从localconfig.py中读取配置，如果不存在读取config.py的配置。
# localconfig.py 应该加入git的忽略文件
try:
    import localconfig
    current_config = localconfig.configs[config_name]
except ImportError:
    current_config = configs[config_name]
