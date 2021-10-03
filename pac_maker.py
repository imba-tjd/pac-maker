import sys
import shutil
import os
from typing import Iterable


pacjsminified = """\
al=JSON.parse('allowlist')
bl=JSON.parse('blocklist')
proxy="__PROXY__",direct="DIRECT;",proxy=="__PRO"+"XY__"&&(proxy=eval("__PRO"+"XY__")),hop=Object.hasOwnProperty;function FindProxyForURL(i,r){if(hop.call(al,r))return direct;for(var e,l=r.lastIndexOf(".");;){if(l<=0)return hop.call(bl,r)?proxy:direct;if(e=r.slice(l+1),hop.call(bl,e))return proxy;l=r.lastIndexOf(".",l-1)}}"""


def readfile(filename: str):
    with open(filename, encoding='u8') as f:
        for line in f:
            yield line


def striplines(lines: Iterable[str]):
    for line in lines:
        if (hashndx := line.find('#')) != -1:
            line = line[:hashndx]
        if line := line.strip():
            yield line


def domainlist_to_jsonobjstr(lst: Iterable[str]):
    '''['a','b'] -> '{"a":null,"b":null}' '''
    return "{%s}" % ','.join(
        f'"{domain}":null' for domain in lst
    )


def make_pac_content(altxt: Iterable[str], bltxt: Iterable[str]):
    al = domainlist_to_jsonobjstr(altxt)
    bl = domainlist_to_jsonobjstr(bltxt)
    return pacjsminified.replace('allowlist', al).replace('blocklist', bl)


def _main():
    if len(sys.argv) > 1:
        print('There is no argument.')
        sys.exit(1)

    altxt = striplines(readfile('allowlist.txt'))
    bltxt = striplines(readfile('blocklist.txt'))
    pac_content = make_pac_content(altxt, bltxt)

    if os.path.exists('pac.txt'):
        shutil.copy2('pac.txt', 'pac.txt.bak')

    with open('pac.txt', 'w+') as f:
        f.write(pac_content)


if __name__ == "__main__":
    _main()
