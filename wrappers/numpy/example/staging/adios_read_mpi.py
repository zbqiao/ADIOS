#!/usr/bin/env python
"""
Example:

$ python ./adios_read_mpi.py [METHOD] [params]
"""

import adios_mpi as ad
import getopt, sys
import os

method = "BP"
init = "verbose=3;"

if len(sys.argv) > 1:
    method = sys.argv[1]

if len(sys.argv) > 2:
    init = sys.argv[2]

print ">>> Method:", method, init
ad.read_init(method, parameters=init)

f = ad.file("temp.bp", method, is_stream=True, timeout_sec = 10.0)
print f

i = 0
while True:
    print ">>> step:", i
    v = f.var['temperature']
    print v

    #val = v.read(nsteps=1)
    val = v[1:2, 1:5]
    print val

    if (f.advance() < 0):
        break
    i += 1

f.close()

ad.read_finalize(method)

print ">>> Done."
