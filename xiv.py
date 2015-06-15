#!/usr/bin/python

__author__ = 'gideon'


import sys, getopt
import traceback

from actions import sort

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



if __name__ == "__main__":

    main(sys.argv[1:])


sort.read_file('/home/gideon/PycharmProjects/IBM/xiv/input', 'stam.txt')