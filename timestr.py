__all__ = (
    'seconds_to_str',
)


def conver(seconds, times, chr, s):
    if seconds >= times:
        a = seconds // times
        s += "{:02.0f}".format(a) + chr
        seconds -= a * times
    elif s:
        s += f'00'+chr
    return s, seconds

def seconds_to_str(seconds: int) -> str:
    """
    Функция должна вернуть текстовое представление времени
    20 -> 20s
    60 -> 01m00s
    65 -> 01m05s
    3700 -> 01h01m40s
    93600 -> 01d02h00m00s
    """
    s = ""
    s, seconds  = conver(seconds, 86400, 'd',s)
    s, seconds  = conver(seconds, 3600, 'h',s)
    s, seconds  = conver(seconds, 60, 'm',s)
    s += "{:02.0f}s".format(seconds)
    return s

print(seconds_to_str(93600))

