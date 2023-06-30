"""
Speed test for prime sieves using various packages.
1. Standard library only - Ok for small N. Returns list. Using Numba helps a lot.
2. Numpy - Faster for larger N and more memory efficient. Returns np.ndarray.
3. Bitarray - Fastest if returning generator and most memory efficent. (Converting to list slower.)

*** INCOMPLETE ***
"""

import math
import sys
import time

import bitarray
import numba
import numpy as np

from math_helpers import prime_sieve, prime_sieve_np, prime_sieve_bitarray


def speed_test(N=10**6, use_njit=False):
    """
    Runs a speed comparison on three prime number sieves from the module.
    Output printed to console.
    """
    print(f'Speed test for prime number sieves for numbers <{N}.')
    print('Standard lib')
    start = time.time()
    if use_njit:
        x = numba.njit(prime_sieve)(N)
    else:
        x = prime_sieve(N)
    end = time.time()
    print(f'Length:{len(x)} Size:{sys.getsizeof(x)/2**20} Time:{end - start}')

    print('Numpy')
    start = time.time()
    if use_njit:
        y = numba.njit(prime_sieve_np)(N)
    else:
        y = prime_sieve_np(N)
    end = time.time()
    print(f'Length:{len(y)} Size:{y.nbytes/2**20} Time:{end - start}')

    print('Bitarray')
    start = time.time()
    z = prime_sieve_bitarray(N)
    mid = time.time()
    z_list = [p for p in z]
    end = time.time()
    print(
        f'Length:{len(z_list)} Size:~{N/(8 * 2**20)} Time1:{mid - start} Time2:{end - mid}')


if __name__ == '__main__':
    """
    On executing this script, the speed test is run.
    """
    if sys.argv:
        try:
            N = 10**int(sys.argv[1])
        except:
            N = 10**6
        if 'njit' in sys.argv:
            use_njit = True
        else:
            use_njit = False
    speed_test(N, use_njit)
