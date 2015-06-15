#!/usr/bin/python
import os

__author__ = 'gideon'


import sys, getopt, importlib
import traceback


import settings

from dont_touch.interfaces import XivAction

HELP_MESSAGE = 'test.py -i <input_file> -o <output_file> -a <action> -c <class_name>'


args = sys.argv


for a in args:

    print("argument " + a)

print ''



def main(argv):

    input_file = ''
    output_file = ''
    action = ''
    class_name = ''

    try:

        opts, args = getopt.getopt(argv, "hi:o:a:c:", ["ifile=", "ofile=", "action=", "class_name"])

    except getopt.GetoptError:

        print "slick: ", HELP_MESSAGE
        print(sys.exc_info())
        traceback.print_exc()
        sys.exit(2)

    for opt, arg in opts:

        if opt == '-h':

            print HELP_MESSAGE
            sys.exit()

        elif opt in ("-i", "--ifile"):

            input_file = arg

        elif opt in ("-o", "--ofile"):

            output_file = arg

        elif opt in ("-a", "--action"):

            action = arg

        elif opt in ("-c", "--class_name"):

            class_name = arg

    print 'Input file is: ', input_file
    print 'Output file is: ', output_file
    print 'Action is: ', action
    print 'Class name is: ', class_name

    try:

        module = importlib.import_module('actions.' + action)
        # module = __import__(action)
        # my_class = getattr(module, class_name)
        # instance = my_class()

        if class_name == '':

            class_name = settings.installed_actions[action]


        my_class = getattr(module, class_name)
        instance = my_class()
        instance.start(os.path.join(settings.INPUT_DIR, input_file), output_file)

    except getopt.GetoptError:

        print "couldn't import ", action
        print "please create your script and place it in the actions dir of this project"
        print(sys.exc_info())
        traceback.print_exc()
        sys.exit(2)

    except KeyError:

        print "couldn't find a class name to fit ", action
        print "please add a class_name argument"
        print HELP_MESSAGE
        print(sys.exc_info())
        traceback.print_exc()
        sys.exit(2)

if __name__ == "__main__":

    main(sys.argv[1:])


