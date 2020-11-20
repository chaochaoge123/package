#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/19 14:23
# @Author  : qqc
# @File    : q_num.py
# @Software: PyCharm


class NumOpt(object):
    def __init__(self, num_list):
        self.num_list = num_list

    def check_params_type(self):
        if not isinstance(self.num_list, list):
            raise Exception("参数类型错误")

    @property
    def add(self):
        self.check_params_type()
        total = 0
        for i in self.num_list:
            total += i
        return total

    @property
    def subtraction(self):
        self.check_params_type()
        if len(self.num_list) != 2:
            raise Exception("格式错误")
        return self.num_list[0] - self.num_list[1]
