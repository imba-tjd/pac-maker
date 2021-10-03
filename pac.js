al = JSON.parse('allowlist')
bl = JSON.parse('blocklist')

proxy = '__PROXY__'
direct = 'DIRECT;'
if (proxy == '__PRO' + 'XY__') // 压缩时会被优化掉，手动替换一下
    proxy = eval('__PRO' + 'XY__')

hop = Object.hasOwnProperty;

function FindProxyForURL(_, host) {
    if (hop.call(al, host))
        return direct

    var suffix
    var pos = host.lastIndexOf('.')
    while (true) {
        if (pos <= 0) {
            if (hop.call(bl, host))
                return proxy
            else
                return direct
        }
        suffix = host.slice(pos + 1);
        if (hop.call(bl, suffix))
            return proxy
        pos = host.lastIndexOf('.', pos - 1)
    }
}
