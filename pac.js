var al = JSON.parse('allowlist');
var bl = JSON.parse('blocklist');

var proxy = '__PROXY__';
var direct = 'DIRECT;';
if (proxy === '__PRO' + 'XY__') // 小心压缩时被优化掉，手动替换一下
    proxy = eval('__PRO' + 'XY__');

var hop = Object.hasOwnProperty;
function FindProxyForURL(url, host) {
    if (hop.call(al, host))
        return direct;

    var suffix;
    var pos = host.lastIndexOf('.');
    pos = host.lastIndexOf('.', pos - 1);
    while (true) {
        if (pos <= 0) {
            if (hop.call(bl, host))
                return proxy;
            else
                return direct;
        }
        suffix = host.substring(pos + 1);
        if (hop.call(bl, suffix))
            return proxy;
        pos = host.lastIndexOf('.', pos - 1);
    }
}
