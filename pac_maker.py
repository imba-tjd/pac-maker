import sys
import shutil
import os
from typing import Iterable


pacjsminified = """\
a=JSON.parse('allowlist')
b=JSON.parse('blocklist')
p="__PROXY__",d="DIRECT;",p=="__PRO"+"XY__"&&(p=eval("__PRO"+"XY__")),h=Object.hasOwn;function FindProxyForURL(i,r){if(h(a,r))return d;for(var e,l=r.lastIndexOf(".");;){if(l<=0)return h(b,r)?p:d;if(e=r.slice(l+1),h(b,e))return p;l=r.lastIndexOf(".",l-1)}}"""


def readfile(filename: str):
    with open(filename, encoding='u8') as f:
        yield from f


def striplines(lines: Iterable[str]):
    for line in lines:
        if (hashndx := line.find('#')) != -1:
            line = line[:hashndx]
        if line := line.strip():
            yield line


def depart_rule(lines: Iterable[str]):
    '''when al and bl are in the same file, they can't be consumed simultaneously. So they must be cached.'''
    al, bl = [], []
    for line in lines:
        if line.startswith('@'):
            al.append(line[1:])
        else:
            bl.append(line)
    return al, bl


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
        print('There is no argument.', file=sys.stderr)
        sys.exit(1)

    rule = striplines(readfile('rule.txt'))
    pac_content = make_pac_content(*depart_rule(rule))

    if os.path.isfile('pac.txt'):
        shutil.copy2('pac.txt', 'pac.txt.bak')

    with open('pac.txt', 'w+') as f:
        f.write(pac_content)


if __name__ == "__main__":
    _main()
