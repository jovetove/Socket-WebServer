import socket
import threading

from StrategyFactory import StrategyFactory


class WSGIServer(object):
    """提供socket服务 和 并发支持"""

    def __init__(self, server_address):
        """初始化socket"""
        # 创建一个tcp套接字
        self.listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 允许立即使用上次绑定的port,.SO_REUSEADDR 设置 当socket关闭后，本地端用于该socket的端口号立刻就可以被重用。
        self.listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 绑定
        self.listen_socket.bind(server_address)
        # 变为被动，并制定队列的长度
        self.listen_socket.listen(128)

    def serve_forever(self):
        """循环运行web服务器，等待客户端的链接并为客户端服务"""
        while True:
            # 等待新客户端到来
            client_socket, client_address = self.listen_socket.accept()
            print("src_ip: ", client_address, end="\n")
            new_process = threading.Thread(target=self.handleRequest, args=(client_socket,))
            new_process.start()

            # 因为线程是共享同一个套接字，所以主线程不能关闭，否则子线程就不能再使用这个套接字了
            # client_socket.close()

    def handleRequest(self, client_socket):
        """ 用一个新的进程，为一个客户端进行服务 """
        recv_data = client_socket.recv(1024).decode('utf-8')

        requestHeaderLines = recv_data.splitlines()
        for line in requestHeaderLines:
            print(line)

        method = requestHeaderLines[0][0:3]  # 获得请求行方法参数 GET POST ...
        strategy = StrategyFactory.choice_mothod(method)  # 选择策略方法
        response_header, response_body = strategy.do_some_business_logic(requestHeaderLines)

        client_socket.send(response_header.encode('utf-8'))
        client_socket.send(response_body)
        client_socket.close()