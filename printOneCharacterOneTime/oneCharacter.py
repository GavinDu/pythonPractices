import time
import sys

def delay_show(str):
    for c in str:
        sys.stdout.write('%s' % c)
        sys.stdout.flush()
        time.sleep(0.25)
    print('\n')

delay_show("Hello World")