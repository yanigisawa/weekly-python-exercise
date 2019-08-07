import operator

def mygetter(*index_args):
    # return operator.itemgetter(*args)
    def foo(item):
        if len(index_args) == 1:
            return item[index_args[0]]
        return tuple([item[i] for i in index_args])

    return foo