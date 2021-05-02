# Pac Maker

* Generate `pac.txt` from `blocklist.txt` and `allowlist.txt`
* The pattern is simply suffix matching. `pac.js` is the logic. Minified by https://javascript-minifier.com
* List file contains one domain for a line, supporting comments(`#`)
* `null` seems to be faster than `undefined`; `JSON.parse` seems to be faster than directly define an object
* Inspired by the pac.txt from ssr

## 测试方法

1. 准备好黑白名单
2. 运行Run.bat，会生成pac.txt
3. 运行test.py，会生成test.js
4. 打开node REPL，全选test.js里的东西复制粘贴。不能在VSC的终端中打开，有BUG
5. FindProxyForURL('','xxx')
