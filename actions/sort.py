__author__ = 'gideon'

import sys, os, traceback


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



# read_file('/home/gideon/PycharmProjects/IBM/xiv/input', 'stam.txt')


# TODO find more elegant way instead of hack import from parent directory

import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
os.sys.path.insert(0, parentdir)

import settings

print('settings.BASE_DIR: ', settings.BASE_DIR)

from dont_touch import interfaces

print interfaces.__author__


class Sorter(interfaces.XivAction):

    def start(self, input_file, output_file):

        print "input_file: ", input_file
        print "output_file: ", output_file

        _file = self.read_file(input_file)

        self.sort_alfabet(_file)


    def read_file(self, full_name):

        try:

            _file = open(full_name)

            i = 0

            for line in _file:

                i += 1
                print i, ': ', line

            return _file

        except IOError:

            print "There was an error reading, file_name: ", full_name
            print(sys.exc_info())
            traceback.print_exc()
            sys.exit()


    def sort_alfabet(_file):

        lines = []

        for line in _file:

            lines.append(line)

        lines = sorted(lines)

        for line in lines:

            print(line)
