# coding=utf-8
import config
import time

my_config = config.get_config()
number_of_loops = my_config.getint("Global", "number_of_loops")


def good_list():
    my_list = [value for value in range(number_of_loops)]


def modulus_validation(value):
    return value % 2 == 0


def good_list_validation():
    my_list = [value for value in range(number_of_loops)
               if modulus_validation(value)]


def good_tuple():
    my_tuple = tuple(value for value in range(number_of_loops))


def good_set():
    my_set = {value for value in range(number_of_loops)}


def good_dict():
    my_dict = {value: value for value in range(number_of_loops)}

start = time.time()
good_list_validation()
end = time.time()
print(end - start)
