"""
@author Chr.yl
    udp绑定发送

"""
import socket

udp_bind_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 端口绑定 address:元组
udp_bind_socket.bind(('127.0.0.1', 8888))
# 发送
udp_bind_socket.sendto('hello'.encode(), ('127.0.0.1', 8080))
# 关闭
udp_bind_socket.close()
