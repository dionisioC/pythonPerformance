# coding=utf-8
import config
import time

my_config = config.get_config()
number_of_loops = my_config.getint("Global", "number_of_loops")


def expensive_function(value):
    time.sleep(0.5)
    return value * 2


def cache_testing():
    for loop_count in range(number_of_loops):
        expensive_function(loop_count % 8)


start = time.time()
cache_testing()
end = time.time()
print(end - start)
