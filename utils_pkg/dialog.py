"""Dramatic and cinematic dialog printing."""

import time

def say(msg = None, rate = 20, debug = False):
    """Say a string and wait based on length."""

    # string type check
    if not isinstance(msg, str):
        print(f'ERROR: "{msg}" is not a string.')
        return

    # string content check
    if msg is None or len(msg) < 1:
        print('ERROR: No string to print.')
        return

    # print newline and string regardless of rate
    print('\n' + msg)

    # rate type check
    if not isinstance(rate, int) and rate >= 1:
        print(f'ERROR: "{rate}" not an integer 1 or greater.')
        return

    # minimum rate check
    rate = min(rate, len(msg))

    time.sleep(msg/rate) # do the waiting

    if debug:
        print('DEBUG: Paused for', len(msg)/rate, 'seconds')

    return
