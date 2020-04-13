# -* - coding: UTF-8 -* -
from configparser import ConfigParser


def read_cfg(path="config.cfg") -> ConfigParser:
    # 生成config对象
    config = ConfigParser()
    # 用config对象读取配置文件
    config.read(path)
    return config