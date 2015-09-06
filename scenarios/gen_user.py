# -*- coding: utf-8 -*-

import os

if __name__ == '__main__':
    for i in xrange(5000):
        os.system("kamctl add test%d test1234" % i)
