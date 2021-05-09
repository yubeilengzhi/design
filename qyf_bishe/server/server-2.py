"""
服务器 2
"""
import socket
import AES

iv = AES.iv
key = AES.key
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server_socket.bind(("", 9090))
tcp_server_socket.listen(128)
while True:
    client_socket, client_ip = tcp_server_socket.accept()
    print("客户端：", client_ip, "已连接!")
    file_name_data = client_socket.recv(4096)
    file_name = file_name_data.decode()
    try:
        with open("./" + file_name, "r+",encoding='utf-8') as file:
            file_data = AES.encrypt(key,iv,file.read(4096))
            if file_data:
                client_socket.send(file_data)
            else:
                print(file_name, "传输成功")
                break
    except Exception as e:
        print("传输异常：", e)
    client_socket.close()
