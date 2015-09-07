#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2015 Doug Hellmann.  All rights reserved.
#
"""ChainMap as a namespace stack
"""
#end_pymotw_header

import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}
c = {'c': 'E'}

m1 = collections.ChainMap(a, b)
m2 = m1.new_child(c)

print('m1["c"] = %s' % m1['c'])
print('m2["c"] = %s' % m2['c'])