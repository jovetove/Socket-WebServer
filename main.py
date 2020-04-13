# coding=utf-8
from Config import read_cfg
from WSGIServer import WSGIServer


if __name__ == "__main__":
    cfg = read_cfg()
    SERVER_ADDR = (cfg.get("SOCKET", "HOST"), cfg.getint("SOCKET", "PORT"))
    print(SERVER_ADDR)
    httpd = WSGIServer(SERVER_ADDR)
    print("web Server: Serving HTTP on port %d ...\n " % cfg.getint("SOCKET", "PORT"))
    httpd.serve_forever()
