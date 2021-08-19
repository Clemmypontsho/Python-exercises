import numpy as np


def doubler(numbers):
    
    n_array = []
    for num in numbers:
        n_array.append(num * 2)
    return np.array(n_array)


if __name__ == "__main__":
    arr = np.array([3, 5, 2, 6, 7])
    print(doubler(arr))

