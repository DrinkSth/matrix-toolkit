#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2017/8/18 上午9:50
# @Author : Matrix
# @Github : https://github.com/blackmatrix7/
# @Blog : http://www.cnblogs.com/blackmatrix/
# @File : retry.py
# @Software: PyCharm
from time import sleep
from functools import wraps

__author__ = 'blackmatrix'


"""
在函数执行出现异常时自动重试的简单装饰器
"""


def retry(max_retries: int =5, delay: int =0, step: int =0, exceptions: tuple =BaseException, sleep_func=sleep, callback=None):
    """
    函数执行出现异常时自动重试的简单装饰器。
    :param max_retries:  最多重试次数。
    :param delay:  每次重试的延迟，单位秒。
    :param step:  每次重试后延迟递增，单位秒。
    :param exceptions:  触发重试的异常类型，单个异常直接传入异常类型，多个异常以tuple或list传入。
    :param sleep_func:  实现延迟的方法，默认为time.sleep。
    在一些异步框架，如tornado中，使用time.sleep会导致阻塞，可以传入自定义的方法来实现延迟。
    自定义方法函数签名应与time.sleep相同，接收一个参数，为延迟执行的时间。
    :param callback: 回调函数，函数签名应接收一个参数，每次出现异常时，会将异常对象传入。
    可用于记录异常日志，中断重试等。
    如回调函数正常执行，并返回True，则终止重试，并将被装饰函数的异常冒泡抛出。
    如回调函数正常执行，没有返回值或返回除True以外的结果，则继续重试。
    如回调函数抛出异常，则终止重试，并将回调函数的异常冒泡抛出。
    :return: 被装饰函数的执行结果。
    """
    def wrapper(func):
        @wraps(func)
        def _wrapper(*args, **kwargs):
            nonlocal delay, step, max_retries, exceptions
            func_ex = RuntimeError
            while max_retries > 0:
                try:
                    return func(*args, **kwargs)
                except exceptions as ex:
                    if callable(callback) and callback(ex) is True:
                        raise ex
                    func_ex = ex
                finally:
                    max_retries -= 1
                    if delay > 0 or step > 0:
                        sleep_func(delay)
                        delay += step
            else:
                raise func_ex
        return _wrapper
    return wrapper


if __name__ == '__main__':
    pass
