# coding=utf-8
"""Item30
Consider `@property` instead of refactoring attributes.
"""
import datetime
import time


class Bucket(object):
    def __init__(self, period):
        self.period_delta = datetime.timedelta(seconds=period)
        self.reset_time = datetime.datetime.now()
        self.quota = 0

    def __repr__(self):
        return "Bucket(quota=%d)" % self.quota


class Bucket2(object):
    """在Bucket的基础上，以不改变接口为前提，添加新的逻辑。"""
    def __init__(self, period):
        self.period_delta = datetime.timedelta(seconds=period)
        self.reset_time = datetime.datetime.now()
        self.max_quota = 0
        self.quota_consumed = 0

    @property
    def quota(self):
        pass

    @quota.setter
    def quota(self, amount):
        pass