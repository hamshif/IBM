__author__ = 'gideon'

import sys, os, traceback

# TODO find less hacky and polluted way to import from parent dirthis was done via __init__.py
import settings

print('settings.BASE_DIR: ', settings.BASE_DIR)

from dont_touch import interfaces

print interfaces.__author__


class Sorter(interfaces.XivAction):

    def start(self, input_file, output_file):

        print "input_file: ", input_file
        print "output_file: ", output_file

        lines = self.read_file(input_file)

        self.sort_alfabet(lines, output_file)


    def read_file(self, full_name):

        try:

            _file = open(full_name)

            i = 0

            lines = []

            for line in _file:

                i += 1
                print i, ': ', line
                lines.append(line)

            return lines

        except IOError:

            print "There was an error reading, file_name: ", full_name
            print(sys.exc_info())
            traceback.print_exc()
            sys.exit()


    def sort_alfabet(self, lines, full_output_name):

        lines = sorted(lines)

        try:

            f = open(full_output_name, "w")

            for line in lines:

                print(line)
                f.write(line + '\n')

        except IOError:

            print "There was an error writing, file_name: ", full_output_name
            print(sys.exc_info())
            traceback.print_exc()
            sys.exit()


