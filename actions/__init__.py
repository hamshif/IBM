__author__ = 'gideon'


import os
# TODO find more elegant way instead of hack import from parent directory

import inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
os.sys.path.insert(0, parent_dir)

print "visited __init__"

#
#
# for v in os.environ:
#
#     print v

