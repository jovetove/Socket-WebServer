# 基于Python socket的多线程web服务器

## 1. 功能介绍

此项目为静态内容web服务器，具体功能点包括:

+ 支持多线程并发
+ 支持改变端口和ip 
+ 支持html文件
+ 支持css js文件，以及可自己定义的web文本文件类型
+ 支持 二进制文件，如图片的png jpg jpeg 等游览器可解析的文件类型

此外项目还具有良好的横向扩展能力。


## 2. 项目文件说明


> main.py  主函数文件
>
> WSGIServer.py       socket和多线程处理模块
>
> StrategyFactory.py  请求方法策略工厂
>
> MethodStrategy.py   定义处理方法的策略
>
> Response_header.py  响应消息处理模块
>
> Config.py           读取配置文件
>
> config.cfg          配置文件

## 3. 运行方法

1. 安装python 3.x环境 
2. 安装requirements.txt 第三方库
3. 进入项目目录，在powershell 中输入 `python main.py`
4. 访问 127.0.0.1