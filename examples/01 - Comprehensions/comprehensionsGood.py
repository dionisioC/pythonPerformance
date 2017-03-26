# coding=utf-8
import config
import time

my_config = config.get_config()
number_of_loops = my_config.getint("Global", "number_of_loops")


def good_list():
    my_list = [value for value in range(number_of_loops)]

start = time.time()
good_list()
end = time.time()
print(end - start)
