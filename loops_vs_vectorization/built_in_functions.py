import timeit

# Original list and vectorized operation
original_list = [1, 2, 3, 4, 5]

def vectorized_operation(original_list):
    return list(map(lambda x: x * 2, original_list))

# Non-vectorized operation using a for loop
def non_vectorized_operation(original_list):
    result = []
    for x in original_list:
        result.append(x * 2)
    return result

# Measure execution time for vectorized operation
vectorized_time = timeit.timeit(lambda: vectorized_operation(original_list), number=1000000)

# Measure execution time for non-vectorized operation
non_vectorized_time = timeit.timeit(lambda: non_vectorized_operation(original_list), number=1000000)

# Print the results
print(f"Vectorized Operation Time: {vectorized_time:.6f} seconds")
print(f"Non-Vectorized Operation Time: {non_vectorized_time:.6f} seconds")
