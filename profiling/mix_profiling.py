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


from line_profiler import LineProfiler
profiler = LineProfiler()
@profiler.profile
def my_slow_function():
    total = 0
    for _ in range(100000):
        total += random.randint(1, 1000)
    return total

if __name__ == '__main__':
    my_lazy_function
