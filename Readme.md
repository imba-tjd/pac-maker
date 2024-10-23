# Pac Maker

A suffix domain matching pac.txt generator. Use it if you want to control the proxy list by your own at the domain level.

Inspired by the pac.txt from ssr.

## Usage

1. Create and edit `rule.txt`.
  * One domain for a line
  * Use `@` for allowed domain. It must be exact match, i.e. no suffix matching.
  * Comments(`#`) are supported
2. Run `Run.bat`.
3. Create symbol link for your proxy tool, e.g. `mklink` in CMD.

## Implementation remarks

* `null` seems to be faster than `undefined`
* `JSON.parse` seems to be faster than literal object
* `Object.hasOwn` requires FF >= 92 and Chrome >= 93

### 如何测试FindProxyForURL

1. 打开浏览器F12的Console
2. 输入`__PROXY__='PROXY;'`
3. 复制pac.txt里的内容输入
4. `FindProxyForURL('','xxx')`

## TODO

* 改用Set？但初始化列表一次，传进Set又一次，不知道效率如何

## Resources

* https://developer.mozilla.org/en-US/docs/Web/HTTP/Proxy_servers_and_tunneling/Proxy_Auto-Configuration_PAC_file
* https://learn.microsoft.com/previous-versions/troubleshoot/browsers/connectivity-navigation/optimize-pac-performance
* https://findproxyforurl.com/pac-functions/
