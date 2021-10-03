# Pac Maker

A simple suffix domain matching pac.txt generator. Use it if you want to control the proxy list by your own at the domain level.

## Usage

1. Create and edit `blocklist.txt` and `allowlist.txt`. One domain for a line. comments(`#`) are supported.
2. Run `Run.bat`.
3. Create symbol link for your proxy tool, e.g. `mklink` in CMD.

## Remarks

* `null` seems to be faster than `undefined`
* `JSON.parse` seems to be faster than literal object
* Inspired by the pac.txt from ssr
* `Object.hasOwn` is too new. It only works with FF >= 92 and Chrome >= 93

## 如何测试FindProxyForURL

1. 打开浏览器F12的Console
2. 输入`__PROXY__='PROXY;'`
3. 复制pac.txt里的内容输入
4. `FindProxyForURL('','xxx')`

## TODO

* 改用Set？但初始化列表一次，传进Set又一次，不知道效率如何
