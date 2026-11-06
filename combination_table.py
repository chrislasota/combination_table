# combination_table.py
#
# Author: Chris LaSota
# Incept Date: Jul 24, 2021
# Latest Mod : Nov 06, 2026


class CombinationTable():
    ''' Given a positive integer N, this class constructs a lookup table to
        provide fast values for the number of combinations C(N,k).  The class
        instance is constructed by specifying the largest N value that will be
        needed.  The lookup table is held in memory as a list of lists and is
        created very quickly without factorials using Pascal's triangle.  Only
        the "left" half of Pascal's triangle is created, and held in memory,
        including the center values.

        Usage example:
            import combination_table as ct
            a = ct.CombinationTable(52)
            print(f"There are {a.combination(52, 5)} different 5-card " +
                   "poker hands")

        Only builds the "left" half of Pascal's triangle to save on memory,
        since C(N, k) = C(N, N-k)
    '''

    def __init__(self, max_N: int) -> None:
        """Checks that max_N is a non-negative integer, and makes a call
           to _build_table() to initialize the C(N, k) table in memory"""
        if isinstance(max_N, int):
            if max_N < 0:
                raise ValueError("Cannot create CombinationTable(N) " +
                                 "because max_N < 0")
            self._max_N = max_N
            self._combo_table = []
            self._build_table()
        else:
            raise TypeError("Cannot create CombinationTable(N) because " +
                            "N is not an integer")

    def _build_table(self) -> None:
        if self._combo_table:    # Do not rebuild table!
            return
        pascal_row = [1]
        self._combo_table.append(pascal_row)
        # We create the remaining rows of Pascal's triangle using
        # Python language features to do some heavy lifting.  Each
        # subsequent row is created by prepending a copy of the
        # current row with zero, and adding it to another copy of
        # the current row which has a zero appended to its end.  Then
        # we do tweaks to only store half a row
        endcap = [0]
        for dummy in range(self._max_N):
            pascal_row = [row1 + row2 for row1, row2 in \
                zip(endcap + pascal_row, pascal_row + endcap)]
            pascal_row.pop()
            if dummy % 2 == 0:
                pascal_row.append(pascal_row[-1])
            self._combo_table.append(pascal_row)

    def combination(self, n: int, k: int) -> int:
        """Returns the value of C(n, k) from the lookup table.
           If n < 0 or k < 0, a ValueError exception is raised.
           If n > max_N, a ValueError exception is raised.
           For convenience in some use cases, returns 0 if k > n"""
        if not isinstance(n, int):
            raise TypeError("n must be an integer")
        if not isinstance(k, int):
            raise TypeError("k must be an integer")
        if n < 0 or n > self._max_N:
            raise ValueError(f"Error in combination(n, k) : "
                             + f"n must be between 0 and N={self._max_N}")
        if k > n:
            return 0
        if k < 0:
            raise ValueError(f"Error in combination(n,k) : "
                             + f"k must be non-negative")
        if k > n/2:
            k = n - k
        return self._combo_table[n][k]
