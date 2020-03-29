"""
@author Chr.yl
    发送给客户端
"""
import socket

tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 一个参数: ('ip',port)
# 绑定监听端口: tcp_socket.connect(address)
tcp_server.bind(('', 8080))
# 开启监听
# listen: 监听模式,不能发送数据,等对方先沟通,参数为允许的最大连接数,但linux无效
tcp_server.listen(128)
# 等待客户连接:开始接受客户端连接
new_client_socket, client_ip_port = tcp_server.accept()
# accept_data = tcp_server.accept()
# accept_data 有两部分
# 1.一个新的套接字 对象 accept_data[0] :new_client_socket 连接上之后,新建一个新的套接字(只对这个客户端而言),如果有其他的客户端连接,再新建一个客户端
# 2.客户端的ip地址 元组  accept_data[2]:client_ip_port 该客户端的ip port
# print(accept_data)


# 利用新建的套接字 接收 2进制 ,注意这里用新new的套接字接收数据
recv_data = new_client_socket.recv(1024)
# 解码
recv_text = recv_data.decode('utf-8')
print(recv_text)

# 利用新建的套接字发送
new_client_socket.send('你也好 哦'.encode())

# 关闭,注意这里需要关闭两个,新new的套接字也需要关闭
# 注意,新建的套接字关闭之后,就不能和客户单通信了
new_client_socket.close()
# 不再接受新的客户端
tcp_server.close()
