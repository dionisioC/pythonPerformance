# coding=utf-8
from memory_profiler import profile
import config
import time

my_config = config.get_config()
number_of_loops = my_config.getint("Global", "number_of_loops")


def generator():
    return (x*2 for x in xrange(number_of_loops))

@profile
def generator_testing():
    for loop_count in generator():
        foo = loop_count + 3

start = time.time()
generator_testing()
end = time.time()
print(end - start)
