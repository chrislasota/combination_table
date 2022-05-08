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
        k = random.randint(0, n)
        c = math.comb(n, k)

def test_comb_table(cnk_table, max_N: int, trials: int) -> None:
    for trial in range(trials):
        n = random.randint(0, max_N)
        k = random.randint(0, n)
        c = cnk_table.combination(n, k)

if __name__ == '__main__':
    max_N = 3000
    num_trials = 10000

    print("Running timed tests comparing combination_table.combination() to math.comb()")
    print()
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


