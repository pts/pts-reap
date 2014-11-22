#! /usr/bin/python

"""Example program which ignores some signals."""

import time
import signal
import sys

def handler(signum, frame):
  print 'SLEEP SIG', signum

signal.signal(signal.SIGINT, handler)
signal.signal(signal.SIGQUIT, handler)
if len(sys.argv) > 1:
  signal.signal(signal.SIGTERM, handler)

delta = 5
target = time.time() + delta
tosleep = delta + 0.
while tosleep > 0:
  print 'SLEEP(%r)' % tosleep
  time.sleep(tosleep)
  tosleep = target - time.time()
print 'SLEEP DONE'
