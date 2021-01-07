import sys
import shutil
import os
from typing import Iterable


pacjsminified = """\
var al=JSON.parse('allowlist');
var bl=JSON.parse('blocklist');
var proxy="__PROXY__",direct="DIRECT;";"__PROXY__"===proxy&&(proxy=eval("__PRO'+'XY__"));var hop=Object.hasOwnProperty;function FindProxyForURL(r,o){if(hop.call(al,o))return direct;var l,t=o.lastIndexOf(".");for(t=o.lastIndexOf(".",t-1);;){if(t<=0)return hop.call(bl,o)?proxy:direct;if(l=o.substring(t+1),hop.call(bl,l))return proxy;t=o.lastIndexOf(".",t-1)}}"""


# 从文件中读取并去掉空行和注释
def readfromfile(filename: str):
    with open(filename, encoding='u8') as f:
        for line in f:
            if (hashndx := line.find('#')) != -1:
                line = line[:hashndx]
            if line := line.strip():
                yield line


def domainlist_to_jsonobjstr(lst: Iterable[str]):
    return "{%s}" % ','.join(
        f'"{domain}":null' for domain in lst
    )


def make_pac_content(altxt: Iterable[str], bltxt: Iterable[str]):
    al = domainlist_to_jsonobjstr(altxt)
    bl = domainlist_to_jsonobjstr(bltxt)
    return pacjsminified.replace('allowlist', al, 1).replace('blocklist', bl, 1)


def _main():
    if len(sys.argv) > 1:
        print('There is no argument.')
        sys.exit(1)

    altxt = readfromfile('allowlist.txt')
    bltxt = readfromfile('blocklist.txt')
    pac_content = make_pac_content(altxt, bltxt)

    if os.path.exists('pac.txt'):
        shutil.copy2('pac.txt', 'pac.txt.bak')

    with open('pac.txt', 'w+') as f:
        f.write(pac_content)


if __name__ == "__main__":
    _main()
