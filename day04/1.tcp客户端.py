"""
@author Chr.yl
    tcp接收服务端
"""
import socket

tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 一个参数: ('ip',port)
# 主动连接:tcp_socket.connect(address)
tcp_client.connect(('127.0.0.1', 8080))
# sendto 是udp的发送方式
tcp_client.send('你好'.encode())
# 接收 2进制
recv = tcp_client.recv(1024)
# 解码
recv_txt = recv.decode('utf-8')
print(recv_txt)

tcp_client.close()
