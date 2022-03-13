import datetime


def time_stamp_hex_generator():
    time_stamp = datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S%f")
    time_stamp_hex = hex(int(time_stamp))
    return time_stamp_hex[:20]
