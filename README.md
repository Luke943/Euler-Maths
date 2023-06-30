# Math Helper Functions

## Description

A collection of helper functions for mathematical calculations, mostly concerned with prime numbers and basic algebra on natural numbers.

## Module Dependencies

To improve execution speed and memory usage, many of the functions take advantage of either:
- [Numpy](https://numpy.org/)
- [Bitarray](https://pypi.org/project/bitarray/)

## Contents

- Prime number sieves:
    1. using only the standard library
    2. using Numpy
    3. using Bitarray
- Prime factor sieve
- Primality tests:
    1. a basic/direct test 
    2. a Miller-Raben test (useful for large integers)
- Euler totient function
- Euler totient sieve
- Square-free sieve
- Modular inverse

*For comparison of the performance of the prime sieves, see Performance Test below.*

## Improving Performance at Runtime

The functions using native Python and Numpy are designed to be compatible with the [Numba](https://numba.pydata.org/)'s JIT compiler. The exception is the version of the prime seive that uses the Bitarray module, which is not compatible with Numba.

When dealing with large enough values, Numba can significantly improve execution speed compared to vanilla Python.

To take advantage of this in your script, use the `numba.njit` decorator on the desired function.

## Performance Test

***TODO - speed and memory test***

## Motivation

The functions contained here are commonly used in solving [Project Euler](https://projecteuler.net/) problems.

![ProjectEulerProfile](https://projecteuler.net/profile/Luke943.png)

*Note: These are NOT solutions to any particular problem.*
