#!/usr/bin/python

__author__ = 'gideon'


import sys, getopt, importlib
import traceback

# import actions

args = sys.argv


for a in args:

    print("argument " + a)

print ''

def main(argv):

    input_file = ''
    output_file = ''
    action = ''

    try:

        opts, args = getopt.getopt(argv, "hi:o:a:", ["ifile=", "ofile=", "action="])

    except getopt.GetoptError:

        print 'test.py -i <input_file> -o <output_file> -a <action>'
        print(sys.exc_info())
        traceback.print_exc()
        sys.exit(2)

    for opt, arg in opts:

        if opt == '-h':

            print 'test.py -i <input_file> -o <output_file> -a <action>'
            sys.exit()

        elif opt in ("-i", "--ifile"):

            input_file = arg

        elif opt in ("-o", "--ofile"):

            output_file = arg

        elif opt in ("-a", "--action"):

            action = arg

    print 'Input file is: ', input_file
    print 'Output file is: ', output_file
    print 'Action is: ', action

    try:

        importlib.import_module('actions.' + action)
        # module = __import__(action)
        # my_class = getattr(module, class_name)
        # instance = my_class()

    except getopt.GetoptError:

        print "couldn't import ", action
        print "please create your script and place it in the actions dir of this project"
        print(sys.exc_info())
        traceback.print_exc()
        sys.exit(2)


if __name__ == "__main__":

    main(sys.argv[1:])

