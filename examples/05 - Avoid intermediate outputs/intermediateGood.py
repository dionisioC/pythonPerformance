# coding=utf-8
import config
import time

my_config = config.get_config()
number_of_loops = my_config.getint("Global", "number_of_loops")


def intermediate_testing():
    for loop_count in range(number_of_loops):
        print ('Hi how are you')


def intermediate_no_print_testing():
    for loop_count in range(number_of_loops):
        foo = 20 + 20 + 20

start = time.time()
intermediate_no_print_testing()
end = time.time()
print(end - start)
