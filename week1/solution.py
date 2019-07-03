def magic_tuples(total, count):
    high, low = count - 1, 1
    for _ in range(total):
        if low >= count:
            return
        if high + low == total:
            yield (high, low)
        high -= 1
        low += 1
