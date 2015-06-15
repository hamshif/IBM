__author__ = 'gideon'

import sys, os, traceback

from xiv.dont_touch.interfaces import XivAction


def read_file(path, file_name):

    full_name = os.path.join(path, file_name)

    try:

        _file = open(full_name)

        i = 0

        for line in _file:

            i += 1
            print i, ': ', line

    except IOError:

        print "There was an error reading, file_name: ", full_name
        print(sys.exc_info())
        traceback.print_exc()
        sys.exit()



read_file('/home/gideon/PycharmProjects/IBM/xiv/input', 'stam.txt')


print(XivAction.start)