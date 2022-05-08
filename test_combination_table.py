# test_combination_table.py
#
# Author: Chris LaSota
# Incept Date: July 25, 2021
# Latest Mod : May 8, 2022

import combination_table
import random
import math
import time

def test_math_comb(max_N: int, trials: int) -> None:
    for trial in range(trials):
        n = random.randint(0, max_N)
        k = random.randint(0, max_N)
        if n >= k:
            c = math.comb(n, k)
        else:
            c = math.comb(k, n)

def test_comb_table(cnk_table, max_N: int, trials: int) -> None:
    for trial in range(trials):
        n = random.randint(0, max_N)
        k = random.randint(0, max_N)
        if n >= k:
            c = cnk_table.combination(n, k)
        else:
            c = cnk_table.combination(k, n)

# UNCOMMENT EACH LINE TO TEST EACH ERROR CONDITION INDIVIDUALLY

# Create error -- n cannot be greater than MAX_N
    # print_test_results(MAX_N + 1, 1)
# Create error -- in C(n,k) k must be less than or equal to n
    # print_test_results(MAX_N, MAX_N + 1)
# Create error -- in C(n,k) the value of n and k must be positive
    # print_test_results(-1, 0)
    # print_test_results(MAX_N, -1)

#def print_test_results(n: int, k: int) -> None:
#    print(f"C({n},{k}) = {test_table.combination(n,k)}")



if __name__ == '__main__':
    print("Running timed tests comparing combination_table.combination() to math.comb()")
    print()

    max_N = 3000  # modify this as you need for different tests
    num_trials = 10000

    print("Using CombinationTable...")
    start_time = time.time()
    ctable = combination_table.CombinationTable(max_N)
    stop_time = time.time()
    print(f"Elapsed time to initialize the lookup table for max_N = {max_N} : {stop_time - start_time} seconds")

    start_time = time.time()
    test_comb_table(ctable, max_N, num_trials)
    stop_time = time.time()
    print(f"Elapsed time to compute {num_trials} random values of C(n,k) for max_N = {max_N} : {stop_time - start_time} seconds")
    print()

    start_time = time.time()
    test_math_comb(max_N, num_trials)
    stop_time = time.time()
    print("Using math.comb()...")
    print(f"Elapsed time to compute {num_trials} random values of C(n,k) for max_N = {max_N} : {stop_time - start_time} seconds")


