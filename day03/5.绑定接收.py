"""
@author Chr.yl

"""
import socket

udp_bind_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_bind_socket.bind(('127.0.0.1', 8080))

# 接收
recvfrom = udp_bind_socket.recvfrom(1024)
rec_data = recvfrom[0]
ip_port = recvfrom[1]
# 解码
print(recvfrom)

udp_bind_socket.close()
