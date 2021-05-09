"""
client端
"""
import socket
from AES import *

# 创建套接字
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定端口
tcp_client_socket.bind(("", 22000))
# 连接ip地址和端口
try:
    tcp_client_socket.connect(("127.0.0.1", 8080))
except:
    print("服务器 1 连接失败！")
    print("已连接备份服务器！")
    tcp_client_socket.connect(("127.0.0.1", 9090))
file_name = input("请输入要下载的文件：")
# 文件名编码
tcp_client_socket.send(file_name.encode())
try:
    with open("./" + file_name, "w+",encoding='utf-8') as file:
        while True:
            # 接受数据
            file_data = decrypt(key,iv,tcp_client_socket.recv(4096))
            # file_data = tcp_client_socket.recv(4096)
            # 数据长度不为0写入文件
            if file_data:
                file.write(file_data)
            else:
                break
except Exception as e:
    print("下载异常", e)
else:
    print(file_name, "下载成功！")
tcp_client_socket.close()
