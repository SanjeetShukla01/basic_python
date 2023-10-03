import cProfile
import random
import time
from functools import reduce


# Define a complex calculation function
def some_complex_calculation(x, y):
    # Simulate a complex calculation, e.g., multiplying two numbers
    result = x * y
    return result


# Using the reduce function for vectorization
def using_reduce(func, data: list):
    t1 = time.time()
    result = reduce(func, data)
    t2 = time.time()
    return result, t2 - t1


# Using a plain for loop
def using_loop(data):
    t1 = time.time()
    result = 1
    for num in data:
        result *= num
    t2 = time.time()
    return result, t2-t1


if __name__ == "__main__":
    # Generate a list of random numbers for demonstration
    data = [random.randint(1, 1000) for _ in range(10000)]
    result_of_reduce, time_taken_reduce = using_reduce(some_complex_calculation, data)
    print("Using reduce function:")
    print("Execution Time for reduce function is:", time_taken_reduce, "seconds")

    result_plain_loop, time_plain_loop = using_loop(data)
    print("\nUsing plain for loop:")
    print("Execution Time using loop is:", time_plain_loop, "seconds")
