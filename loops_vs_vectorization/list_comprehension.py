import timeit


# Using list comprehension
def using_list_comprehension(n):
    return [x * 2 for x in range(n)]


# Using a for loop
def using_for_loop(n):
    result = []
    for x in range(n):
        result.append(x * 2)
    return result


if __name__ == '__main__':
    # Number of iterations for the test
    n = 10000
    # Measure execution time for list comprehension
    list_comp_time = timeit.timeit(lambda: using_list_comprehension(n), number=1000)
    # Measure execution time for a for loop
    for_loop_time = timeit.timeit(lambda: using_for_loop(n), number=1000)
    # Print the results
    print(f"Time taken by List Comprehension: {list_comp_time:.6f} seconds")
    print(f"Time taken by For Loop: {for_loop_time:.6f} seconds")
