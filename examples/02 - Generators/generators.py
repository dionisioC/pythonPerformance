# coding=utf-8
from memory_profiler import profile
import config
import time

my_config = config.get_config()
number_of_loops = my_config.getint("Global", "number_of_loops")


def my_generator(start_value):
    while start_value < number_of_loops:
        yield start_value
        start_value += 1


@profile
def generator_testing():
    for loop_count in my_generator(0):
        foo = loop_count + 3

start = time.time()
generator_testing()
end = time.time()
print(end - start)
