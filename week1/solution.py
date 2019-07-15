def magic_tuples(total, count):
    return (
        (i, x)
        for i in range(count)
        for x in range(count)
        if i + x == total
    )
    # high, low = count - 1, 1
    # for _ in range(total):
    #     if low >= count:
    #         return
    #     if high + low == total:
    #         yield (high, low)
    #     high -= 1
    #     low += 1
