a = JSON.parse('allowlist')
b = JSON.parse('blocklist')

p = '__PROXY__'
d = 'DIRECT;'
if (p == '__PRO' + 'XY__') // 压缩时会被优化掉，手动替换一下
    p = eval('__PRO' + 'XY__')

h = Object.hasOwn;

function FindProxyForURL(_, host) {
    if (h(a, host))
        return d

    var suffix
    var pos = host.lastIndexOf('.')
    while (true) {
        if (pos <= 0) {
            if (h(b, host))
                return p
            else
                return d
        }
        suffix = host.slice(pos + 1);
        if (h(b, suffix))
            return p
        pos = host.lastIndexOf('.', pos - 1)
    }
}
