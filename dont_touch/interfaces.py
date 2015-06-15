__author__ = 'gideon'


import abc

class XivAction(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def start(self, input_file, output_file):
        """Receive input and define output"""
        return

