# coding=utf-8


class Response_header(object):
    def __init__(self):
        self.response_header = ""

    def choice(self, statu: bool) -> str:
        if statu:
            self.ok()
        else:
            self.not_find()
        return self.response_header

    def not_find(self) -> None:
        self.response_header = "HTTP/1.1 404 not found\r\n"
        self.response_header += "\r\n"

    def ok(self) -> None:
        self.response_header = "HTTP/1.1 200 OK\r\n"
        self.response_header += "\r\n"
