# coding=utf-8
import config
import time

my_config = config.get_config()
number_of_loops = my_config.getint("Global", "number_of_loops")
my_set = {value for value in range(number_of_loops)}

start = time.time()
number_of_loops - 10 in my_set
end = time.time()
print(end - start)