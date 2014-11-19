#!/usr/bin/env python
"""
 replace_secret.py file

 Will replace all SECRET_KEY in a Django Settings-File with a freshly generated.

 This file by Stephan S. Hepper (hello@stephanhepper.com) only
 reassembles portions of the django-project's code 1.6.1

 Contributions goes to:

 Django Software Foundation foundation@djangoproject.com

 Licence: BSD https://github.com/django/django/blob/master/LICENSE
"""
import hashlib
import time
import os
import sys
import fileinput

import random
try:
    random = random.SystemRandom()
    using_sysrandom = True
except NotImplementedError:
    import warnings
    warnings.warn('A secure pseudo-random number generator is not available '
                  'on your system. Falling back to Mersenne Twister.')
    using_sysrandom = False

CHARS = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'


def get_random_string(length=12,
                      allowed_chars='abcdefghijklmnopqrstuvwxyz'
                                    'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'):
    """
    Returns a securely generated random string.

    The default length of 12 with the a-z, A-Z, 0-9 character set returns
    a 71-bit value. log_2((26+26+10)^12) =~ 71 bits
    """
    if not using_sysrandom:
        # This is ugly, and a hack, but it makes things better than
        # the alternative of predictability. This re-seeds the PRNG
        # using a value that is hard for an attacker to predict, every
        # time a random string is required. This may change the
        # properties of the chosen random sequence slightly, but this
        # is better than absolute predictability.
        random.seed(
            hashlib.sha256(
                ("%s%s" % (
                    random.getstate(),
                    time.time())).encode('utf-8')
            ).digest())
    return ''.join([random.choice(allowed_chars) for i in range(length)])


def generate_key(length):
    return get_random_string(length, CHARS)

if len(sys.argv) < 2:
    print "please supply a filename"
    exit(1)

filePath = sys.argv[1]

import re
rx = re.compile(r'''(\s*SECRET_KEY\s*=\s*)(["'])(.*)(\2)''')

key = generate_key(50)
for line in fileinput.input(filePath, inplace=True):
    sys.stdout.write(rx.sub(r'\g<1>\g<2>%s\g<2>'%key, line))