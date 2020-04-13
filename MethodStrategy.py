# coding=utf-8
import re

# 设置服务器服务静态资源时的路径
from Config import read_cfg
from Response_header import Response_header

cfg = read_cfg()

DOCUMENTS_ROOT = cfg.get("FILE", "DOCUMENTS_ROOT")
IMG_PATH = cfg.get("FILE", "IMG_PATH")
STATIC_PATH = cfg.get("FILE", "STATIC_PATH")
MAIN_FILE = cfg.get("FILE", "MAIN_FILE")  # 主页

class MethodStrategy(object):
    """抽象策略类"""

    def MethodInterface(self, requestHeaderLines):
        raise NotImplementedError()


class Context(object):
    def __init__(self, strategy: MethodStrategy) -> None:
        self._strategy = strategy

    def strategy(self) -> MethodStrategy:
        return self._strategy

    def strategy(self, strategy: MethodStrategy) -> None:
        self._strategy = strategy

    def do_some_business_logic(self, requestHeaderLines: list) -> tuple:
        return self._strategy.MethodInterface(requestHeaderLines)


class POST(MethodStrategy):
    def MethodInterface(self, requestHeaderLines):
        print("this POST")
        response_header = None
        response_body = None
        return response_header, response_body


class GET(MethodStrategy):
    def MethodInterface(self, requestHeaderLines):
        request_line = requestHeaderLines[0]  # 请求行 GET /index.html HTTP/1.1
        get_file_name = re.match("[^/]+(/[^ ]*)", request_line).group(1)  # 获取文件名字

        print("file name is ===>%s" % get_file_name)  # for test

        postfix = get_file_name.split('.')[-1]  # 获取文件名后缀

        if get_file_name == '/' or not Filetype.is_binary_flow(postfix):  # 判断是否为文本文件
            response_header, response_body = Filetype.read_charactor_flow(get_file_name)
        elif Filetype.is_binary_flow(postfix):  # 二进制文件
            response_header, response_body = Filetype.read_binary_flow(get_file_name)
        else:
            response_header, response_body = (Response_header().choice(False), None)
        return response_header, response_body


class Filetype(object):
    _charactor_flow = ('html', 'js', 'css')
    _binary_flow = ('png', 'jpg', 'jpeg')

    @staticmethod
    def read_charactor_flow(filename: str) -> tuple:  # /index.html
        """
        读取响应文件内容
        :param filename: 文件路径
        :return: 响应头 和 响应体
        """
        # 先判断是否为根文件
        if filename == "/":
            get_file_name = DOCUMENTS_ROOT + MAIN_FILE
        # 再判断是否为 html 文件
        elif filename.split('.')[-1] == 'html':
            get_file_name = DOCUMENTS_ROOT + filename
        else:  # 如果不是html文件

            #files_name = os.listdir(DOCUMENTS_ROOT + STATIC_PATH) # 获取当前目录下的所有文件名字
            #print(filename)
            #if filename in files_name:
            get_file_name = DOCUMENTS_ROOT + filename
            #else:
            #    raise Warning("不支持的文件类型")
        response_body = Filetype.read_file(get_file_name)

        if response_body is not None:
            response_header = Response_header().choice(True)
        else:
            response_body = Response_header().choice(False)

        return response_header, response_body

    @staticmethod
    def read_binary_flow(filename: str) -> tuple:
        get_file_name = DOCUMENTS_ROOT + filename
        response_body = Filetype.read_file(get_file_name)
        if response_body is not None:
            response_header = Response_header().choice(True)
        else:
            response_body = Response_header().choice(False)

        return response_header, response_body

    @staticmethod
    def read_file(path: str) -> bytes:
        with open(path, 'rb') as file:
            return file.read()



    @staticmethod
    def is_binary_flow(filename: str) -> bool:
        if filename in Filetype._charactor_flow:
            return False
        elif filename in Filetype._binary_flow:
            return True
        else:
            raise Warning("不支持的文件类型")



