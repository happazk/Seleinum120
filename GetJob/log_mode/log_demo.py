import logging


# logging.basicConfig(  # 通过具体的参数来更改logging模块默认行为；
#         level=logging.ERROR,  # 设置告警级别为ERROR；
#         format="%(asctime)s---%(lineno)s----%(name)s: %(message)s",  # 自定义打印的格式；
#         filename="yinzhengjie.txt",  # 将日志输出到指定的文件中；
#         filemode="a",  # 以追加的方式将日志写入文件中，w是以覆盖写的方式哟;
# )
# logging.debug("debug message")  # 告警级别最低，只有在诊断问题时才有兴趣的详细信息。
#
# logging.info("info message")  # 告警级别比debug要高，确认事情按预期进行。
#
# logging.warning("warning message")  # 告警级别比info要高，该模式是默认的告警级别！预示着一些意想不到的事情发生，或在不久的将来出现一些问题（例如“磁盘空间低”）。该软件仍在正常工作。
#
# logging.error("error message")  # 告警级别要比warning药膏，由于一个更严重的问题，该软件还不能执行某些功能。
#
# logging.critical("critical message")  # 告警级别要比error还要高，严重错误，表明程序本身可能无法继续运行。


class LogMod():
    def log_err(self, file='log_info.txt', message='', write=True):
        logging.basicConfig(  # 通过具体的参数来更改logging模块默认行为；
                level=logging.ERROR,  # 设置告警级别为ERROR；
                format="%(asctime)s---%(lineno)s----%(funcName)s: %(message)s",  # 自定义打印的格式；
                filename=file,  # 将日志输出到指定的文件中；
                filemode="a",  # 以追加的方式将日志写入文件中，w是以覆盖写的方式哟;
        )
        if write != True:
            return
        logging.error(message)

    def log_debug(self, file='log_info.txt', message='', write=True):
        logging.basicConfig(  # 通过具体的参数来更改logging模块默认行为；
                level=logging.DEBUG,  # 设置告警级别为DEBUG；
                format="%(asctime)s---%(lineno)s----%(funcName)s: %(message)s",  # 自定义打印的格式；
                filename=file,  # 将日志输出到指定的文件中；
                filemode="a",  # 以追加的方式将日志写入文件中，w是以覆盖写的方式哟;
        )
        if write != True:
            return
        logging.debug(message)

    def log_info(self, file='log_info.txt', message='', write=True):
        logging.basicConfig(  # 通过具体的参数来更改logging模块默认行为；
                level=logging.INFO,  # 设置告警级别为INFO；
                format="%(asctime)s---%(lineno)s----%(funcName)s: %(message)s",  # 自定义打印的格式；
                filename=file,  # 将日志输出到指定的文件中；
                filemode="a",  # 以追加的方式将日志写入文件中，w是以覆盖写的方式哟;
        )
        if write != True:
            return
        logging.info(message)


"""
19 format参数中可能用到的格式化串:
20     1>.%(name)s
21          Logger的名字
22     2>.%(levelno)s
23         数字形式的日志级别
24     3>.%(levelname)s
25         文本形式的日志级别
26     4>.%(pathname)s
27         调用日志输出函数的模块的完整路径名，可能没有
28     5>.%(filename)s
29         调用日志输出函数的模块的文件名
30     6>.%(module)s
31         调用日志输出函数的模块名
32     7>.%(funcName)s
33         调用日志输出函数的函数名
34     8>.%(lineno)d
35         调用日志输出函数的语句所在的代码行
36     9>.%(created)f
37         当前时间，用UNIX标准的表示时间的浮 点数表示
38     10>.%(relativeCreated)d
39         输出日志信息时的，自Logger创建以 来的毫秒数
40     11>.%(asctime)s
41         字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
42     12>.%(thread)d
43         线程ID。可能没有
44     13>.%(threadName)s
45         线程名。可能没有
46     14>.%(process)d
47         进程ID。可能没有
48     15>.%(message)s
49         用户输出的消息
50 """
