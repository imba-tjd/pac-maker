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

## 测试方法

1. 准备好黑白名单
2. 运行Run.bat，会生成pac.txt
3. 运行test.py，会生成test.js
4. 打开node REPL，全选test.js里的东西复制粘贴。不能在VSC的终端中打开，有BUG
5. FindProxyForURL('','xxx')

## TODO

* 重写测试
* 改用Set
