import asyncio
@asyncio.coroutine
def a(host):
    conn = asyncio.open_connection(host,80)
    reader,write = yield from conn
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    write.write(header.encode('utf-8'))
    yield from write.drain()
    while True:
        lin = yield from reader.readline()
        if lin == b'\r\n':
            break
        print('%s header > %s' % (host, lin.decode('utf-8').rstrip()))
    write.close()

loop = asyncio.get_event_loop()
task = [a(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_unit_complete(asyncio.wait(task))
loop.close()