from pac_maker import striplines, domainlist_to_jsonobjstr
import json
import os
import subprocess
import tempfile


def striplines_test():
    lines = '''
    # comment
    a.com   # zxcv
    b.org
    # asdf
    '''.splitlines()

    lines_stripped = list(striplines(lines))
    assert lines_stripped == ['a.com', 'b.org']


def domainlist_to_jsonobjstr_test():
    domainlist = ['a.com', 'b.org']
    jsonobjstr = domainlist_to_jsonobjstr(domainlist)

    jsonobj = json.loads(jsonobjstr)
    assert len(jsonobj) == 2
    assert 'a.com' in jsonobj
    assert 'b.org' in jsonobj


def pactxt_syntax_test():
    if not os.path.exists('pac.txt'):
        print('pac.txt not found. Skip syntax test.')
        return

    with open('pac.txt') as f:
        pactxt = f.read()
    pactxt = pactxt.replace('__PROXY__', 'PROXY;')

    tempf = tempfile.NamedTemporaryFile()
    tempf.write(pactxt.encode())
    tempf.flush()

    try:
        subprocess.run(['node', tempf.name], check=True)
    except OSError:
        print('nodejs is not installed. Skip syntax test.')

if __name__ == '__main__':
    striplines_test()
    domainlist_to_jsonobjstr_test()
    pactxt_syntax_test()
