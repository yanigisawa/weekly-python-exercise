
def str_range(start, end, step=1):
    for i in range(ord(start), ord(end) + step, step):
        yield chr(i)
