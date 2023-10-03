import timeit


def vectorized_operation(original_list):
    return list(map(lambda x: x * 2, original_list))


# Non-vectorized operation using a for loop
def non_vectorized_operation(original_list):
    result = []
    for x in original_list:
        result.append(x * 2)
    return result


if __name__ == '__main__':
    original_list = [1, 2, 3, 4, 5]
    # Measure execution time for vectorized operation
    vectorized_time = timeit.timeit(lambda: vectorized_operation(original_list), number=1000000)

    # Measure execution time for non-vectorized operation
    non_vectorized_time = timeit.timeit(lambda: non_vectorized_operation(original_list), number=1000000)

    # Print the results
    print(f"Time taken by Vectorized Operation: {vectorized_time:.6f} seconds")
    print(f"Time taken by Non-Vectorized Operation: {non_vectorized_time:.6f} seconds")
