# test_combinationtable.py
#
# Author: Chris LaSota
# Date: July 25, 2021

from combination_table import CombinationTable
from random import randint

MAX_N = 52
test_table = CombinationTable(MAX_N)

def testing() -> None:
    for items in range(MAX_N + 1):
        for choices in range(items + 1):
            print_test_results(items, choices)

# UNCOMMENT EACH LINE TO TEST EACH ERROR CONDITION INDIVIDUALLY

# Create error -- n cannot be greater than MAX_N 
    # print_test_results(MAX_N + 1, 1)
# Create error -- in C(n,k) k must be less than or equal to n
    # print_test_results(MAX_N, MAX_N + 1)
# Create error -- in C(n,k) the value of n and k must be positive
    # print_test_results(-1, 0)
    # print_test_results(MAX_N, -1)

def print_test_results(n: int, k: int) -> None:
    print(f"C({n},{k}) = {test_table.combination(n,k)}")


if __name__ == '__main__':
    testing()
