import time


def meeting_start_time(time_s):
    # time_format = time.strptime(time_start, "%Y-%m-%d %H:%M:%S")
    # 获取当前时间
    time_current = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    # 转换为时间戳
    time_format = time.strptime(time_current, "%Y-%m-%d %H:%M:%S")
    start_time = time.localtime(int(time.mktime(time_format) + time_s))
    return str(time.strftime("%Y-%m-%d %H:%M:%S", start_time))


def meeting_end_time(time_s):
    # 获取当前时间
    time_current = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    # 转换为时间戳
    time_format = time.strptime(time_current, "%Y-%m-%d %H:%M:%S")
    end_time = time.localtime(int(time.mktime(time_format) + time_s))
    return str(time.strftime("%Y-%m-%d %H:%M:%S", end_time))
