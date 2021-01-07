from pac_maker import *
import json
import os
from os.path import exists
import sys
import subprocess

# test readfromfile
testlist_content = '''
# comment
a.com # comment
b.org
'''

with open('testlist.txt', 'w+') as f:
    f.write(testlist_content)

testlist_readed = list(readfromfile('testlist.txt'))
assert testlist_readed == ['a.com', 'b.org']


# test domainlist_to_jsonobjstr
testlist_jsonobj = json.loads(domainlist_to_jsonobjstr(testlist_readed))
assert len(testlist_jsonobj) == 2
assert 'a.com' in testlist_jsonobj
assert 'b.org' in testlist_jsonobj


# test js syntax
if not exists('pac.txt'):
    if exists('allowlist.txt') and exists('blocklist.txt'):
        pass
    elif not(exists('allowlist.txt') and exists('blocklist.txt')):
        os.rename('testlist.txt', 'blocklist.txt')
        with open('allowlist.txt', 'w+'):
            pass
    else:
        sys.exit()

    from pac_maker import _main
    _main() # Generate pac.txt

with open('pac.txt') as f:
    pactxt = f.read()
pactxt = pactxt.replace('__PROXY__', 'PROXY;')
with open('test.js', 'w+') as f:
    f.write(pactxt)

try:
    subprocess.run(['node', 'test.js'], check=True)
except OSError:  # nodejs isn't installed
    pass
