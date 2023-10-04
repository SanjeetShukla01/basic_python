# import profile
# import random
# 
# 
# # Define a function that simulates some work
# def my_slow_function():
#     total = 0
#     for _ in range(100000):
#         total += random.randint(1, 1000)
#     return total
# 
# 
# # Profile the function using cProfile
# if __name__ == "__main__":
#     profiler = profile.Profile()
#     profiler.run('my_slow_function()')
#     profiler.print_stats()
# 
#
# import random
# from line_profiler import LineProfiler
# prof = LineProfiler()
#
#
# def profile(func):
#     from functools import wraps
#
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         try:
#             return prof(func)(*args, **kwargs)
#         finally:
#             prof.print_stats()
#
#     return wrapper
#
#
# @profile
# def my_slow_function():
#     total = 0
#     for _ in range(100000):
#         total += random.randint(1, 1000)
#     return total
#
#
# if __name__ == '__main__':
#     my_slow_function()


# from memory_profiler import profile
# import random
#
#
# @profile
# def memory_intensive_function():
#     data = [random.randint(1, 1000) for _ in range(1000000)]
#     result = sum(data)
#     del data  # To free up memory
#     return result



# if __name__ == "__main__":
#     result = memory_intensive_function()
#     print("Result:", result)


import timeit

# Define a function to be benchmarked
def example_function():
    total = 0
    for i in range(1000):
        total += i
    return total

# Measure the execution time of the function using timeit
if __name__ == "__main__":
    execution_time = timeit.timeit("example_function()", globals=globals(), number=10000)
    print("Execution Time:", execution_time, "seconds")


