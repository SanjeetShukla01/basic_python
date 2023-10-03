import cProfile
import random


# Define a complex calculation function
def complex_calculation(x):
    # Simulate a complex calculation, e.g., squaring the number
    result = x * x
    return result


# Generate a list of random numbers for demonstration
data = [random.randint(1, 1000) for _ in range(10000)]


# Using the map function for vectorization
def using_map():
    return list(map(complex_calculation, data))


# Using a plain for loop
def using_plain_loop():
    result = []
    for num in data:
        result.append(complex_calculation(num))
    return result


if __name__ == "__main__":
    print("Using map function:")
    cProfile.run("using_map()")

    print("\nUsing plain for loop:")
    cProfile.run("using_plain_loop()")
