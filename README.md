### The problem

Do you need a way to generate a large number of combinatorial values even faster than Python's ``math.comb()`` method?

If you have **n** unique items and choose **k** of them without replacement, and you *don't care about the order* in which they were selected (e.g. jackpot lottery numbers), then the number of ways to form such **combinations** is

![Binomial coefficients](binomial_coefficients.png)

These values are also known as **binomial coefficients**.

For example, the number of 5-card hands you can draw from a 52-card deck is

![C(52, 5)](poker_hands.png)

If your application requires many values for *C(n,k)*, then efficiency is a serious concern.  If we explicitly calculated the value of *C(n,k)* every time we needed it, we would encounter a number of potential inefficiencies:

 - Calling a function to compute a factorial directly is inefficient
 - Representing large integers in memory can be challenging
 - Even though *C(n,k)* is guaranteed to produce an integer, computing it using floating point math may introduce problems.

Although Python's ``math`` module can quickly provide these values with the ``math.comb()`` method, *it is possible to generate results even faster* by using a clever method to generate a lookup table.

---

### An efficient solution

There is an extremely fast and efficient way to pre-compute a lookup table for the values of *C(n,k)*.  It doesn't require any factorials, and it doesn't require any multiplications or division.  However, it *does* require that we compute **all** of the values of *C(n,k)* up to some maximum *n* value we may need.

What is this computational magic?

**Pascal's triangle**.   Pascal's triangle contains every one of the values of *C(n,k)*, and each row can be computed from the previous row using only sums.

![Pascal's triangle image](pascal.png)

etc....

Creating a lookup table for combinations up a maximum value of *N*  will require us to store *(N+1)(N+2)/2*  integers in memory, and we will have to spend a little bit of time up front to do so.  But once the table is created, acquiring a particular *C(n,k)* value will only require constant time *O(1)* for lookups.

---

The Python code presented here in module file "**combination_table.py**" provides a class to implement this lookup table for *C(n,k)*.

Import the python module "**combination_table**", and then create an instance of the **CombinationTable** class, specifying the largest value of n you will need:

```python
>>> from combination_table import CombinationTable
>>> cnk = CombinationTable(1000)
>>> print(cnk.combination(1000, 500))
270288240945436569515614693625975275496152008446548287007392875106625428705522193898612483924502370165362606085021546104802209750050679917549894219699518475423665484263751733356162464079737887344364574161119497604571044985756287880514600994219426752366915856603136862602484428109296905863799821216320
>>> print(cnk.combination(52, 5))
2598960
>>> print(cnk.combination(20, 5))
15504
>>> print(cnk.combination(12, 4))
495
>>> print(cnk.combination(0, 0))
1
>>> print(cnk.combination(10, 35)
0
>>> # Feel free to try and "break" it by using *n < 0*, *n > max_N*, or *k < 0*
```

Use the **`test_combination_table.py`** file to run a comparison of the time required to compute 10000 values of *C(n,k)* where the *n >= k* values are chosen at random, for a maximum *n* value of 3000.

```
$ python test_combination_table.py
Running timed tests comparing combination_table.combination() to math.comb()

Using CombinationTable...
Elapsed time to initialize the lookup table for max_N = 3000 : 0.717766523361206 seconds
Elapsed time to compute 10000 random values of C(n,k) for max_N = 3000 : 0.022130489349365234 seconds

Using math.comb()...
Elapsed time to compute 10000 random values of C(n,k) for max_N = 3000 : 2.3813798427581787 seconds
```

As you can see, if you can afford the memory and a small set-up time, you can gain significant speedup using a lookup table to obtain values of *C(n,k)*.



