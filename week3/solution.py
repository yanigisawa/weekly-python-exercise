import os
from threading import Thread
import glob
import logging
import random
from time import sleep

logging.basicConfig(level=logging.DEBUG, format="(%(threadName)-10s) %(message)s")


def count_words_sequential(pattern):
    files = glob.glob(pattern)
    total_words = 0
    for f in files:
        total_words += count_words_file(f)
    return total_words


def count_words_file(file_name):
    total_words = 0
    if not os.path.isfile(file_name):
        return 0

    with open(file_name, "r") as fi:
        for line in fi:
            total_words += len(line.split())
    return total_words


class CountWords(Thread):
    def __init__(self, file_name):
        super(CountWords, self).__init__()
        self.total_words = 0
        self.file_name = file_name

    def run(self):
        self.total_words = count_words_file(self.file_name)


def count_words_threading(pattern):
    files = glob.glob(pattern)
    total_words = 0
    threads = []
    for f in files:
        th = CountWords(f)
        threads.append(th)
        th.start()

    for t in threads:
        t.join()
        total_words += t.total_words

    return total_words

