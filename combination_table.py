# combination_table.py
#
# Author: Chris LaSota
# Date: July 24, 2021


class CombinationTable():

    """ Given a positive integer N, this class constructs a lookup table to
        provide fast values for the number of combinations C(N,k).  The class
        instance is constructed by specifying the largest N value that will be
        needed.  The lookup table is held in memory as a list of lists and is
        created very quickly without factorials using Pascal's triangle
    """

    def __new__(cls, max_size: int):
        if max_size < 0:
            raise Exception("Cannot create CombinationTable(n) object because n < 0")
        else:
            return super().__new__(cls)

    def __init__(self, max_size: int) -> None:
        self._max_size = max_size
        self._combo_table = []
        self._build_table()

    def _build_table(self) -> None:
        pascal_row = [1]
        self._combo_table.append(pascal_row)
        endcap = [0]
        for dummy in range(self._max_size):
            pascal_row = [row1 + row2 for row1, row2 in zip(pascal_row + endcap, endcap + pascal_row)]
            self._combo_table.append(pascal_row)

    def combination(self, n: int, k: int) -> int:
        """Returns the value of C(n,k) from the lookup table"""

        if n < 0 or n > self._max_size:
            raise Exception(f"Error in combination(n,k) : " +
                            f"n must be between 0 and {self._max_size}")
        if k < 0 or k > n:
            raise Exception(f"Error in combination(n,k) : " + 
                            f"k must be between 0 and {n}")
        return self._combo_table[n][k]
