"""
All other functions
"""

import math
import numpy as np
from typing import List, Iterator


def euler_totients(N: int) -> List[int]:
    """Returns list with phi(i) at index i for i < N."""
    phi = [0] * N
    for i in range(2, N):
        if phi[i] == 0:
            phi[i] = i - 1
            for j in range(2 * i, N, i):
                if phi[j] == 0:
                    phi[j] = j
                phi[j] = (i - 1) * phi[j] // i
    return phi


def euler_totient(n: int, prime_factors: Iterator[int]) -> int:
    """Given n and its prime factors, calculates Euler's totient function."""
    return int(n * math.prod(1 - 1 / p for p in prime_factors))


def mobius_array(N: int) -> np.ndarray:
    """Returns np.ndarray containing μ(n) at index n for n <= N."""
    prime = np.ones(N + 1, np.int8)
    mobius = np.ones(N + 1, np.int8)
    for i in range(2, N + 1):
        if not prime[i]:
            continue
        mobius[i] = -1
        prime[2 * i :: i] = 0
        mobius[2 * i :: i] *= -1
        i_sq = i * i
        mobius[i_sq::i_sq] = 0
    return mobius


def square_free(N: int) -> int:
    """Count of square free numbers <= N"""
    sqrt_N = int(N**0.5)
    mobius = mobius_array(sqrt_N)
    return sum(mobius[i] * (N // (i * i)) for i in range(1, sqrt_N + 1))


def modular_inverse(a: int, n: int) -> int:
    """Multiplicative inverse of a modulo n."""
    t, new_t = 0, 1
    r, new_r = n, a % n
    while new_r:
        q = r // new_r
        t, new_t = new_t, t - q * new_t
        r, new_r = new_r, r - q * new_r
    if r > 1:
        return 0
    if t < 0:
        t += n
    return t


def isqrt2(n: int) -> int:
    """
    Integer square root (equivalent to math.isqrt)
    Designed for up to 64-bit int and compatible with numba
    """
    lower = 0
    roof = n // 2 + 1  # avoid overflow
    while roof - 1 - lower:
        mid = (lower + roof) // 2
        if mid * mid <= n:
            lower = mid
        else:
            roof = mid
    return lower
