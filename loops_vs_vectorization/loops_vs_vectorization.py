import time
import numpy as np


def create_nested_list_using_loops(n):
    t1 = time.time()
    nested_list = []
    value = 1  # Initial value to start with
    for _ in range(n):
        row = []
        for _ in range(n):
            row.append(value)
            value += 1  # Increment the value for the next element
        nested_list.append(row)
    print(nested_list)
    t2 = time.time()
    print(f"With for loop it took {t2-t1} seconds \n")
    return nested_list


def create_nested_list_using_vectorization(n):
    tv1 = time.time()
    value = 1  # Initial value to start with
    nested_list = [[value + i + j for j in range(n)] for i in range(0, n * n, n)]
    print(nested_list)
    tv2 = time.time()
    print(f"With vectorization it took {tv2-tv1} seconds")
    return nested_list


def create_nested_list_numpy(n):
    t1 = time.time()
    value = 1  # Initial value to start with
    arr = np.arange(value, value + n * n, n)
    nested_list = arr + np.arange(n)
    print(nested_list.tolist())
    t2 = time.time()
    print(f"With vectorization it took {t2-t1} seconds")


def create_multidimensional_array(shape, initial_value=0, dtype=float):
    t1 = time.time()
    print(np.full(shape, initial_value, dtype=dtype))
    t2 = time.time()
    print(f"With vectorization it took {t2 - t1} seconds")


def create_multidimensional_incremental_array_vectorized(shape, start_value=0, dtype=int):
    # t1 = time.time()
    total_elements = np.prod(shape)
    arr = np.arange(start_value, start_value + total_elements, dtype=dtype).reshape(shape)
    # print(arr)
    # t2 = time.time()
    # print(f"With vectorization it took {t2 - t1} seconds")
    return arr


def multiply_nested_list_by_n_loop(nested_list, n):
    t1 = time.time()
    result = []
    for row in nested_list:
        new_row = [element * n for element in row]
        result.append(new_row)
    print(result)
    t2 = time.time()
    print(f"With for loop it took {t2 - t1} seconds \n")


def multiply_nested_list_by_n_vectorized(nested_list, n):
    t1 = time.time()
    # Convert the nested list to a NumPy array
    arr = np.array(nested_list)
    # Perform vectorized multiplication
    result = arr * n
    # Convert the result back to a nested list
    result_nested_list = result.tolist()
    print(result_nested_list)
    t2 = time.time()
    print(f"With vectorization it took {t2 - t1} seconds \n")


def multiply_numpy_array_by_n_loop(arr, n):
    t1 = time.time()
    result = np.empty_like(arr)
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            result[i, j] = arr[i, j] * n
    print(result)
    t2 = time.time()
    print(f"With for loop it took {t2 - t1} seconds \n")


def multiply_numpy_array_by_n_vectorized(arr, n):
    t1 = time.time()
    result = arr * n
    print(result)
    t2 = time.time()
    print(f"With vectorization it took {t2 - t1} seconds \n")


if __name__ == '__main__':
    # create_nested_list_using_loops(10)
    # create_nested_list_using_vectorization(10)
    # create_nested_list_numpy(10)
    # create_multidimensional_array((10, 10), 1, int)
    # create_multidimensional_incremental_array_vectorized((10, 10), 1, int)

    nested_list = create_nested_list_using_vectorization(10)
    multiply_nested_list_by_n_loop(nested_list, 7)
    multiply_nested_list_by_n_vectorized(nested_list, 7)

    # numpy_array = create_multidimensional_incremental_array_vectorized((10, 10), 1, int)
    # multiply_numpy_array_by_n_loop(numpy_array, 7)
    # multiply_numpy_array_by_n_vectorized(numpy_array, 7)


original_list = [1, 2, 3, 4, 5]
result = [x * 2 for x in original_list]
