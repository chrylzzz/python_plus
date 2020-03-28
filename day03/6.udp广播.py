"""
@author Chr.yl
    广播的意思就是:发送网络号 192.168.150 下的主机都会收到信息
"""
import socket

#                               ipv4            udp
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# PermissionError: [Errno 13] Permission denied
# 设置广播权限,套接字默认不允许发送广播,需要开启权限
# udp_socket.setsockopt(套接字,那个属性,属性值)
# SOL_SOCKET  当前socket
# SO_BROADCAST 广播类型
udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)

udp_socket.sendto('hhah~'.encode(), ('255.255.255.255', 8080))

udp_socket.close()
