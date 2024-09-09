import logging.handlers

from config import Run_Path


def init_log(path=Run_Path+"/run_log.log", time="D", wait_log_num=3, save_num=5):
    # 1. 创建日志器对象
    logger = logging.getLogger()

    # 2. 设置日志INFO打印级别
    logger.setLevel(logging.DEBUG)

    # 3.1 创建 输出到控制台 处理器对象
    st = logging.StreamHandler()
    # 3.2 创建 输出到日志文件对象
    # 3.3 按小时保存，每3小时后继续进行日志记录，最多保存5个日志文件
    fh = logging.handlers.TimedRotatingFileHandler(path, when=time, interval=wait_log_num,
                                                   backupCount=save_num, encoding='utf-8')
    # 4. 创建日志信息格式
    fmt = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    time_formatter = logging.Formatter(fmt)

    # 控制台打印日志
    # st.setFormatter(time_formatter)
    # logger.addHandler(st)

    # log文件写入日志
    fh.setFormatter(time_formatter)
    logger.addHandler(fh)


if __name__ == '__main__':
    init_log()
    logging.info("info日志")
