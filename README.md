# Euler Maths

## Description

A collection of useful functions for mathematical calculations, mostly concerned with prime numbers and basic algebra on natural numbers.

### Key features
- Prime number sieve
- Primality test
- Prime factors sieve
- Euler's totient function
- Mobius function
- Modular inverse

### Motivation
The functions contained here are commonly used in solving [Project Euler](https://projecteuler.net/) problems.

![ProjectEulerProfile](https://projecteuler.net/profile/Luke943.png)

*Note: These are NOT solutions to any particular problem.*

## Module Dependencies

To improve execution speed and memory usage, many of the functions take advantage of either:
- [Numpy](https://numpy.org/)
- [Bitarray](https://pypi.org/project/bitarray/)

## Contents

- `primes(N)` - Performs prime sieve and returns an array of primes <N.
- `primes_iter(N)` - Rerforms prime sieve and returns bitarray iterator of primes <N.
- `prime_factors(N)` - Returns array of unique prime factors for each number < N.
- `is_prime(n)` - Determines if n is prime (utilising the Miller-Rabin test for large values).
- `euler_totients(N)` - Returns an array with value of Euler's totient function for numbers <N.
- `euler_totient(n, prime_factors)` - Calculates Euler's totient function of n given a list of its prime factors.
- `mobius_array(N)` - Returns an array with value of the Mobius function for numbers <N.
- `square_free(N)` - Counts of the number of square-free values <N.
- `modular_inverse(a, n)` - Computes the inverse of a modulo n.
- `isqrt2(n)` - Integer square-root of n. Same functionality as the standard library `math.isqrt` function, but compatible with Numba.

## Installation

The package can be installed from PyPI by running:
```bash
pip install euler-maths
```

## Usage

Once installed, simply import the module and use the functions it provides.

```python
import euler_maths

euler_maths.primes(10)
# array([2, 3, 5, 7])

euler_maths.euler_totients(10)
# [0, 0, 1, 2, 2, 4, 2, 6, 4, 6]
```

## Improving Performance at Runtime

The functions using native Python and Numpy are designed to be compatible with the [Numba](https://numba.pydata.org/)'s JIT compiler. The only exception is `primes_iter`, which uses the Bitarray module and is not compatible with Numba.

When dealing with large enough values, Numba can significantly improve execution speed compared to vanilla Python. To take advantage of this in your script, use the `numba.njit` decorator on the desired function.

##  Prime Sieves Speed Test

Comparison of performance of various prime sieve implementations. Times are given in seconds.

| $N$ | Std Lib | Numpy | Numpy with Numba | Bitarray (iterator) | Bitarray to list |
| :-: | :-: | :-: | :-: | :-: | :-: |
| 1,000 |0.001999 | 0.0 | - | 0.0 | 0.0 |
| 1,000,000 | 0.148910 | 0.007995 |  - |0.001998 | 0.015990 | 
| 10,000,000 | 1.499077 | 0.101938 | - |0.021986 | 0.105933 |
| 100,000,000 | 16.03813 | 1.068342 | 1.928385 |0.380769 | 0.946416 | 
| 1,000,000,000 | 180.1974 | 14.23469 | 11.39456 |5.243182 | 8.692384 |
| 10,000,000,000 | - | 166.3705 | 133.3257 |71.00818 | 87.48354 |

*All tests run with latest versions of Python 3.11 and dependent modules as of 12/07/23.*

Usage of Numba helps only when sieving close to 10<sup>9</sup> integers. However, it may prove useful at lower orders depending on what further computions need to be done.
