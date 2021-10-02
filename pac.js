al = JSON.parse('allowlist');
bl = JSON.parse('blocklist');

proxy = '__PROXY__';
direct = 'DIRECT;';
if (proxy == '__PRO' + 'XY__') // 压缩时会被优化掉，手动替换一下
    proxy = eval('__PRO' + 'XY__');

oho = Object.hasOwn;

function FindProxyForURL(_, host) {
    if (oho(al, host))
        return direct;

    var suffix;
    var pos = host.lastIndexOf('.');
    while (true) {
        if (pos <= 0) {
            if (oho(bl, host))
                return proxy;
            else
                return direct;
        }
        suffix = host.slice(pos + 1);
        if (oho(bl, suffix))
            return proxy;
        pos = host.lastIndexOf('.', pos - 1);
    }
};
