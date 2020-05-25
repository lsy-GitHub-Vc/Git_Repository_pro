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

def client_side(PORT):
    HOST = 'localhost' #本地 或者localhost
    #PORT = 8888 #服务端端口
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)    #定义socket类型，网络通信，TCP
    client.connect((HOST,PORT))  #连接
    try:
        while True:
            for i in range(20):
                client.send()
                data = client.recv(1024)

                print("返回的数据：",repr(data))
            client.close()
    except Exception as ex:
        print(ex)

    finally:
        client.close()

if __name__ == '__main__':
    client_side(8888)