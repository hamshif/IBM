__author__ = 'gideon'

import os

# TODO find a better way to use parent directories
import inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
os.sys.path.remove(parent_dir)


print "visited __termin__"
#
#
#
# for v in os.environ:
#
#     print v