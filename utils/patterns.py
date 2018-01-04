# -*- coding: utf-8 -*-

__author__ = "mertsalik"
__copyright__ = "Copyright 2018"
__credits__ = ["mertsalik", ""]
__license__ = "Private"
__email__ = ""


class SingletonDecorator:
    """
    Look:
    http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html
    """

    def __init__(self, klass):
        self.klass = klass
        self.instance = None

    def __call__(self, *args, **kwds):
        if self.instance is None:
            self.instance = self.klass(*args, **kwds)
        return self.instance
