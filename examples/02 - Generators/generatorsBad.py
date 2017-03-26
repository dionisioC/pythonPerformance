# coding=utf-8
from memory_profiler import profile
import config
import time

my_config = config.get_config()
number_of_loops = my_config.getint("Global", "number_of_loops")


def generator():
    return [x*2 for x in range(number_of_loops)]


@profile
def generator_testing():
    for loop_count in generator():
        foo = loop_count + 3

start = time.time()
generator_testing()
end = time.time()
print(end - start)

# # coding=utf-8
#
# Use Generators
#
# Generators are objects that generate sequences one item at a time.
# This provides a great gain in performance when working with large data, because it won't generate the whole sequence unless needed, and it’s also a memory saver. A simple way to use generators is very similar to the comprehensions we saw above, but you encase the sentence with () instead of [] for example:
#
# my_generator = (do_something_with(value) for value in range(10))
#
# my_generator
# <generator object <genexpr> at 0x7f0d31c207e0>
# The range function itself returns a generator (unless you're using legacy Python 2, in which case you need to use xrange).
#
# Once you have a generator, call next to iterate over its items, or use it as a parameter to a sequence constructor if you really need all the values:
#
# next(my_generator)
# 0
# next(my_generator)
# 2
# To create your own generators, use the yield keyword inside a loop instead of a regular return at the end of a function or method. Each time you call next on it, your code will run until it reaches a yield statement, and it saves the state for the next time you ask for a value.
#
# # this is a generator that infinitely returns a sequence of numbers, adding 1 to the previous
# def my_generator_creator(start_value):
#     while True:
#         yield start_value
#         start_value += 1
#
# my_integer_generator = my_generator_creator(0)
#
# my_integer_generator
# <generator object my_generator_creator at 0x7f0d31c20708>
# next(my_integer_generator)
# 0
# next(my_integer_generator)
# 1
# The benefits of generators in this case are obvious—you would never end up generating numbers if you were to create the whole sequence before using it. A great use of this, for example, is for reading a file stream.