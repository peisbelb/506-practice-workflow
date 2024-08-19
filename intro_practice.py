import pandas as pd
import numpy as np

# Variables
number_var = 42
string_var = "Hello, World!"
list_var = [1, 2, 3, 4, 5]
dict_var = {
    'key1': 'value1',
    'key2': [1, 2, 3],
    'key3': {'nested_key': 'nested_value'}
}

# Function
def sample_function(a, b):
    if a > b:
        result = a - b
    else:
        result = b - a
    return result

# Print statements
print("Number Variable:", number_var)
print("String Variable:", string_var)
print("List Variable:", list_var)
print("Dictionary Variable:", dict_var)

# Function call and print result
result = sample_function(10, 5)
print("Function Result:", result)
