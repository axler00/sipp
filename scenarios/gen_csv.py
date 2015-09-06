# -*- coding: utf-8 -*-

import sys
from sys import argv

user_num = 5000

if __name__ == '__main__':
    if len(argv) != 2:
        print 'Usage: %s uac|uas' % (argv[0])
        sys.exit(0)

    fn = argv[1] + '.csv'
    with open(fn, 'w') as f:
        f.write("SEQUENTIAL\n")
        if argv[1] == 'uac':
            for i in xrange(1, user_num):
                f.write("test%d;[authentication username=test%d password=test1234];test%d\n" % (i, i, user_num-i))
        else:
            for i in xrange(user_num-1, 0, -1):
                f.write("test%d;[authentication username=test%d password=test1234];test%d\n" % (i, i, user_num-i))
