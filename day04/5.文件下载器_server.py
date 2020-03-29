"""
@author Chr.yl
    使用套接字,服务端,接收客户端,注意这里server端没有移动到任何目录下,直接在本目录下下载而已
"""
import socket

tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_server.bind(('', 8080))
tcp_server.listen(128)
while True:
    new_client_socket, client_ip_port = tcp_server.accept()

    recv_data = new_client_socket.recv(1024)
    # 获取文件名
    file_name = recv_data.decode('utf-8')
    print(file_name)
    try:
        with open(file_name, 'rb') as file:
            while True:
                # 解码
                file_data = file.read(1024)
                if file_data:
                    # 利用新建的套接字发送
                    new_client_socket.send(file_data)
                else:
                    break
    except Exception as e:
        print('文件%s 下载失败' % file_name)
    else:
        print('文件%s 下载成功' % file_name)
    # 关闭,注意这里需要关闭两个,新new的套接字也需要关闭
    # 注意,新建的套接字关闭之后,就不能和客户单通信了
    new_client_socket.close()
# 不再接受新的客户端
tcp_server.close()
