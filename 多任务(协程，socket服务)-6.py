'''
socket编程思路
TCP服务端：
1 创建套接字，绑定套接字到本地IP与端口
   # socket.socket(socket.AF_INET,socket.SOCK_STREAM) , s.bind()
2 开始监听连接                   #s.listen()
3 进入循环，不断接受客户端的连接请求              #s.accept()
4 然后接收传来的数据，并发送给对方数据         #s.recv() , s.sendall()
5 传输完毕后，关闭套接字                     #s.close()

TCP客户端:

1 创建套接字，连接远端地址
       # socket.socket(socket.AF_INET,socket.SOCK_STREAM) , s.connect()
2 连接后发送数据和接收数据          # s.sendall(), s.recv()
3 传输完毕后，关闭套接字          #s.close()
'''
import gevent,time,socket
from gevent import monkey

monkey.patch_all()

def seversocket(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("",port))    #套接字绑定IP和端口
    sock.listen(10)         #进行TCP监听
    while True:
        conn,addr = sock.accept()  #接受TCP连接，并返回新的套接字与IP地址
        print("客户端访问中，地址：",addr,conn)
        gevent.spawn(sever_data_feedback,conn)

def sever_data_feedback(conn):
    try:
        while True:
            data = conn.recv(1024) #把接受的数据实例化

            '''
            使用使用shutdown来关闭socket的功能
            SHUT_RDWR:关闭读写,即不可以使用send/write/recv/read
            SHUT_RD:关闭读,即不可以使用recv/read
            SHUT_WR:关闭写,即不可以使用send/write
           '''
            if not data : conn.shutdown(socket.SHUT_WR)
            print("recv:",data.decode())
            conn.send(data*3) #数据返回客户端
    except Exception as ex:
        print(ex)
    finally:
        conn.close()

if __name__ == '__main__':
    seversocket(8888)
