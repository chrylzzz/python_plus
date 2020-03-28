"""
@author Chr.yl

"""
import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 自动接收1024个字节 ,不发生就等待
# 接受的是一个元组:(b'接收数据的二进制',('ip',port))
# rec_data[0] :接收数据的二进制
# rec_data[1] :接收数据ip+port
rec_data = udp_socket.recvfrom(1024)
# 解码: gbk , 解码错误后执行的:ignore:解码失败忽略错误,strict:严格模式
rec_text = rec_data[0].decode(encoding="gbk", errors='ignore')
#
print(rec_text)
