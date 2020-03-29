"""
@author Chr.yl
    使用套接字,客户端
"""
import socket

tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接
tcp_client.connect(('127.0.0.1', 8080))
file_name = input('请输入要下载的文件名:\n')
# 发送文件名
tcp_client.send(file_name.encode())
with open('/Users/chryl/upload/20200329/' + file_name, 'wb') as file:
    while True:
        file_data = tcp_client.recv(1024)
        # 判断是否传输完成
        if file_data:
            file.write(file_data)
        else:
            break

tcp_client.close()
