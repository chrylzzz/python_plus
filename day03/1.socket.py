"""
@author Chr.yl
 发送数据
"""
import socket

# 创建套接字
# socket.socket(协议类型,传输方式)
# socket.AF_INET ipv4
# socket.AF_INET6 ipv6
# socket.SOCK_DGRAM udp
# socket.SOCK_STREAM tcp
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 数据传输 :二进制数据
udp_socket.sendto('hello'.encode(), {'192,168.87.127', 9090})
# 关闭
udp_socket.close()
